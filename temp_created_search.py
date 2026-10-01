import requests, re
r=requests.get("https://www.finn.no/recommerce/forsale/item/471185141", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
text=r.text
print('status', r.status_code)
for m in re.finditer(r'created', text, re.IGNORECASE):
    idx=m.start()
    print('---')
    print('match:', text[idx:idx+20])
    print(text[max(0, idx-40):idx+80].replace('\n',' '))
