import datetime
from datetime import date

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.sql import db

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

###Login

    def test01_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver=self.driver)
        login.enter_login_phone_number("09379161530")
        login.enter_login_check_phone_number()



    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


try:
    sleep(2)
    msg = 'pass'
except:
    msg = 'fail'

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
end_time = datetime.datetime.now().replace(microsecond=0)
duration = (end_time - start_time).total_seconds()
db('Inquiry', 'login', date.today(), current_time, duration, msg)

