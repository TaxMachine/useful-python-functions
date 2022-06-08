# useful-python-functions
useful python functions to make life easier

## Proxy rotator
Very cool to use this when you make tons of requests and don't want to use your own IP Address to bypass rate limits, ip grabbing, etc
You can get proxy lists on this website(there's planty of other websites like that but this is the one i use): https://proxyscrape.com/free-proxy-list
**Function**
```python
def proxies(ptype):
    match ptype:
        case "socks4":
            with open('./socks4_proxies.txt') as f:
                d = ''.join(random.choice(f.read().split('\n')))
                return {"http": f"socks4://{d}", "https": f"socks4://{d}"}
        case "http":
            with open('./http_proxies.txt') as f:
                e = ''.join(random.choice(f.read().split('\n')))
                return {"http": e, "https": e}
        case "socks5":
            with open('./socks5_proxies.txt') as f:
                d = ''.join(random.choice(f.read().split('\n')))
                return {"http": f"socks5://{d}", "https": f"socks5://{d}"}
```
**Uses**
```python
import requests

formdata = {
    "field1": "something",
    "field2": "something else"
}

while True:
  try:
    r = requests.post('https://someurls.com', data=formdata, proxies=proxies("http"))
    print(r.text)
  except Exception:
    pass
```

## User-Agent rotator
Could be useful if you want to randomize large amount of requests
List of user agent is on the repo
```python
#local file
def agent():
    with open('./useragents.txt') as f:
        e = f.read().split('\n')
        d = random.choice(e)
        return ''.join(d)
#from this repo
import requests
def agent():
    r = requests.get("https://")
    e = r.split('\n')
    return ''.join(random.choice(e))
```
**Uses**
```python
import requests
while True:
    r = requests.get("https://api.someurl.com", headers={"User-Agent": agent()})
    print(r.text)
```
