from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

from Locators import *
from Pages.Login import LoginPage
from Pages.Orders_Create import Orders_Create
from Pages.Find_Element import FindElement
import unittest

driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_Orders_Create(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

###Login

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9122367860")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43126")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل شد")
###Orders_Create

    def test02_orders_create(self):
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders_create.enter_click_orders_create()
        findel.wait_until_element_has_an_attribute('xpath', orders_create_name_select, 'class', 'selection')
        orders_create.enter_orders_create_name_select_text("ملیک")
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', orders_create_name_select_option,
                                                   'class', 'select2-results__option select2-results__option--highlighted')
        # orders_create.enter_orders_create_name_select_option()
        orders_create.enter_orders_create_check_transport()
        orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        print("با موفقیت تست بررسی شد.")

###orders_create_products

    def test03_orders_create(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_products_holder()

        sleep(3)

        print("با موفقیت تست بررسی شد.")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
