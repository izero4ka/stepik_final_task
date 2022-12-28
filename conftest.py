import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="Chrome",
                     help="Выберите браузер: Chrome или Firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Выберите язык: ru, en or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "Chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nЗапуск браузера Chrome для теста..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "Firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nЗапуск браузера Firefox для теста..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name должно быть Chrome или Firefox")
    yield browser
    print("\nЗакрытие браузера..")
    browser.quit()
