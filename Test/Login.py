import datetime
from datetime import date

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.sql import SqlServer

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

###Login

    def test01_login(self):
        self.driver.get(url_test)
        self.tests_texts.append("test")

    def test02_login(self):
        self.driver.get(url_test)


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


SqlServer.run_tests_and_insert_into_sql_server(TestLogin, 'test_login')
