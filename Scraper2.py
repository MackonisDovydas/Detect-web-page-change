import netrc
from selenium import webdriver
import time

HOST = 'VU_login'
secrets = netrc.netrc()
USERNAME, account, PASSWORD = secrets.authenticators(HOST)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
driver.get("https://is.vu.lt")

time.sleep(1)
button = driver.find_element_by_xpath("//input[@name='Submit']")
button.click()

time.sleep(1)
button = driver.find_element_by_xpath("//input[@name='src-dnVfbGRhcC1zdHVkZW50YWk=']")
button.click()

username = driver.find_element_by_xpath("//input[@name='username']")
password = driver.find_element_by_xpath("//input[@name='password']")
submit = driver.find_element_by_xpath("//button[@name='wp-submit']")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit.click()

driver.get("https://is.vu.lt/pls/klevas/am$pd_reg_app.show?p_stud_id=219671&p_kalba_name=lt")
page_source = driver.page_source

f = open("html.txt", "w+")
f.write(page_source)
f.close()

driver.close()