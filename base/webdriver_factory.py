from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver

from config import BASE_URL


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        if self.browser.lower() == "chrome":
            browser = webdriver.Chrome(ChromeDriverManager().install())
        elif self.browser.lower() == "firefox":
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser.lower() == "ie":
            browser = webdriver.Ie(IEDriverManager().install())
        else:
            browser = webdriver.Chrome(ChromeDriverManager().install())

        browser.get(BASE_URL)
        return browser
