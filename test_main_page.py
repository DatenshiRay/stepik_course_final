import time

import pytest

from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
# Открываем главную страницу сайта
@pytest.mark.login_guest
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/"])
class TestLoginFromMainPage():
   def test_guest_can_go_to_login_page(self, browser, link):
      main_page = MainPage(browser=browser, url=link)
      main_page.open()
      # Находим и кликаем на ссылку для входа

      main_page.go_to_login_page()
      login_page = LoginPage(browser, browser.current_url)

      # Проверяем, что переход на страницу входа произошел успешно
      login_page.should_be_login_page()

   def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, link):

      main_page = MainPage(browser=browser, url=link)
      main_page.open()

      main_page.go_to_basket_page()
      basket_page = BasketPage(browser, browser.current_url)

      basket_page.should_not_be_content_in_basket()
      basket_page.should_be_content_title_is_empty()