# Deal with suspicious mails

See also: [Redirect spam mails](redirect-spam-mails.md)

## Find sender IP address

Find the abusive IP-address from the mail

The header of the mail contains multiple `Received: `statements. The lowest one belongs to the original sender (if the ones above can be trusted). All mail servers in the chain of forwarding the mail add their content at the top of the message.

## Report abusive domains and IP-addresses

Write to the abuse email listened at the registrar information that can be receivFed from the [whois service](https://www.whois.com/whois)

Report the domain at [abuseipdb](https://www.abuseipdb.com/) Therefore get the IP-address from a [online whois service](https://dnschecker.org/domain-ip-lookup.php) or the linux command:

### IP lookup non anonymous

`nslookup my.domain.example.de`

The relavant information appears after the `Non-authoritative answer:` line.

The linux whois command can be used to get the name server:
`whois my.domain.example.de`

For more lookup information see [Lookup domains and ip addresses](../../data/internet/lookup-domains-and-ip-addresses.md).

### IP lookup anonymous

[Enable Tor client](../../data/internet/tor.md)
Get the IP address:
```
tor-resolve <your-domain>
```
## Website
If the mail links to a malicious or phishing website you can download the content over [Tor](../../data/internet/tor.md) with:
```
curl --socks5-hostname localhost:9050 -o untrusted-website.txt https://<untrusted-link-url>
```
Replace `<untrusted-link-url>`

==Be careful if you inspect the potentially malicious file.== Even some [text editors have arbitrary code execution exploits when opening files](https://cybersecuritynews.com/vim-modeline-bypass-vulnerability/).
A malware scan for files is available [here](https://yaraify.abuse.ch/scan/) or [here](https://www.virustotal.com/gui/home/upload)

## Check websites online

A suspicious link can be checked [with virustotal](https://www.virustotal.com/gui/home/url) or [sucuri](https://sitecheck.sucuri.net/)
Phishing websites can be checked by [phishtank](https://phishtank.org/)
A screenshot of the webpage can be viewed with [cloudflare](https://radar.cloudflare.com/scan)


