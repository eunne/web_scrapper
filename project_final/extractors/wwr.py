from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  #search_term = "python" #input("input a job to seartch:") 함수로 만들면 keyword를 아래 response에 바로 넣으면 되므로 input함수 필요 없음

  response = get(f"{base_url}{keyword}")

  if response.status_code != 200:
    print("can't response website")
  else:
    
    results = []
    soup = BeautifulSoup(response.text, "html.parser")

    #section -> class=jobs 정보를 모두 가져옴
    job_sections = soup.find_all('section', class_="jobs")
    
    #[red] job_section 중에서 li인 항목만 가져옴/ 3개
    for job_section in job_sections:
      job_posts = job_section.find_all('li')

      #job_post중에서 필요없는 정보제거(view_all) / 마지막 1개
      job_posts.pop(-1)
      for job_post in job_posts:

        #[yellow] anchor를 찾는다. 2개
        anchors = job_post.find_all('a')
        anchor = anchors[1]
        company, kind, location = anchor.find_all('span', class_='company')

        link = anchor['href']
        position = anchor.find('span', class_='position')

        #job data를 dic형식으로 만들기
        job_data = {
          'position': position.string.replace(","," "),
          'company': company.string.replace(","," "),
          'location': location.string.replace(","," "),
          'link' : f"https://weworkremotely.com/{link}"
        }

        #job data가 forloop를 돌면서 없어지니까 반복문 밖의 list에 저장시키기
        results.append(job_data)

    return results  