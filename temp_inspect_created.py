import requests, re
from bs4 import BeautifulSoup
s=requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
r=s.get("https://www.finn.no/recommerce/forsale/item/471185141")
text=r.text
print('status', r.status_code)
print('created count raw', text.lower().count('created'))
for pat in [r'"created"\s*:\s*\d+', r'created\s*:\s*\d+', r'"meta"\s*:\s*\{']:
    print('pattern', pat, 'count', len(re.findall(pat, text, re.IGNORECASE)))
for m in re.finditer(r'"meta"\s*:\s*\{', text, re.IGNORECASE):
    idx=m.start()
    print('meta idx', idx)
    print(text[max(0, idx-120):idx+600].replace('\n',' '))
    break
soup=BeautifulSoup(text, 'html.parser')
for i, script in enumerate(soup.find_all('script')):
    scr=script.string
    if not scr:
        continue
    lower=scr.lower()
    if 'meta' in lower or 'created' in lower or 'itemdata' in lower:
        print('\n--- script', i, 'len', len(scr), '---')
        print(scr[:1200].replace('\n',' '))
        break
