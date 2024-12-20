from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# something related to waiting for element to be loaded
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


opts = Options()
opts.add_argument("--headless=new")

browser = Chrome(options=opts)
URL = "https://apps.openedu.ru/learning/course/course-v1:msu+FRSTATEHOOD+fall_2024_stud/block-v1:msu+FRSTATEHOOD+fall_2024_stud+type@sequential+block@75c53791d3d44c7d9a7b4aff4459448e/block-v1:msu+FRSTATEHOOD+fall_2024_stud+type@vertical+block@e0c560ef5781455d89aa7be622ffcfa7"
browser.get(URL)
# browser.timeouts.explict_wait = 10

element = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'form-input')))

# auth
inps = browser.find_elements(By.CLASS_NAME, "form-input")
inps[0].send_keys("login")
inps[1].send_keys("password")
browser.find_element(By.CLASS_NAME, "btn-submit").click()

# playing with page

# soup = BeautifulSoup(browser.page_source, 'html.parser')
element = WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.ID, 'unit-iframe')))

iframe = browser.find_element(By.ID, "unit-iframe")
browser.get(iframe.get_attribute("src"))

problems = browser.find_elements(By.CLASS_NAME, "wrapper-problem-response")
for prob in problems:
    # undestading the type of the question
    # choose group
    box = prob.find_elements(By.CLASS_NAME, "choicegroup")
    if len(box):
        box = box[0]
        legend = box.find_element(By.TAG_NAME, "legend").text
        cor_answ = box.find_element(By.CLASS_NAME, "choicegroup_correct").text
        print(f"{legend} <{cor_answ}>")
        continue
    
    # checking other types
    box = prob.find_elements(By.CLASS_NAME, "textline")
    if len(box):
        box = box[0]
        legend = box.find_element(By.CLASS_NAME, "problem-group-label").text
        cor_answ = box.find_element(By.TAG_NAME, "input").get_attribute("value")
        print(f"{legend} <{cor_answ}>")
        continue

    box = prob.find_elements(By.CLASS_NAME, "inputtype")
    if len(box):
        box = box[0]
        legend = box.find_element(By.CLASS_NAME, "problem-group-label").text
        cor_answ = box.find_element(By.TAG_NAME, "input").get_attribute("value")
        print(f"{legend} <{cor_answ}>")
        continue

    print("UNKNOWN TYPE")
    break

# print(soup.contents)
browser.close()

