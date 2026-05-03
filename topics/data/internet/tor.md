# Tor

Tools to use the [Tor network](https://en.wikipedia.org/wiki/Tor_(network)) can be installed on Debain with:
```
apt install tor
```
After installation there runs a tor service that listens on port 9050 by default.
Check if the service is running by checking [the listening ports](../../linux/hosting/list-all-listening-ports.md) or by running
```
systemctl status tor
```
## Request resource from the internet
While the tor service is running you can execute.
```
curl --socks5-hostname localhost:9050 https://<url-of-the-resource> -o <file-path-of-the-file-where-to-save-the-resource>
```
Where `<url-of-the-resource>` and `<file-path-of-the-file-where-to-save-the-resource>` need to be replaced.

[Source](https://cybrkyd.com/post/using-curl-with-tor/)

## Check the tor ip

You can check your Tor output IP address by runing
```
curl --socks5-hostname localhost:9050 -s -o - https://ipecho.net/plain | less
```
Compare this with your normal IP address
```
cat | less << EOF
Normal IPv4: $(curl -4 -s -o - https://ipecho.net/plain)
Normal IPv6: $(curl -6 -s -o - https://ipecho.net/plain)
Toŕ IP: $(curl --socks5-hostname localhost:9050 -s -o - https://ipecho.net/plain)
EOF
```

## Resolve domain via the Tor network
While the tor service is running you can run
```
tor-resolve <your-domain>
```
It returns the IP address of the website.

