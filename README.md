# Nautic job listings

Scrape nautic job listings from Maritime Zone. We use python, `requests` and `Beautifulsoup`.

## Tools and method

The tool uses python. With curl we fetch the raw html of the job listing pages (`fetch-job-pages.py`). Then we fetch all the loose ads, also as raw html (`fetch-individual-jobs.py`). With Beautifulsoup we load the html files and take the listings from the html. Those we put in a csv file (`jobs-to-csv.py`).

## Want to run this?

- Install Python (version 3 and higher) and Pip package manager
- Navigate to this folder using your terminal
- Run `pip install -r requirements.txt` (preferably use an environment manager if you're advanced enough)

You're good to go! Now run the scripts

- Run `python fetch-job-pages.py`
- Run `python fetch-individual-jobs.py`
- Run `python jobs-to-csv.py` (watch the limit parameter)
