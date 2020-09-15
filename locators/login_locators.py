from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_input = (By.ID, 'user-name')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    valid_login = (By.XPATH, '//*[@id="inventory_filter_container"]//*[@class="product_label"]')
    invalid_login_message = (By.XPATH, '//*[@id="login_button_container"]/div/form/h3')