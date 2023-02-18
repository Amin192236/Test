from Locators import *


class Orders_Create:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_orders_create(self):
        self.driver.find_element('xpath', click_orders_create).click()

    def enter_orders_create_name_select(self):
        self.driver.find_element('xpath', orders_create_name_select).click()

    def enter_orders_create_name_select_text(self, name):
        self.driver.find_element('xpath', orders_create_name_select_text).send_keys(name)

    def enter_orders_create_name_select_option(self):
        self.driver.find_element('xpath', orders_create_name_select_option).click()

    def enter_orders_create_check_transport(self):
        self.driver.find_element('xpath', orders_create_check_transport).click()

    def enter_orders_create_check_clearance(self):
        self.driver.find_element('xpath', orders_create_check_clearance).click()

    def enter_orders_create_chooseservices(self):
        self.driver.find_element('xpath', orders_create_chooseservices).click()

    def enter_orders_create_products_holder(self):
        self.driver.find_element('xpath', orders_create_products_holder).click()

    def enter_orders_create_category_select(self):
        self.driver.find_element('xpath', orders_create_category_select).click()

    def enter_orders_create_category_select_option(self):
        self.driver.find_element('xpath', orders_create_category_select_option).click()

    def enter_orders_create_form_name(self, name):
        self.driver.find_element('xpath', orders_create_form_name).send_keys(name)

    def enter_orders_create_form_name_en(self, name):
        self.driver.find_element('xpath', orders_create_form_name_en).send_keys(name)

    def enter_orders_create_form_type(self):
        self.driver.find_element('xpath', orders_create_form_type).click()

    def enter_orders_create_form_type_option(self):
        self.driver.find_element('xpath', orders_create_form_type_option).click()

    def enter_orders_create_form_quantity(self):
        self.driver.find_element('xpath', orders_create_form_quantity).click()

    def enter_orders_create_form_quantity_option(self):
        self.driver.find_element('xpath', orders_create_form_quantity_option).click()

    def enter_orders_create_form_quantity_number(self, number):
        self.driver.find_element('xpath', orders_create_form_quantity_number).send_keys(number)

    def enter_orders_create_form_one_weight(self, number):
        self.driver.find_element('xpath', orders_create_form_one_weight).send_keys(number)

    def enter_orders_create_form_length(self, number):
        self.driver.find_element('xpath', orders_create_form_length).send_keys(number)

    def enter_orders_create_form_width(self, number):
        self.driver.find_element('xpath', orders_create_form_width).send_keys(number)

    def enter_orders_create_form_height(self, number):
        self.driver.find_element('xpath', orders_create_form_height).send_keys(number)

    def enter_orders_create_form_quantity_in_box(self, number):
        self.driver.find_element('xpath', orders_create_form_quantity_in_box).send_keys(number)

    def enter_orders_create_form_price_unit(self):
        self.driver.find_element('xpath', orders_create_form_price_unit).click()

    def enter_orders_create_form_price_unit_option(self):
        self.driver.find_element('xpath', orders_create_form_price_unit_option).click()

    def enter_orders_create_form_one_price(self, number):
        self.driver.find_element('xpath', orders_create_form_one_price).send_keys(number)

    def enter_orders_create_form_price(self, number):
        self.driver.find_element('xpath', orders_create_form_price).send_keys(number)

    def enter_orders_create_HSCODE(self):
        self.driver.find_element('xpath', orders_create_HSCODE).click()

    def enter_orders_create_HSCODE_option(self):
        self.driver.find_element('xpath', orders_create_HSCODE_option).click()

    def enter_orders_create_form_part_number(self, number):
        self.driver.find_element('xpath', orders_create_form_part_number).send_keys(number)

    def enter_orders_create_form_buy_url(self, url):
        self.driver.find_element('xpath', orders_create_form_buy_url).send_keys(url)

    def enter_orders_create_form_text(self, text):
        self.driver.find_element('xpath', orders_create_form_text).send_keys(text)

    def enter_orders_create_form_country(self, country):
        self.driver.find_element('xpath', orders_create_form_country).send_keys(country)

    def enter_orders_create_submit_information(self):
        self.driver.find_element('xpath', orders_create_submit_information).click()











