import requests
r=requests.get("https://www.finn.no/recommerce/forsale/search/api/search/SEARCH_ID_BAP_COMMON", params={"q":"471185141","rows":5}, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
print(r.status_code)
print(r.headers.get('content-type'))
try:
    data=r.json()
    docs=data.get('docs', [])
    print('count', len(docs))
    for doc in docs:
        print(doc.get('id'), doc.get('timestamp'))
except Exception as e:
    print('json error', e)
