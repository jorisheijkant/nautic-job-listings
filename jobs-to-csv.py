import os 
from bs4 import BeautifulSoup
import csv

jobs_folder = "output/listing"
listings = []
limit = 10000

for (folder, labels, files) in os.walk(jobs_folder):
    for file_index, file in enumerate(files):
        if file_index < limit:
            file_path = f"{jobs_folder}/{file}"
            print(f"Parsing file {file_index}")
            with open(file_path, "r") as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')
                job_container = soup.find("div", {"class": "white-box"})

                job_id = file.split(".")[0]
                job_title = ""
                wage = ""
                vessel_type = ""
                vessel_name = ""
                start_date = ""
                contract_duration = ""
                trading_region = ""
                info_text = ""

                if job_container:
                    job_title_item = job_container.find("h1")
                    if job_title_item:
                        job_title = job_title_item.text 
                    
                    wage_item = job_container.find()

                lists = job_container.find_all("ul", {"class": "single-list"})
                if len(lists) > 0:
                    job_info = lists[0]
                    if job_info:
                        job_info_items = job_info.find_all("li")
                        wage_item = job_info_items[0]
                        if wage_item: 
                            wage_string_item = wage_item.find("strong")
                            if wage_string_item: 
                                wage = wage_string_item.text
                        vessel_type_item = job_info_items[1]
                        if vessel_type_item: 
                            vessel_type_string_item = vessel_type_item.find("strong")
                            if vessel_type_string_item: 
                                vessel_type = vessel_type_string_item.text
                        start_date_item = job_info_items[2]
                        if start_date_item: 
                            start_date_string_item = start_date_item.find("strong")
                            if start_date_string_item: 
                                start_date = start_date_string_item.text
                        contract_length_item = job_info_items[3]
                        if contract_length_item: 
                            contract_length_string_item = contract_length_item.find("strong")
                            if contract_length_string_item: 
                                contract_duration = contract_length_string_item.text
                    
                    vessel_info = lists[1]
                    if vessel_info:
                        vessel_info_items = vessel_info.find_all("li")
                        trading_region_item = vessel_info_items[0]
                        if trading_region_item: 
                            trading_region_string_item = trading_region_item.find("strong")
                            if trading_region_string_item: 
                                trading_region = trading_region_string_item.text
                        if len(vessel_info_items) > 2:
                            vessel_name_item = vessel_info_items[2]
                            if vessel_name_item: 
                                vessel_name_string_item = vessel_name_item.find("strong")
                                if vessel_name_string_item: 
                                    vessel_name = vessel_name_string_item.text

                    ad_text_item = job_container.find("div", {"class": "single-info"})
                    if ad_text_item:
                        info_text = ad_text_item.text
                
                listings.append({
                    "job_id": job_id,
                    "job_title": job_title, 
                    "wage": wage,
                    "vessel_type": vessel_type,
                    "vessel_name": vessel_name,
                    "start_date": start_date,
                    "contract_duration": contract_duration,
                    "trading_region": trading_region,
                    "info_text": info_text
                })

with open("output.csv", "w") as csv_output:
    csv_writer = csv.writer(csv_output)
    csv_writer.writerow(["id", "title", "wage", "vessel_type", "vessel_name", "start_date", "contract_duration", "trading_region", "info_text"])

    for job in listings:
        csv_writer.writerow([job["job_id"], job["job_title"], job["wage"], job["vessel_type"], job["vessel_name"], job["start_date"], job["contract_duration"], job["trading_region"], job["info_text"]])

print(f"All data added to the csv")
            