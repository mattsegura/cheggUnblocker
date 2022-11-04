from re import sub
import webbrowser
import time
from xml.etree.ElementTree import Comment
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import ssl
from PIL import Image

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    """
        # use proxies for the browser instance
        options = uc.options()
        options.add_argument("--headless")

        browser = uc.Chrome(
            options=options
        )
    """
    # connect to the browser instance
    web = uc.Chrome()
    fill = "https://www.chegg.com/homework-help/questions-and-answers/reserve-ratio-refers-ratio-bank-s-multiple-choice-checkable-deposits-total-liabilities-cap-q50410095"
    # use the browser instance 
    web.get("https://homeworkify.net/free-homework-question-answers-unblur-links/")
    
    # find the input field
    input = web.find_element(By.XPATH, '/html/body/div/div/div/div/div/article/div/div[1]/input')
    
    # fill the input field
    input.send_keys(fill)
    
    # find the submit button
    submit = web.find_element(By.XPATH, '/html/body/div/div/div/div/div/article/div/div[1]/button')
    # click the submit button
    submit.click()
    
    # wait for the page to load
    time.sleep(4)
    
    # click the authorization button
    
    print("clicking bot button")
    submit.click()
    time.sleep(4)

    screen = web.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/article/div/div[2]/div/div[3]/div[3]')

    # take screenshot of webpage 
    screen = web.save_screenshot("screenshot.png")

    # crop the image 
    im = Image.open("screenshot.png")
    im = im.crop((0, 0, 860, 835))
    im.save("screenshot.png")

    # close the browser instance
    web.quit()

  