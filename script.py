import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://appstage.sustainonline.com/')
time.sleep(5)
browser.find_element_by_link_text('Close').click()
uname = browser.find_element_by_name('login')
passw = browser.find_element_by_name('password')
uname.send_keys("gaurav+z11@treeni.com")
time.sleep(5)
passw.clear()
time.sleep(5)
passw.send_keys("Treeni@#1232")
logIn_button = browser.find_element_by_xpath("//button[text()='Log In'][@type='submit']")
logIn_button.click()
