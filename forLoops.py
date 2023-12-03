from requests import get
from bs4 import BeautifulSoup
'''
websites = (
    "google.com",
    "https://facebook.com",
    "apple.com",
    "https://tiktok.com",
    "microsoft.com"
  )

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "working"
  else:
    results[website] = "not working"

print(results)
'''

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python" #input("input a job to seartch:")

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("can't response website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  #section -> class=jobs 정보를 모두 가져옴
  job_sections = soup.find_all('section', class_="jobs")
  
  results = []

  #[red] job_section 중에서 li인 항목만 가져옴/ 3개
  for job_section in job_sections:
    job_posts = job_section.find_all('li')

    #job_post중에서 필요없는 정보제거(view_all) / 마지막 1개
    job_posts.pop(-1)
    for job_post in job_posts:

      #[yellow] anchor를 찾는다. 2개
      anchors = job_post.find_all('a')
      anchor = anchors[1]
      company, kind, region = anchor.find_all('span', class_='company')

      link = anchor['href']
      title = anchor.find('span', class_='title')

      #job data를 dic형식으로 만들기
      job_data = {
        'company': company.string,
        'title': title.string,
        'kind': kind.string,
        'region': region.string
      }

      #job data가 forloop를 돌면서 없어지니까 반복문 밖의 list에 저장시키기
      results.append(job_data)

  for result in results:
    print(result)
    print("///////////")    