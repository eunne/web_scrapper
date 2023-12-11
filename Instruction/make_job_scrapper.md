### 1. [Library: requests] request and response 요청하고 응답받기

```python
import requests

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

print(response.content)
```


![request에 응답하여 url의 태그들을 보여주고 있다.](https://prod-files-secure.s3.us-west-2.amazonaws.com/bdc6e658-fa48-4622-9152-0070b47ff401/01dc3012-2807-4775-bd61-7b335bc3cd75/Untitled.png)

request에 응답하여 url의 태그들을 보여주고 있다.

- request : 브라우저에서 서버로 내용을 요청하는 것을 request라고 한다.
- response : 그러면 서버에서는 url 주소를 확인하여 응답메세지를 전송한다.
    
    위 화면에서 보면 request(요청)한 url에 담긴 정보를 response(응답)하여 보여주고 있다.
    
- python에서는 request를 손쉽게 할 수 있는 패키지가 있으므로 사용하면 된다.




### 2. [Library: bs4] BeautifulSoup를 이용해 html 정보 가져오기

- BS4가 html 구조를 파악해서html 요소들을 통해 원하는 정보에 접근 가능하도록 해준다.
- BS의 문법은 [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)에서 확인 가능

```python
from bs4 import Beautiful

soup = BeautifulSoup(response.content, "html.parser" )
```

- input ‘what kind of data give to bs’




## 3-1. one page (wwr)

- pagination도 없고, 그냥 한 페이지 안에서 모든 정보가 출력되는 경우




## 3-2. more than one page

- 한 페이지 이상 pagination이 있는 경우




## 3-3. 동적으로 움직이는 페이지인 경우
