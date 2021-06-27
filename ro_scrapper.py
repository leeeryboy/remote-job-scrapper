from bs4 import BeautifulSoup
import requests

def scrap_page(keyword):
  jobs = []
  url = f"https://remoteok.io/remote-dev+{keyword}-jobs"
  html = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
  soup = BeautifulSoup(html.text,"html.parser")
  table = soup.find("table",{"id":"jobsboard"})
  job_items = table.find_all("tr",{"class":"job"})
  for job in job_items:
    link = "https://remoteok.io" + job["data-url"]
    company = job["data-company"]
    title = job.find("h2",{"itemprop":"title"}).string
    job_obj = {"title":title,"company":company,"link":link}
    jobs.append(job_obj)
  return jobs

def ro_get_jobs(keyword):
  return scrap_page(keyword)