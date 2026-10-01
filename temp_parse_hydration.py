import requests, re, json
from bs4 import BeautifulSoup
s=requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
r=s.get("https://www.finn.no/recommerce/forsale/item/471185141")
text=r.text
soup=BeautifulSoup(text, 'html.parser')
for i, script in enumerate(soup.find_all('script')):
    scr=script.string
    if not scr:
        continue
    if 'window.__staticRouterHydrationData' in scr:
        print('script', i, 'len', len(scr))
        m=re.search(r'window\.__staticRouterHydrationData\s*=\s*JSON\.parse\("(.*)"\)\s*;', scr, re.S)
        if not m:
            print('no match')
            break
        payload=m.group(1)
        payload=payload.replace('\\"','\"')
        payload=payload.replace('\\n','\n')
        payload=payload.replace('\\/','/')
        data=json.loads(payload)
        print('root keys', list(data.keys())[:20])
        # search recursively for created
        def search(o, path=''):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k.lower()=='created':
                        print('found created at', path + '.' + k, 'value', v)
                    search(v, path + '.' + k)
            elif isinstance(o, list):
                for idx, v in enumerate(o):
                    search(v, f'{path}[{idx}]')
        search(data)
        break
