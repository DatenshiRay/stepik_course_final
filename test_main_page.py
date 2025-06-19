from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    # Открываем главную страницу сайта
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser=browser, url=link)
    main_page.open()
    # Находим и кликаем на ссылку для входа
 
    main_page.go_to_login_page()

    # Проверяем, что переход на страницу входа произошел успешно
    assert "login" in browser.current_url, "Login link is not working correctly"
