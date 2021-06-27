from flask import Flask, render_template, request, send_file
from so_scrapper import so_get_jobs
from wwr_scrapper import wwr_get_jobs
from ro_scrapper import ro_get_jobs
from save import save_file

app = Flask("remote-scrapper")

db = {}

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/results")
def results():
  keyword = request.args.get("keyword")
  keyword = keyword.lower()
  if keyword in db:
    jobs = db[keyword]
  else:
    jobs = so_get_jobs(keyword) + wwr_get_jobs(keyword) + ro_get_jobs(keyword)
    db[keyword] = jobs
  return render_template("results.html",jobs=jobs,keyword=keyword,jobs_len=len(jobs))

@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  save_file(keyword,db[keyword])
  return send_file(f"{keyword}_jobs.csv",mimetype="text/csv",as_attachment=True,attachment_filename=f"{keyword}_jobs.csv")

app.run("127.0.0.1")