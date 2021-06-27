from bs4 import BeautifulSoup
import requests

def scrap_page(keyword):
  jobs = []
  url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
  html = requests.get(url)
  soup = BeautifulSoup(html.text,"html.parser")
  sections = soup.find("div",{"class":"jobs-container"}).find_all("section",{"class":"jobs"})
  for section in sections:
    lis = section.find_all("li")
    for li in lis[:-1]:
      a_tag = li.find_all("a")[1]
      link = "https://weworkremotely.com" + a_tag["href"]
      title = a_tag.find("span",{"class":"title"}).string
      company = a_tag.find("span",{"class":"company"}).string
      job_obj = {"title":title,"company":company,"link":link}
      jobs.append(job_obj)
  return jobs

def wwr_get_jobs(keyword):
  return scrap_page(keyword)