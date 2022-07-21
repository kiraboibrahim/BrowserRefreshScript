#!/usr/bin/python

import time
from selenium import webdriver

url = "https://example.com"
waiting_duration_before_refresh = 5

driver = webdriver.Firefox()
driver.get(url)

assert "Example" in driver.title

time.sleep(waiting_duration_before_refresh)
driver.refresh()

