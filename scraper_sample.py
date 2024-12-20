import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
# "https://apps.openedu.ru/learning/course/course-v1:msu+FRSTATEHOOD+fall_2024_stud/block-v1:msu+FRSTATEHOOD+fall_2024_stud+type@sequential+block@649a36ee2f494b879b31525c646ae0d1/block-v1:msu+FRSTATEHOOD+fall_2024_stud+type@vertical+block@b99b634587444b59b7cb18d28f278f16"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
job_cards = results.find_all("div", class_="card-content")
for i in job_cards:
    titel = i.find("h2", class_="title")
    compel = i.find("h3", class_="company")
    locel = i.find("p", class_= "location")
    print(titel.text.strip())
    print(compel.text.strip())
    print(locel.text.strip())
    print()