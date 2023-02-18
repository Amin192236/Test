from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from Pages.Login import LoginPage
from Pages.Orders import Orders
import unittest

driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_bpm(unittest.TestCase):
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
###Orders

    def test02_orders(self):
        orders = Orders(driver=self.driver)
        orders.enter_click_orders()
        orders.enter_orders_start_date()
        orders.enter_orders_start_date_month()
        orders.enter_orders_start_date_month_option()
        orders.enter_orders_start_date_option()
        orders.enter_orders_end_date()
        orders.enter_orders_end_date_month()
        orders.enter_orders_end_date_month_option()
        orders.enter_orders_end_date_option()
        orders.enter_orders_click_span()
        orders.enter_orders_dateFilter()
        sleep(2)
        orders.enter_assert_orders_result()
        print("با موفقیت تست بررسی شد.")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
