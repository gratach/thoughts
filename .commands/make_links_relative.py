from pathlib import Path
import os
import argparse

def getAllMDFileNamesRecursive(basePath: Path):
    retDict = {}
    for child in basePath.iterdir():
        if child.is_dir():
            childDict = getAllMDFileNamesRecursive(child)
            for k, v in childDict.items():
                if k in retDict:
                    print(f"{k} in {retDict} insert {v}")
                    retDict[k] = retDict[k] | v
                    print(f"result: {retDict[k]}")
                else:
                    retDict[k] = v
        if child.is_file() and child.suffix == ".md":
            retDict[child.stem] = {child}
    return retDict

def findLinkPositions(text):
    allPositions = []
    linkStart = None
    bracketActivated = False
    bracketCount = 0
    quoteCount = 0
    quoteActivated = False
    trippleQuotesActivated = False
    i = 0
    while i < len(text):
        if quoteActivated:
            if text[i] == "`":
                if quoteCount == 0:
                    quoteActivated = False
                else:
                    quoteCount += 1
                    if quoteCount == 3:
                        quoteActivated = False
                        trippleQuotesActivated = True
                        quoteCount = 0
            else:
                quoteCount = 0
        elif trippleQuotesActivated:
            if text[i] == "`":
                quoteCount += 1
                if quoteCount == 3:
                    trippleQuotesActivated = False
                    quoteCount = 0
            else:
                quoteCount = 0
        else:
            if text[i] == "`":
                quoteCount = 1
                quoteActivated = True
            elif bracketActivated:
                if text[i] == "]":
                    bracketCount += 1
                    if bracketCount == 2:
                        bracketActivated = False
                        bracketCount = 0
                        allPositions.append([linkStart, i + 1])
                else:
                    bracketCount = 0
            else:
                if text[i] == "[":
                    bracketCount += 1
                    if bracketCount == 2:
                        bracketActivated = True
                        bracketCount = 0
                        linkStart = i - 1
                else:
                    bracketCount = 0
        i += 1
    return allPositions


def replaceLinks(text, fileNamesDict, path: Path):
    positions = findLinkPositions(text)
    replacements = []
    for p in positions:
        doublebracketlinkparts = text[p[0] + 2 : p[1] -2].split("|")
        doublebracketlinkfilename = doublebracketlinkparts[0]
        targetpaths = [*fileNamesDict[doublebracketlinkfilename]]
        print(f"Get link for {doublebracketlinkparts} {targetpaths}")
        if len(targetpaths) > 1:
            resultPath: Path = None
            while resultPath is None:
                try:
                    print("Select target path:")
                    for i, p in enumerate(targetpaths):
                        print(f"   {i}: {p}")
                    resultPath = targetpaths[int(input("Select result path id: "))]
                except:
                    print("Invalid input.")
        else:
            resultPath: Path = targetpaths[0]
        doublebracketlinkname = doublebracketlinkparts[1] if len(doublebracketlinkparts) > 1 else doublebracketlinkfilename
        replacements.append(f"[{doublebracketlinkname}]({os.path.relpath(resultPath, path)})")
    returnArray = [text] if len(positions) == 0 else [text[0: positions[0][0]]]
    for i in range(1, len(positions)):
        returnArray.append(replacements[i - 1])
        returnArray.append(text[positions[i - 1][1]:positions[i][0]])
    if len(positions) > 0:
        returnArray.append(replacements[-1])
        returnArray.append(text[positions[-1][1]:])
    return "".join(returnArray)        

def makeLinksRelative(pathOfFileThatContainsTheLinks):
    scriptDir = Path(__file__).parent.absolute()
    pathOfFileThatContainsTheLinks = Path(pathOfFileThatContainsTheLinks).absolute()
    commonPath = Path(os.path.commonpath([scriptDir, pathOfFileThatContainsTheLinks]))
    namePathDict = getAllMDFileNamesRecursive(commonPath)
    with pathOfFileThatContainsTheLinks.open("r") as f:
        text = f.read()
    replacedText = replaceLinks(text, namePathDict, pathOfFileThatContainsTheLinks.parent)
    with pathOfFileThatContainsTheLinks.open("w") as f:
        f.write(replacedText)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert [[bracket|links]] to (links)[./that/are/relative]")
    parser.add_argument("filepath", type=str, help="The path of the file that contains the links that should be converted.")
    args = parser.parse_args()

    # Use argument
    if args.filepath:
        makeLinksRelative(args.filepath)
    else:
        print("Filepath expected!")