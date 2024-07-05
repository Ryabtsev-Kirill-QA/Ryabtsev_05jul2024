import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_get_token():
    response = requests.get('https://www.chitai-gorod.ru')
    cookies = response.cookies
    token = cookies.get('access-token')
    return token[9:]


@pytest.fixture
def base_url():
    return 'https://web-gate.chitai-gorod.ru/api/v1'


@pytest.fixture
def headers():
    token = test_get_token()
    headers = \
        {
            'accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://www.chitai-gorod.ru/',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
    return headers


@pytest.fixture(scope="session")
def browser():
    """
    Main fixture
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # open Browser in maximized mode
    chrome_options.add_argument("--disable-infobars") # disabling infobars
    chrome_options.add_argument("--disable-extensions") # disabling extensions
    chrome_options.add_argument("--disable-gpu") #  applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
    # chrome_options.add_argument("--headless")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
