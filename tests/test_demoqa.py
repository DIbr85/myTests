import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class Test:
    def test_links(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        url = "https://demoqa.com/links"
        driver.get(url)
        driver.maximize_window()
        click_created = driver.find_element(By.XPATH, "//a[@id='created']")
        click_created.click()
        message = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@id='linkResponse']")))
        driver.execute_script("arguments[0].scrollIntoView();", message)
        text_message = "Link has responded with staus 201 and status text Created"
        assert message.text == text_message
        time.sleep(5)
        driver.quit()

    def test_text_box(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        url = "https://demoqa.com/text-box"
        driver.get(url)
        driver.maximize_window()
        FULL_NAME = (By.XPATH, "//input[@id='userName']")
        EMAIL = (By.XPATH, "//input[@id='userEmail']")
        CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
        PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
        SUBMIT = (By.XPATH, "//button[@id='submit']")
        email = "RamFromEgypt@mail.com"
        current_adr = "Cairo, Egyptian Museum, Tahrir Square"
        wait(driver, 10).until(EC.visibility_of_element_located(FULL_NAME)).send_keys("Ramses")
        wait(driver, 10).until(EC.visibility_of_element_located(EMAIL)).send_keys(email)
        wait(driver, 10).until(EC.visibility_of_element_located(CURRENT_ADDRESS)).send_keys(current_adr)
        wait(driver, 10).until(EC.visibility_of_element_located(PERMANENT_ADDRESS)).send_keys("Egypt, 2nd pyramid, "
                                                                                              "sarcophagus No. 1")
        submit = wait(driver, 10).until(EC.presence_of_element_located(SUBMIT))
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()
        time.sleep(5)
        driver.quit()



