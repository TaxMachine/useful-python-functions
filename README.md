# useful python functions
useful python functions to make life easier

## Proxy rotator
Very cool to use this when you make tons of requests and don't want to use your own IP Address to bypass rate limits, ip grabbing, etc
You can get proxy lists on this website(there's planty of other websites like that but this is the one i use): https://proxyscrape.com/free-proxy-list

### Function
```python
import random
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
### Uses
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

### Function
```python
#local file
import random
def agent():
    with open('./useragents.txt') as f:
        e = f.read().split('\n')
        d = random.choice(e)
        return ''.join(d)
   
   
#from this repo
import random,requests
def agent():
    agt = []
    r = requests.get("https://raw.githubusercontent.com/TaxMachine/useful-python-functions/main/useragents.txt")
    e = r.text.split('\n')
    for t in e:
        agt.append(t)
    return ''.join(random.choice(agt))
```

### Uses
```python
import requests
while True:
    r = requests.get("https://api.someurl.com", headers={"User-Agent": agent()})
    print(r.text)
```

## Colors
Make your console outputs cool and colorful

### Functions
```python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
```

### Uses
```python
print(f"{bcolors.OKGREEN}This is green")
print(f"{bcolors.OKBLUE}This is blue")
print(f"{bcolors.OKCYAN}This is cyan")
print(f"{bcolors.WARNING}This is yellow")
# and it goes on for the others...
```

# Crediting
if you want to use my code feel free no need to credit me, just don't be a pussy and if someone asked you just say you found it on github

# Donation
ETH -> `0xF583244C94298605f1e6104ABEC573a3b14b9a17`
