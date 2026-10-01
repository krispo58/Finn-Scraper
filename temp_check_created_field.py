import requests
r=requests.get("https://www.finn.no/recommerce/forsale/search/api/search/SEARCH_ID_BAP_COMMON", params={"q":"macbook air m2","rows":5}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
data=r.json()
docs=data.get("docs", [])
print("status", r.status_code)
print("count", len(docs))
print("created_present", any("created" in doc for doc in docs))
print("keys_sample", sorted(set().union(*(doc.keys() for doc in docs[:3]))))
