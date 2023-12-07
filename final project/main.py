from extract.linkedin import extract_linkedin_jobs

keyword = ""

linkedin = extract_linkedin_jobs(keyword)

print(linkedin)


file = open(f"{keyword}2.csv", "w")
file.write("title, company, location, link\n")

for job in linkedin:
  file.write(f"{job['title']},{job['company']},{job['location']},{job['link']}\n")

file.close()