from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import *
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


def check_upgrades():
    store = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed) b")
    items = {}
    for i in range(0, len(store)):
        item = store[i].text.split(" - ")
        items[i] = {
            "name": item[0],
            "price": item[1],
        }
    return items


time_start = time.time()
time_1 = time_start
while time.time() - time_start < 300:
    cookie.click()
    if (time.time() - time_1) > 5:
        items = check_upgrades()
        last_key = list(items.keys())[-1]
        item_id = f"buy{(items[last_key]['name'])}"
        item = driver.find_element(By.ID, item_id)
        item.click()
        time_1 = time.time()
cps = driver.find_element(By.ID, "cps")
print(f"CPS: {cps.text}")
