from Locators import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_login_username(self, mobile):
        self.driver.find_element('xpath', login_username).send_keys(mobile)

    def enter_login_btn_submit_next(self):
        self.driver.find_element('xpath', login_btn_submit_next).click()

    def enter_login_password(self, code):
        self.driver.find_element('xpath', login_password).send_keys(code)

    def enter_login_btn_submit(self):
        self.driver.find_element('xpath', login_btn_submit).click()

