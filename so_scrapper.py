from bs4 import BeautifulSoup
import requests

def get_total_page_num(keyword):
  url = f"https://stackoverflow.com/jobs?r=true&q={keyword}"
  html = requests.get(url)
  soup = BeautifulSoup(html.text,"html.parser")
  pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
  return int(pages[-2].get_text().strip())

def scrap_pages(num,keyword):
  jobs = []
  for idx in range(num):
    url = f"https://stackoverflow.com/jobs?r=true&q={keyword}&pg={idx+1}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text,"html.parser")
    listResults = soup.find("div",{"class":"listResults"}).find_all("div",{"class":"-job"})
    for listResult in listResults:
      a_tag = listResult.find("a",{"class":"s-link"})
      link = "https://stackoverflow.com" + a_tag["href"]
      title = a_tag["title"]
      company = " ".join(listResult.find("h3").find("span").get_text().split())
      job_obj = {"title":title,"company":company,"link":link}
      jobs.append(job_obj)
  return jobs

def so_get_jobs(keyword):
  num = get_total_page_num(keyword)
  return scrap_pages(num,keyword)