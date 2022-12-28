from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class BasePage():
    # Добавляем конструктор (__init__) — метод, который вызывается, когда мы создаем объект.
    # И передаем в качестве параметров экземпляр драйвера и url адрес.
    def __init__(self, browser, url, timeout=10):  # print("les4.3.6-3")
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # И добавляем метод open - он будет открывать нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)

    # Проверка элемента на странице - https://stepik.org/lesson/238819/step/6
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            # print(f"Your code: {alert_text}")
            print(f"{bcolors.OKGREEN}Your code: {alert_text}{bcolors.ENDC}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка для входа не найдена"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Значок пользователя не найден," \
                                                                     "вероятно, неавторизованный пользователь"
