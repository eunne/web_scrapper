from flask import Flask, render_template, request, redirect
from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.linkedin import extract_linkedin_jobs

app = Flask(__name__)

#user가 방문하면 아래 def 함수를 호출함.
@app.route("/") 
#decorator, 아래 def와 꼭 함께 있어야함. 그래야 작동.
#이렇게 def랑 떨어져있으면 작동안함!!
def home():
  return render_template("home.html", name="Eunne")

#make db
db = {}

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword in db:
    jobs = db[keyword]
  else:
    indeed = extract_indeed_jobs("keyword")
    wwr = extract_wwr_jobs("keyword")
    linkedin = extract_linkedin_jobs("keyword")
    jobs = indeed + wwr + linkedin
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)

#server 만듦. user의 request받을 수 있음
app.run("127.0.0.1", debug=True)