import allure
from time import sleep
from pages_for_ui_tests.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

book_name = 'Болотник панченко'
URL = "https://www.chitai-gorod.ru/"


@allure.tag("web")
@allure.label("owner", "kirill_r")
@allure.feature("Cart")
def test_find_and_add_book_in_cart(browser):
    main_page = MainPage(browser)

    with allure.step("Переходим на стартовую страницу"):
        main_page.go_to_site()

    with allure.step("В поисковой строке вводим название искомой книги"):
        main_page.input_text(browser, book_name)
        main_page.find_element((By.XPATH, '//*[@class="search-product-card"]'))
        WebDriverWait(browser, timeout=5, poll_frequency=2).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@class="search-product-card"]'), "Болотник"))

    with allure.step("Нажимаем кнопку поиск"):
        search_button = browser.find_element(By.XPATH, '//button[@class="header-search__button"]')
        search_button.click()

    with allure.step("Скроллим вниз странички с товаром"):
        main_page.find_element((By.XPATH, '//section[@class="catalog-list catalog-search-products__list"]'))
        browser.execute_script("window.scrollBy(0, 400)")

    with allure.step("Нажимаем кнопку Купить"):
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Купить")]')))
        buy_button = browser.find_element(By.XPATH, '//span[contains(text(), "Купить")]')
        buy_button.click()
        sleep(2)

    with allure.step("Проверяем, что в корзину добавлен товар"):
        count_of_books_in_cart = browser.find_element(By.XPATH, "//*[@id='__layout']/div/header/div/div[2]/a/span[1]")
        assert "1" in count_of_books_in_cart.text
