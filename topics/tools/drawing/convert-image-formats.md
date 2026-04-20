# Convert image formats

Install image magic to use convert.
```
sudo apt-get install imagemagick
```
## png to jpg

An image can be converted from png to jpg by running:
```
convert my-image-name.png my-image-name.jpeg
```
As described [here](https://www.tecmint.com/linux-image-conversion-tools/) all images in the working directory can be converted from png to jpeg using the following command:
```bash
ls -1 *.png | xargs -n 1 bash -c 'convert "$0" "${0%.png}.jpg"'
```
The old .png files do not get changed by that.

## Changing image sizes

A image can be down scaled by a given percentage using the `-resize` argument of convert:
```
convert -resize 20% my-image-name.png my-other-image-name.png
```