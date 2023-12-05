from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

results = []

def extract_jobs(term):
  browser = webdriver.Chrome()
  browser.get(f"https://remoteok.com/remote-{term}-jobs")

  while():
    True


  #beutifulsoup이 html 페이지를 읽어오는 것임
  soup = BeautifulSoup(browser.page_source, "html.parser")

  #job_list가 들어가있는 태그를 찾아서(find) 그 안에 있는 모든 리스트를 찾는다.(find_all)
  job_list = (soup.find("tbody"))
  job_posts = job_list.find_all("td", class_="company position company_and_position") #recursive=False 재귀함수/본인이 내장하고 있는 정보까지 찾지 않는다.

  #맨 첫번째 있는 데이터는 필요 없으므로 삭제한다.
  job_posts.pop(0)

  for job_post in job_posts:
    job_len = job_post.find_all('div', class_ = "location")
    if len(job_len) != 2:
      pass #company만 있거나 Salary만 있는 예외항목은 pass함
    else:
      location, salary = job_post.find_all('div', class_ = "location")

    title = job_post.find('h2', itemprop = "title")
    company = job_post.find('h3', itemprop = "name")
    link = job_post.find('a')['href'] #bs4가 dic형태로 값을 가져오므로 key값(href)을 적으면 value값이 조회됨.

    job_data = {
      'title' : title.string,
      'company' : company.string,
      'location' : location.string,
      'salary' : salary.string,
      'link' : f"https://remoteok.com/{link}"
    }
    
    results.append(job_data)
  return results

print(extract_jobs('python'))
