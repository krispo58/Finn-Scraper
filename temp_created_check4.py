import requests
from bs4 import BeautifulSoup
s=requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
r=s.get("https://www.finn.no/recommerce/forsale/item/471185141")
text=r.text
print('status', r.status_code)
idx=text.lower().find('created')
print('idx', idx)
print('count', text.lower().count('created'))
if idx != -1:
    print(text[max(0, idx-120):idx+180].replace('\n', ' '))

from bs4 import BeautifulSoup
soup=BeautifulSoup(text, 'html.parser')
for i, script in enumerate(soup.find_all('script')):
    scr=script.string
    if scr and 'created' in scr.lower():
        print('\nscript', i, 'len', len(scr))
        idx2=scr.lower().find('created')
        print('script idx', idx2)
        print(scr[max(0, idx2-120):idx2+180].replace('\n', ' '))
        break
