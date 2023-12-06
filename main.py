
from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs

keyword = "python" #input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

file = open(f"{keyword}.csv", "w")
file.write("title,company,location,link\n")

for job in jobs:
  file.write(
    f"{job['title']},{job['company']},{job['location']},{job['link']}\n"
    )

file.close()
