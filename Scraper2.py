import netrc
import pickle
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

HOST = 'VU_login'
secrets = netrc.netrc()
USERNAME, account, PASSWORD = secrets.authenticators(HOST)

options = Options()
firefox_profile = FirefoxProfile()
options.headless = True
firefox_profile.set_preference("javascript.enabled", True)
options.profile = firefox_profile
driver = webdriver.Firefox(options=options)
driver.get("https://is.vu.lt")

time.sleep(1)
button = driver.find_element_by_xpath("//input[@name='Submit']")
button.click()

button = driver.find_element_by_xpath("//input[@name='src-dnVfbGRhcC1zdHVkZW50YWk=']")
button.click()

time.sleep(1)
username = driver.find_element_by_xpath("//input[@name='username']")
password = driver.find_element_by_xpath("//input[@name='password']")
submit = driver.find_element_by_xpath("//button[@name='wp-submit']")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit.click()

time.sleep(1)
driver.get("https://is.vu.lt/pls/klevas/am$pd_reg_app.show?p_stud_id=219671&p_kalba_name=lt")
page_source = driver.page_source
url = driver.current_url

f = open("html.txt", "w+")
f.write(page_source)
f.close()
f = open("URL.txt", "w+")
f.write (url)
f.close()

driver.close()
