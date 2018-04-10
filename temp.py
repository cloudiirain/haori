"""Testing."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

c_opt = Options()
c_opt.add_argument('--headless')

driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=c_opt)

driver.get('http://www.google.com')

print(len(driver.page_source))
