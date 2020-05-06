import netrc
import pickle
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

HOST = 'VU_login'
secrets = netrc.netrc()
USERNAME, account, PASSWORD = secrets.authenticators(HOST)

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

"""options.add_argument('--disable-dev-shm-usage') 

Firefox
options = Options()
firefox_profile = FirefoxProfile()
options.headless = True
firefox_profile.set_preference("javascript.enabled", True)
options.profile = firefox_profile
driver = webdriver.Firefox(options=options)
driver.get("https://is.vu.lt")
"""

driver.get("https://is.vu.lt")

time.sleep(2)
button = driver.find_element_by_xpath("//input[@name='Submit']")
button.click()

time.sleep(2)
button = driver.find_element_by_xpath("//input[@name='src-dnVfbGRhcC1zdHVkZW50YWk=']")
button.click()

time.sleep(2)
username = driver.find_element_by_xpath("//input[@name='username']")
password = driver.find_element_by_xpath("//input[@name='password']")
submit = driver.find_element_by_xpath("//button[@name='wp-submit']")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit.click()

time.sleep(2)
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
