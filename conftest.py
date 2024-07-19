import pytest
import requests
from selenium import webdriver


def options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1900,1030")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture(autouse=True)
def driver(request):
    driver = options()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def get_joke():
    response = requests.get(
        url="https://geek-jokes.sameerkumar.website/api"
    )
    assert response.status_code == 200, f"Status Code Error: Expected 200, but got {response.status_code}"
    return response.json()

