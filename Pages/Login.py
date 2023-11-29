
import os
from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# import pytesseract
# from PIL import Image


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.2)
    element.click()
    sleep(0.2)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.2)
    element.clear()
    sleep(0.2)
    element.send_keys(text)
    sleep(0.2)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_login_phone_number(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', login_phone_number, text)

    def enter_login_check_phone_number(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_check_phone_number)

    def enter_login_password(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', login_password, text)

    def enter_login_password_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_password_submit)
