import pytest

from base.webdriver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture()
def browser(request):
    web_driver_factory = WebDriverFactory(request.config.getoption("--browser"))
    browser = web_driver_factory.get_webdriver_instance()
    browser.maximize_window()
    browser.implicitly_wait(10)

    def finalizer():
        browser.quit()

    request.addfinalizer(finalizer)
    return browser


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        if "browser" in item.fixturenames:
            browser = item.funcargs['browser']
            extra.append(pytest_html.extras.url(browser.current_url))
            screenshot = browser.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
