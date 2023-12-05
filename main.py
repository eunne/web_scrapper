from requests import get
from bs4 import BeautifulSoup
from extractor.wwr import extract_wwr_jobs
from selenium import webdriver



def extract_job(keyword):
  browser = webdriver.Chrome()
  browser.get(f"https://kr.indeed.com/jobs?q={keyword}")

  while():
    True

  #beutifulsoup이 html 페이지를 읽어오는 것임
  results = []
  soup = BeautifulSoup(browser.page_source, "html.parser")

  job_list = (soup.find("ul", class_="css-zu9cdh eu4oa1w0"))
  jobs = job_list.find_all('li', recursive=False)
  # print(len(jobs))
  for job in jobs:

    #mosaic이라는 이상한 li를 제거함
    zone =  job.find("div", class_="mosaic-zone")
    if zone == None:

      anchor = job.select_one("h2 a")
      title = anchor["aria-label"]
      link = anchor["href"]

      position = job.find("span", class_="css-1x7z1ps eu4oa1w0")
      location = job.find("div", class_="css-t4u72d eu4oa1w0")

      job_data = {
        'title' : title,
        'link' : link,
        'position' : position.string.strip(),
        'location' : location.string.strip()
      }

      results.append(job_data)

  return results

print(extract_job('react'))