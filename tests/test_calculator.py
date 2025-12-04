import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_teardown():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_addition(setup_teardown):
    driver = setup_teardown

    driver.get("http://localhost:8888/index.html") 
    driver.find_element(By.ID, "num1").send_keys("100")
    driver.find_element(By.ID, "num2").send_keys("43")

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    result=driver.find_element(By.ID,"result").text

    assert "143" in result, f"Expected 143, but got: {result}"

    print("Test Passed")



