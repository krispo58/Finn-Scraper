import requests
import bs4
from datetime import datetime, timezone

class FinnAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )
        self.base_url = "https://www.finn.no/recommerce/forsale/search/api/search/SEARCH_ID_BAP_COMMON"
    
    def search(
        self,
        query,
        rows=100,
        published_today=False,
        page=1,
        sort=None,
        fiks_ferdig=False,
        min_price=None,
        max_price=None,
    ):
        params = {
            "q": query,
            "rows": rows,
            "page": page,
            "published": 1 if published_today else None,
            "sort": sort,
            "shipping_types": 0 if fiks_ferdig else None,
            "price_from": min_price,
            "price_to": max_price,
        }
        response = self.session.get(self.base_url, params=params)
        response.raise_for_status()
        return self._clean_search_results(response.json())

    def _clean_search_results(self, results):
        cleaned_results = []
        for result in results.get("docs", []):
            labels = result.get("labels") or []
            cleaned_result = {
                "heading": result.get("heading"),
                "price": result.get("price").get("amount"),
                "id": result.get("id"),
                "timestamp": result.get("timestamp"),
                "fiks_ferdig": any(label.get("id") == "fiks_ferdig" for label in labels),
            }
            cleaned_results.append(cleaned_result)
        return cleaned_results
    
    def get_url(self, id):
        return f"https://www.finn.no/recommerce/forsale/item/{id}"

    def _get_listing_metadata(self, id):
        results = self.search(query=id, rows=1)
        if results and results[0].get("id") == id:
            return results[0]
        return {}

    def _get_listing_timestamp(self, id):
        return self._get_listing_metadata(id).get("timestamp")

    def _get_single_info(self, id):
        url = self.get_url(id)
        response = self.session.get(url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        description_element = soup.find(attrs={"data-testid": "description"})
        description = None
        if description_element:
            n_soup = bs4.BeautifulSoup(description_element.decode_contents(), "html.parser")
            description = n_soup.get_text(strip=True).removesuffix(
                "Pluss tegnVis hele beskrivelsenNB: Knappen for å vise hele beskrivelsen har kun en visuell effekt."
            )

        location_element = soup.find(attrs={"data-testid": "object-address"})
        location = location_element.get_text(strip=True) if location_element else None

        metadata = self._get_listing_metadata(id)
        timestamp = metadata.get("timestamp")
        date = None
        if timestamp is not None:
            date = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).isoformat()

        return {
            "description": description,
            "location": location,
            "date": date,
            "fiks_ferdig": metadata.get("fiks_ferdig", False),
        }
    
    def get_info(self, id: list | str):
        if isinstance(id, list):
            # Return a list of dicts for consistency and better downstream handling
            return [
                {"id": single_id, **self._get_single_info(single_id)}
                for single_id in id
            ]

        # For a single id, return a dict with id, description and location
        return {"id": id, **self._get_single_info(id)}

if __name__ == "__main__":
    api = FinnAPI()
    results = api.search("macbook air m2", rows=100, published_today=False)
    results = api.search("macbook air m1", rows=100, published_today=False)
    results = api.search("macbook pro m2", rows=100, published_today=False)
    results = api.search("Iphone 16", rows=100, published_today=False)
    results = api.search("Iphone 15", rows=100, published_today=False)
    print(print(len(str(results)) + len(str(api.get_info([result["id"] for result in results])))))
        
