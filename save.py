import csv

def save_file(keyword,jobs):
  with open(f"{keyword}_jobs.csv",mode="w",encoding='UTF-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title","Company","Link"])
    for job in jobs:
      writer.writerow(list(job.values()))
  return