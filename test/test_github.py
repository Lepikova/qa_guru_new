import pytest
from selenium import webdriver


@pytest.mark.selenium
def test_open_google():
    driver = webdriver.Chrome()
    url = 'https://www.google.com/'

    driver.get(url)

    assert driver.title == "Google"
    assert driver.current_url == url