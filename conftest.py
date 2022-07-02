import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# The page load strategy:
#  normal-Used by default, 
#  eager - DOM access is ready, but other resources like images may still be loading
options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(options=options,
                              service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
