import os 
from bs4 import BeautifulSoup
import requests
import time

listing_folder = "output/listings"
links_to_listings = []

for (folder, labels, files) in os.walk(listing_folder):
    for file in files:
        file_path = f"{listing_folder}/{file}"
        with open(file_path, "r") as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')

            job_list = soup.find("div", {"class": "list-view"})

            if job_list:
                jobs = job_list.find_all("div", {"class": "item"})
                print(f"{len(jobs)} jobs found")

                for job in jobs:
                    job_id = job.get("data-key")
                    job_link_item = job.find("a", {"class": "card-title"})
                    job_link = job_link_item.get("href")
                    job_link = f"https://maritime-zone.com{job_link}"
                    print(f"{job_id}, {job_link_item}, {job_link}")

                    response = requests.get(job_link)
                    response.raise_for_status()
                    bestand_map = f"output/listing"
                    bestand_naam = f"output/listing/{job_id}.html"
                    os.makedirs(bestand_map, exist_ok=True)

                    with open(bestand_naam, "w", encoding="utf-8") as f:
                        f.write(response.text)

                    time.sleep(0.5)