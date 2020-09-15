import pytest
from base.base_test import BaseTest

login = 'standard_user'
password = 'secret_sauce'
invalid_user_login = 'xyz'
invalid_user_password = 'abc'


class TestLoginToPortal(BaseTest):
    @pytest.fixture(autouse=True)
    def init(self, browser):
        super().init(browser)

    def test_invalid_login(self):
        self.pages.get_login_page.login_to_portal(invalid_user_login, invalid_user_password)
        assert self.pages.get_login_page.invalid_login_msg()

    def test_valid_login(self):
        self.pages.get_login_page.login_to_portal(login, password)
        assert self.pages.get_login_page.is_valid_login()
