# Элементы страниц в паттерне Page Object - https://stepik.org/lesson/238819/step/7

from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


# https://stepik.org/lesson/238819/step/8
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#register_form input[type=email]")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#register_form input[name=registration-password1]")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#register_form input[name=registration-password2]")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    BASKET_CONFIRM = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner>strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
