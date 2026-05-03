# HTTP requests in Python

HTTP and HTTPS request in Python can be done with the requests library:
```
apt install python3-requests
```

## Get request
With python execute:
```python3
import requests
response = requests.get(
    "https://en.wikipedia.org/w/rest.php/v1/search/page?q=jupiter&limit=2", 
    headers= {"User-Agent":"python3-requests"})
print(f"Status code: {response.status_code}\n\nResponse Headers:\n{response.headers}\n\nResponse body:\n{response.content}")
```
## Post request
With python execute:
```python3
response = requests.post(
    "https://en.wikipedia.org/w/rest.php/v1/transform/html/to/wikitext/Jupiter", 
    headers={"User-Agent":"python3-requests","Content-Type":"application/json"}, 
    data=b'{ "html": "<h2> hello World </h2>" }')
print(f"Status code: {response.status_code}\n\nResponse Headers:\n{response.headers}\n\nResponse body:\n{response.content}")
```
This is equivalent to
```python3
response = requests.post(
    "https://en.wikipedia.org/w/rest.php/v1/transform/html/to/wikitext/Jupiter", 
    headers={"User-Agent":"python3-requests"}, 
    json={"html": "<h2> hello World </h2>" })
print(f"Status code: {response.status_code}\n\nResponse Headers:\n{response.headers}\n\nResponse body:\n{response.content}")
```