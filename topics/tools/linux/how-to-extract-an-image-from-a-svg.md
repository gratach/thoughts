# How to extract an image from a SVG

1. Open Inkscape
2. Select the image
3. Open the built-in `XML Editor` (Shift+Ctrl+X)
4. Select the `xlink:href` attribute, which will contain the image as [data: URI](http://en.wikipedia.org/wiki/Data_URI_scheme)
5. Copy the entire `data:` URI
6. Paste that `data:` URI into a browser, and save it from there.

[source](https://superuser.com/questions/299977/how-to-extract-an-embedded-image-from-a-svg-file)