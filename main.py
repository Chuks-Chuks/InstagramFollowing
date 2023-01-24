from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException

import os
import dotenv


def click(action):
    sleep(5)
    action.click()


path = os.path.expanduser('../InstagramFollowing')
dotenv.load_dotenv(os.path.join(path, '..env'))

driver_location = "c:/Development/chromedriver.exe"
ser = Service(driver_location)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=ser, options=chrome_options)
url = "https://www.instagram.com"
browser.get(url)
browser.maximize_window()

sleep(3)
# To click allow essential cookies
allow_click = browser.find_elements(By.CSS_SELECTOR, '._a9--')
click(allow_click[0])


sleep(5)
# To input phone number and password
input_number = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main'
                                              '/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
click(input_number)
sleep(0.5)
input_number.send_keys(os.getenv('IG_NUMBER'))
password_input = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section'
                                                '/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
sleep(0.5)
password_input.send_keys(os.getenv('IG_PASSWORD') + Keys.ENTER)

sleep(5)
not_now = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]'
                                         '/div[2]/section/main/div/div/div/div/button')
click(not_now)

sleep(5)
not_now2 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div'
                                          '/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
click(not_now2)

search = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div'
                                        '/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div')
click(search)

sleep(5)
search_input = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]'
                                              '/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
search_input.send_keys('Python')

sleep(3)
first_result = browser.find_element(By. XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]'
                                               '/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]'
                                               '/div/a/div/div[2]/div[2]/div')
click(first_result)

sleep(3)
followers_tab = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]'
                                               '/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
click(followers_tab)

sleep(5)
#
scrollable_popup = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]'
                                                  '/div/div/div/div/div[2]/div/div/div[2]')

for i in range(100):
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
    sleep(2)

# followers_list = browser.find_elements(By.CSS_SELECTOR, '._aade div')
follow_button = browser.find_elements(By.CSS_SELECTOR, '._aj1- div div')
print(len(follow_button))

button_add = 0
try:
    for _ in range(0, len(follow_button)):
        button_add += 1
        button = f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div' \
                 f'/div[2]/div[1]/div/div[{button_add}]/div[3]/button/div/div'
        follow_click = browser.find_element(By.XPATH, button)
        click(follow_click)
except NoSuchElementException:
    ok_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[2]'
                                               '/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
    click(ok_button)
except ElementClickInterceptedException:
    cancel_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div'
                                                   '/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
                                                   '/button[2]')
    click(cancel_button)


