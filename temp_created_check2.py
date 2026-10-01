import requests, re
from bs4 import BeautifulSoup
s=requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
r=s.get("https://www.finn.no/recommerce/forsale/item/471185141")
text=r.text
print('status', r.status_code)
print('total created count', text.lower().count('created'))
for i, script in enumerate(BeautifulSoup(text, 'html.parser').find_all('script')):
    scr=script.string
    if scr and 'created' in scr.lower():
        print('script', i, 'len', len(scr))
        for m in re.finditer(r'created', scr, re.IGNORECASE):
            idx=m.start()
            print('  pos', idx, scr[max(0, idx-50):idx+90].replace('\n',' '))
        break
