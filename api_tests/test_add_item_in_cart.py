import allure
import pytest
import requests
from api_tests import params_add_item as prm
from framework_for_api_tests import assertion, error_msg
from framework_for_api_tests.attach import add_logs_request


@allure.story('Add item in cart')
class TestAddItem:
    @allure.description(
        """
        Тест POST-запроса на добавление книги в корзину с вызовом 200 ответа
        """
    )
    @allure.title("POST/cart")
    @allure.severity('critical')
    @pytest.mark.parametrize("request_body, status_code", prm.add_item_positive_post)
    def test_item_in_cart_positive_post(self, base_url, request_body, headers, status_code):
        response = requests.post(f'{base_url}/cart/product', json=request_body, headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, status_code)
        add_logs_request(response)

    @allure.description(
        """
        Тест POST-запроса на добавление книги в корзину с вызовом 405 ответа
        """
    )
    @allure.title("POST/cart")
    @allure.severity('normal')
    def test_item_in_cart_negative_post(self, base_url, headers):
        response = requests.post(f'{base_url}/cart/product', headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, 400)
