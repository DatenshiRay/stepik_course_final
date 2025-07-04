import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавление опции для выбора языка браузера
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Choose browser language"
    )

@pytest.fixture(scope="function")
def browser(request):
    # Получение значения языка из параметров командной строки
    browser_language = request.config.getoption('language')
    options = Options()
    # Установка предпочтительного языка для браузера
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    

    yield browser

    # Закрытие браузера после выполнения теста
    browser.quit()
