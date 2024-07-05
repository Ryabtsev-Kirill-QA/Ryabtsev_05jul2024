from pages_for_ui_tests.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def input_text(self, browser, book_name):
        return browser.find_element(By.XPATH, '//input[@class="header-search__input"]').send_keys(book_name)
