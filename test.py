import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

course_form = browser.find_elements_by_class_name('so-course-card-title')[0]
course_form.click()

sub_course = browser.find_elements_by_class_name('so-course-card-small')[2]
sub_course.click()


browser.execute_script("window.scrollTo(0, 10)")

btn = browser.find_element_by_class_name('block-continue__content')
btn.click()

# btn = browser.find_element_by_xpath("//div[text()='CONTINUE']")
# btn.click()





