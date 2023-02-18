from Locators import *


class Orders:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_orders(self):
        self.driver.find_element('xpath', click_orders).click()

    def enter_orders_start_date(self):
        self.driver.find_element('xpath', orders_start_date).click()

    def enter_orders_start_date_month(self):
        self.driver.find_element('xpath', orders_start_date_month).click()

    def enter_orders_start_date_month_option(self):
        self.driver.find_element('xpath', orders_start_date_month_option).click()

    def enter_orders_start_date_back(self):
        self.driver.find_element('xpath', orders_start_date_back).click()

    def enter_orders_start_date_option(self):
        self.driver.find_element('xpath', orders_start_date_option).click()

    def enter_orders_end_date(self):
        self.driver.find_element('xpath', orders_end_date).click()

    def enter_orders_end_date_month(self):
        self.driver.find_element('xpath', orders_end_date_month).click()

    def enter_orders_end_date_month_option(self):
        self.driver.find_element('xpath', orders_end_date_month_option).click()

    def enter_orders_end_date_back(self):
        self.driver.find_element('xpath', orders_end_date_back).click()

    def enter_orders_end_date_option(self):
        self.driver.find_element('xpath', orders_end_date_option).click()

    def enter_orders_click_span(self):
        self.driver.find_element('xpath', orders_click_span).click()

    def enter_orders_dateFilter(self):
        self.driver.find_element('xpath', orders_dateFilter).click()

    def enter_assert_orders_result(self):
        check_result= self.driver.find_element('xpath', orders_normalize_space).text

        # assert check_result== "نتایج 1 تا 30 از 1353 نتیجه "

        print("نتایج بصورت: ", check_result, "می باشد." )
        # print("نتایج بصورت: ", check_result, "می باشد." )


