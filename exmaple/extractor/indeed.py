from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

#여러 페이지에 접근하기 위한 페이지 숫자 추출하는 함수
def get_page_count(keyword):
  browser = webdriver.Chrome()
  browser.get(f"https://kr.indeed.com/jobs?q={keyword}")

  while():
    True

  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("ul", class_="css-1g90gv6 eu4oa1w0")
  pages = pagination.find_all("li", recursive=False)
  count = len(pages)
  if count == 0:
    return 1
  else:
    return count-1


def extract_indeed_jobs(keyword):
  #페이지 수를 가져오고, 해당 페이지 수만큼 아래 스크랩핑을 반복하도록 명령
  pages = get_page_count(keyword)
  #print("found", pages, "pages")
  results = []
  for page in range(pages):
    browser = webdriver.Chrome()
    final_url = browser.get(f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}")
    #print("Requesting", browser)

    #beutifulsoup이 html 페이지를 읽어오는 것임
    soup = BeautifulSoup(browser.page_source, "html.parser")

    job_list = (soup.find("ul", class_="css-zu9cdh eu4oa1w0"))
    jobs = job_list.find_all('li', recursive=False)
    for job in jobs:

      #mosaic이라는 이상한 li를 제거함
      zone =  job.find("div", class_="mosaic-zone")
      if zone == None:

        anchor = job.select_one("h2 a")
        position = anchor["aria-label"]
        link = anchor["href"]

        company = job.find("span", class_="css-1x7z1ps eu4oa1w0")
        location = job.find("div", class_="css-t4u72d eu4oa1w0")

        job_data = {
          'position' : position.replace(",",""),
          'company' : company.string.strip().replace(",",""),
          'location' : location.string.strip().replace(",",""),
          'link' : f"https://kr.indeed.com/{link}"
        }

        results.append(job_data)

  return results