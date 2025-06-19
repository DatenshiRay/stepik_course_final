from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    # Открываем главную страницу сайта
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)

    # Находим и кликаем на ссылку для входа
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

    # Проверяем, что переход на страницу входа произошел успешно
    assert "login" in browser.current_url, "Login link is not working correctly"
