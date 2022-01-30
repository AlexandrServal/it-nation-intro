from selenium import webdriver

driver = webdriver.Chrome()


def opensearch():
    driver.get('https://www.google.com')
    driver.maximize_window()


def search_link():
    driver.find_element_by_css_selector('[class="gLFyf gsfi"]').send_keys('maven selenium java')
    driver.find_element_by_css_selector('[class="gNO89b"]').click() #css selector
# driver.find_element_by_css_selector('[class="RNmpXc"]').click()
#driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
    driver.find_element_by_css_selector('[class="LC20lb MBeuO DKV0Md"]').click()

def browser_close():
    driver.close()

opensearch()
search_link()
browser_close()
# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]
# <input class="gNO89b"
# <input class="RNmpXc"
# <h3 class="LC20lb MBeuO DKV0Md"
# <input class="gNO89b"
# './/img[@a1t-'Google']
# <input class="gLFyf gsfi"
# ('.//input[@type-"text"]')
