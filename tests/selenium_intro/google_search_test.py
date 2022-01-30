from selenium import webdriver
from itnation_selenium_test import opensearch, search_link, browser_close
driver = webdriver.Chrome()

opensearch()
search_link()
browser_close()