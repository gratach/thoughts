# Linkinator

[Linkinator](https://github.com/JustinBeckwith/linkinator) is a tool to scrape the pages of a webpage and check if its links are broken or not.

## Install:
- From npm repo:
    ```
    npm install -g linkinator
    ```
    Run then with:
    ```
    linkinator
    ```
- Or from git repo
    ```
    git clone https://github.com/JustinBeckwith/linkinator.git
    cd linkinator
    npm install .
    ```
    Run then with:
    ```
    node build/src/cli.js
    ```
## Usage
```
linkinator https://my-url.example.com --recurse
```
## Rate limit

There is an issue that the software can exceed the rate limit of the server which can lead to some links being marked as broken even though they are not.

There is an [issue](https://github.com/JustinBeckwith/linkinator/issues/534) about that on github.
It can be tested on [this website](https://linkinator-test.debablo.de/) by running:
```
linkinator -r https://linkinator-test.debablo.de
```

## See also
[What software can be used to monitor website setups](../../../questions/informatics/server/what-software-can-be-used-to-monitor-website-setups.md)