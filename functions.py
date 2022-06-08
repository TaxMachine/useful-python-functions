# proxy rotator
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
# example
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
    break
# User Agent rotator
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

# example
import requests
while True:
    r = requests.get("https://api.someurl.com", headers={"User-Agent": agent()})
    print(r.text)
    break

# Colors
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

# example
print(f"{bcolors.OKGREEN}This is green")
print(f"{bcolors.OKBLUE}This is blue")
print(f"{bcolors.OKCYAN}This is cyan")
print(f"{bcolors.WARNING}This is yellow")
# and it goes on for the others...

# Download Files
import requests
def download(url, path):
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
    except Exception:
        pass

# example
download("https://avatars.githubusercontent.com/u/78520042?s=96&v=4", "./waifuwareontop.png")