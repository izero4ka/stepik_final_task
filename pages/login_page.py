# Реализация LoginPage - https://stepik.org/lesson/238819/step/8

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Неправильный url страницы входа"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма входа не найдена"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена"

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        mail.send_keys(email)
        passw = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        passw.send_keys(password)
        conf = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        conf.send_keys(password)
        but = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        but.click()
