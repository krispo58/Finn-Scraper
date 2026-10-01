import requests
from bs4 import BeautifulSoup
s=requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
r=s.get("https://www.finn.no/recommerce/forsale/item/471185141")
text=r.text
soup=BeautifulSoup(text, 'html.parser')
for i, script in enumerate(soup.find_all('script')):
    scr=script.string
    if scr and 'window.__staticRouterHydrationData' in scr:
        print('script index', i)
        start=scr.find('window.__staticRouterHydrationData')
        print(scr[start:start+260].replace('\n',' '))
        jstart=scr.find('JSON.parse("', start)
        print('json start', jstart)
        jend=scr.find('")', jstart)
        print('json end', jend)
        print('json excerpt', scr[jstart:jstart+120].replace('\n',' '))
        break
