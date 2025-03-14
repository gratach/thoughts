# How to merge multiple PDFs into one

[Multiple possibilities](https://itsfoss.com/merge-pdf-linux/)

## Command line

==ATTENTION: The last argument is the output file and will be overridden==

```
pdfunite in-1.pdf in-2.pdf in-n.pdf out.pdf
```

## Using Libre Office

* Open all pdf files with Libre Office Draw.
* Select the pages that should be appended to the other document by clicking on them in the left pages bar (press shift or strg to select multiple ones)
* Ctrl-C
* Go to the pages bar where they should be inserted
* Ctrl-V
* If asked if the pages should be scaled select 'no'
* Export as pdf

