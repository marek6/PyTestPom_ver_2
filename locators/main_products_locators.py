from selenium.webdriver.common.by import By


class ProductsPageLocators:
    number_of_products = (By.XPATH, '//*[@id="inventory_container"]//*[@class="inventory_item"]')
    item = (By.XPATH, '//*[text()[contains(.,"Sauce Labs Bolt T-Shirt")]]')
    adding_button = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div/button')
    confirmation_button = (By.XPATH, '//*[@id="inventory_item_container"]//*[@class="btn_secondary btn_inventory"]')
