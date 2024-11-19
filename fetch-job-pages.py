import requests 
import time 
import os

base_url = "https://maritime-zone.com/en/vacancy?page="
amount_of_pages = 148

for page_index in range(amount_of_pages):
    page_url = f"{base_url}{page_index + 2}"
    print(f"Now scraping page {page_index + 2}: {page_url}")

    response = requests.get(page_url)
    response.raise_for_status()
    bestand_map = f"output/listings"
    bestand_naam = f"output/listings/{page_index}.html"
    os.makedirs(bestand_map, exist_ok=True)

    with open(bestand_naam, "w", encoding="utf-8") as f:
        f.write(response.text)

    time.sleep(2)
