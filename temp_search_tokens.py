import requests, re
r=requests.get("https://www.finn.no/recommerce/forsale/item/471185141", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
text=r.text
for token in ["application/ld+json", "window.", "__INITIAL", "itemdata", "itemData", "created", "createdAt", "publish", "published", "hasbeenpublished", "meta", "adData", "adData", "data: {", "data: {\n", "data: {\r", "data":"]:"] ]:"]:"] ]"]:"] "]"]:", "data-", "json"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]"]:"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]"]:"]
