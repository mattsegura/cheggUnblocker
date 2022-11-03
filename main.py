from re import sub
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

web = webdriver.Chrome()

fill = "https://www.chegg.com/homework-help/questions-and-answers/reserve-ratio-refers-ratio-bank-s-multiple-choice-checkable-deposits-total-liabilities-cap-q50410095"
# use the browser instance 
web.get("https://homeworkify.net/free-homework-question-answers-unblur-links/")

input = web.find_element(By.XPATH, '/html/body/div/div/div/div/div/article/div/div[1]/input')

input.send_keys(fill)

# click the submit button 
submit = web.find_element(By.XPATH, '/html/body/div/div/div/div/div/article/div/div[1]/button')
submit.click()

# wait for the page to load
time.sleep(4)

# click the authorization button

submit = web.find_element(By.XPATH, '/html/body/div/div/div/div/div/article/div/div[2]/div/div[2]/div[1]/div')
print("clicking bot button")
submit.click()
time.sleep(4)
