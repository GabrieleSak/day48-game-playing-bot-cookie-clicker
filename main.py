from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import *

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
cookie.click()
