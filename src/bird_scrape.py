from duckduckgo_search import DDGS
import os
import urllib.request

def download_images(query, folder, max_results=20):
    os.makedirs(folder, exist_ok=True)
    
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=max_results)
        for i, result in enumerate(results):
            try:
                url = result['image']
                urllib.request.urlretrieve(url, f"{folder}/{i}.jpg")
                print(f"Downloaded: {url}")
            except Exception as e:
                print(f"Failed: {e}")

# List of common Swedish bird species (you can expand this)
species = ['blåmes', 'talgoxe', 'koltrast', 'gråsparv']

# Download images into folders
for bird in species:
    download_images(f"{bird} fågel", f"data/bird-data/{bird}")
 