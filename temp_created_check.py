import requests, re
r=requests.get("https://www.finn.no/recommerce/forsale/item/471185141", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
text=r.text
print("status", r.status_code)
print("has created", '"created"' in text)
print("count", text.count('"created"'))
idx=text.find('"created"')
print("idx", idx)
if idx != -1:
    print(text[max(0, idx-100):idx+150].replace("\n", " "))
