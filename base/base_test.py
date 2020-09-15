from managers.page_manager import PageManager


class BaseTest:
    pages: PageManager = None

    def init(self, browser):
        self.pages = PageManager(browser)
