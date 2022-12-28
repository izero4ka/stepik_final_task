# from .base_page import BasePage
# from selenium.webdriver.common.by import By

a = '''
class MainPage(BasePage): 
	def go_to_login_page(self):
		login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
		login_link.click()
	def should_be_login_link(self):
		#self.browser.find_element(By.CSS_SELECTOR, "#login_link")
		assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
'''
'''
from .locators import MainPageLocators
class MainPage(BasePage): 
	def go_to_login_page(self):
		link = self.browser.find_element(
			*MainPageLocators.LOGIN_LINK)
		link.click()
		# return LoginPage(browser=self.browser, url=self.browser.curren
		#alert = self.browser.switch_to.alert
		#alert.accept()
	def should_be_login_link(self):
		assert self.is_element_present(
			*MainPageLocators.LOGIN_LINK), "Login link is not presented"
'''

# Page Object для главной страницы сайта - https://stepik.org/lesson/238819/step/3
# https://stepik.org/lesson/238819/step/5
# Локаторы - https://stepik.org/lesson/238819/step/7
# return LoginPage - https://stepik.org/lesson/238819/step/9

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
