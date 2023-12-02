import datetime
from datetime import date

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.sql import SqlServer
from Pages.EmailPage import *

from time import sleep
from Locators import *
from Pages.Login import LoginPage
import unittest

service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

start_time = datetime.datetime.now().replace(microsecond=0)


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []
        cls.tests_screens = []

###Login

    def test01_login(self):
        self.driver.get("https://testbpm.2ms.ir/login")
        self.driver.find_element('xpath', "wwww")
        self.driver.save_screenshot('error_screenshot.png')
        self.tests_texts.append("test1")
        self.tests_screens.append("test01_login_error_screenshot.png")

    def test02_login(self):
        self.driver.get("https://testbpm.2ms.ir/login")
        self.tests_texts.append("test2")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


# run_tests_and_send_email(TestLogin, 'aminpapi192236@gmail.com')

# SqlServer.run_tests_and_insert_into_sql_server(TestLogin, 'TestLogin')
