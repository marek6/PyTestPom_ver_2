import pytest
from base.base_test import BaseTest

login = 'standard_user'
password = 'secret_sauce'
expected_products_number = 6


class TestMainProducts(BaseTest):
    @pytest.fixture(autouse=True)
    def init(self, browser):
        super().init(browser)

    def test_count_products_number(self):
        self.pages.get_login_page.login_to_portal(login, password)
        assert self.pages.get_main_products_page.get_number_of_products() == expected_products_number

    def test_adding_product_to_cart(self):
        self.pages.get_login_page.login_to_portal(login, password)
        self.pages.get_main_products_page.open_product_details()
        self.pages.get_main_products_page.add_product_to_cart()
        assert True is self.pages.get_main_products_page.check_is_remove_button_appear()
