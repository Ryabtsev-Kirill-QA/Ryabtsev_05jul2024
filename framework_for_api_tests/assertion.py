import allure
import requests


def assertFalse(a: bool, msg: str):
    final_msg = f"\n\nПолучено: {a};\n\nОжидалось: False;\n\n{msg}"
    with allure.step(final_msg):
        assert not a, final_msg


def assertTrue(a: bool, msg: str):
    final_msg = f"\n\nПолучено: {a};Ожидалось: True;\n\n{msg}"
    with allure.step(final_msg):
        assert a, final_msg


def assertIsNone(variable_, msg: str):
    @allure.step(msg)
    def wrapper(variable):
        assert variable is None, msg

    wrapper(variable_)


def assertIsNotNone(variable_, msg: str):
    @allure.step(msg)
    def wrapper(variable):
        assert variable is not None, msg

    wrapper(variable_)


def assertEqual(received_, expected_, msg):
    @allure.step(msg)
    def wrapper(received, expected):
        assert received == expected, f"{msg}\nExpected: {expected}\nReceived: {received}"

    wrapper(received_, expected_)


def assertStatusCode(response_: requests.Response, expected_: int):
    msg = "Проверка статус кода ответа."

    @allure.step(msg)
    def wrapper(response: requests.Response, expected):
        assert response.status_code == expected, (
                f"{msg}\nExpected: {expected}\nReceived: {response_.status_code}.\n"
                + f"Тело ответа: {response.content.decode()}"
        )

    wrapper(response_, expected_)


def assertNotEqual(received_, expected_, msg):
    @allure.step(msg)
    def wrapper(received, expected):
        assert received != expected, msg

    wrapper(received_, expected_)


def assertIn(what_, where_, msg):
    @allure.step(msg)
    def wrapper(what, where):
        assert what in where, msg

    wrapper(what_, where_)
