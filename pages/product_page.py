from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button=self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def check_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "название продукта не найдено"
        assert self.is_element_present(*ProductPageLocators.BASKET_CONFIRM), "имя в корзине не найдено"
        product_name= self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_confirm = self.browser.find_element(*ProductPageLocators.BASKET_CONFIRM).text
        assert product_name == product_confirm, "название продукта в корзине не совпадает"

    def check_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "цена продукта не найдена"
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "цена не найдена"
        product_price= self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price= self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "цена товара в корзине не совпадает"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_CONFIRM),"Сообщение об успехе представлено, но не должно быть"
        print("OK")

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_CONFIRM), "Сообщение об успешном завершении должно исчезнуть, но все равно отображается"
        print("OK")