from locators.main_products_locators import ProductsPageLocators
from base.base_page import BasePage


class MainProductsPage(BasePage):
    def get_number_of_products(self):
        products_number = self.browser.find_elements(*ProductsPageLocators.number_of_products)
        return len(products_number)

    def open_product_details(self):
        self.click_element(ProductsPageLocators.item)

    def add_product_to_cart(self):
        self.click_element(ProductsPageLocators.adding_button)

    def check_is_remove_button_appear(self):
        return self.is_element_visible(ProductsPageLocators.confirmation_button)
