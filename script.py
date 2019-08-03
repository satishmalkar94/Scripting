import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('http://appstage.sustainonline.com/')
time.sleep(1)
browser.maximize_window()
browser.find_element_by_link_text('Close').click()

uname = browser.find_element_by_name('login')
passw = browser.find_element_by_name('password')
uname.send_keys("gaurav+z11@treeni.com")
passw.clear()
passw.send_keys("Treeni@#1232")

logIn_button = browser.find_element_by_xpath("//button[text()='Log In'][@type='submit']")
logIn_button.click()

#select course
course_form = browser.find_elements_by_class_name('so-course-card-title')[0]
course_form.click()
# select sub course
sub_course = browser.find_elements_by_class_name('so-course-card-small')[4]
sub_course.click()
time.sleep(10)

# for iframe
wait = WebDriverWait(browser, 1000)
frame = wait.until(EC.presence_of_element_located((By.ID, 'jca_course_player')))

browser.switch_to.frame(frame)
browser.switch_to.frame(0)
time.sleep(5)

btn = browser.find_element_by_link_text('START COURSE')
btn.click()
time.sleep(5)

sub_btn = browser.find_element_by_class_name('block-continue--btn')
sub_btn.click()
time.sleep(5)
sub1_btn = browser.find_element_by_class_name('block-continue--btn')
sub1_btn.click()
time.sleep(5)
sub_btn2 = browser.find_element_by_class_name('block-continue--btn')
sub_btn2.click()

scrolls = 6
while True:
    scrolls -= 1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    if scrolls < 0:
        break

time.sleep(5)
exit_btn = browser.find_element_by_class_name('blocks-button__button')
exit_btn.click()

browser.switch_to.default_content()


























