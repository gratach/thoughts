# Making HTTP requests from the console

A HTTP request can be made by using `curl`:
```
curl https://my-url.example.com
```
It can be saved in a file with:
```
curl https://my-url.example.com > my-file.html
```
Headers can be added to the request with the `-H` flag.
For example a truncated version starting from byte 123 and ending on byte 456 can be received by running:
```
curl -H "Range: bytes=123-456" https://my-url.example.com
```