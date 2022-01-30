from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

#Arrenge
def open_Search():
    browser.config.hold_browser_open = True
    browser.open("https://www.google.com/")
    browser.driver.maximize_window()

#Action
def search_link():
    s('[name=q]').type('selenide').press_enter()
    s('[class="LC20lb MBeuO DKV0Md"]').click()


def browser_close():
    browser.close()

# <h3 class="LC20lb MBeuO DKV0Md">Selenide: лаконичные и стабильные UI тесты на Java</h3>
# <a class="result-title js-result-title" href="https://selenide.org/" rel="noopener">
#                    Selenide: concise UI tests in Java
#                </a>
# browser.all('[href="Selenide: concise UI tests in Java"]').should(have.size(3))
#Assert
#browser.all('[href="/yashaka/selene"]').should(have.size(3))