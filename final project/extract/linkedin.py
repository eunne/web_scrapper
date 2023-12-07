from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver


def extract_linkedin_jobs(keyword):
  browser = webdriver.Chrome()
  browser.get(f"https://www.linkedin.com/jobs/search?keywords={keyword}")

  while():
    True

  soup = BeautifulSoup(browser.page_source, "html.parser")
  job_container = soup.find("ul", class_="jobs-search__results-list")
  job_lists = job_container.find_all("li", recursive=False)
  
  results = []
  for job_list in job_lists:
    title = job_list.find("h3")
    link = job_list.select_one("h4 a")["href"]
    company = job_list.find("a", class_="hidden-nested-link")
    location = job_list.find("span", class_="job-search-card__location")

    jobs = {
      "title" : title.string.strip().replace(","," "),
      "company" : company.string.strip().replace(","," "),
      "location" : location.string.strip().replace(","," "),
      "link" : link
    }
    
    results.append(jobs)
  return results