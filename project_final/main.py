from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.linkedin import extract_linkedin_jobs
from file import save_to_file

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
  if keyword == None or keyword == "":
    return redirect("/")
  if keyword in db:
    jobs = db[keyword]
  else:
    indeed = extract_indeed_jobs("keyword")
    wwr = extract_wwr_jobs("keyword")
    linkedin = extract_linkedin_jobs("keyword")
    jobs = indeed + wwr + linkedin
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  #user dindt input keyword -> go back to homepage
  if keyword == None or keyword == "":
    return redirect("/")
  #keyword is not in db -> send user serach page with keyword
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)


#server 만듦. user의 request받을 수 있음
app.run("127.0.0.1", debug=True)