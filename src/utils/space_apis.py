import requests

def nasa_image_search(query: str)->dict:

    base_url = f"https://images-api.nasa.gov/search?q={query}"


    try:

        response=requests.get(base_url,timeout=10)

        response.raise_for_status()

        data=response.json()

        items = data.get("collection", {}).get("items", [])

        if not items:
            return {"title": "No results", "summary": "No images found for this query.", "image_url": None}
        
        first = items[0]
        item_data = first.get("data", [{}])[0]
        links = first.get("links",[{}])[0]

        return{
            "title":item_data.get("title","No Title"),
            "summary": item_data.get("description","No description available"),
            "image_url": links.get("href")
        }

    except requests.exceptions.RequestException as e:
        return{
            "title": "Error",
            "summary":"Error",
            "image_url":None
        }