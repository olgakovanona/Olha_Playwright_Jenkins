from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators.address_form_page_locators import name_input, email_input, phone_input, \
    street_input, zip_input, city_input, country_select, state_select, use_same_checkbox, continue_checkout_btn
from pages.locators.shipping_page_locators import warning_message, save_address_btn


class CheckoutPage(BasePage):
    def fill_name(self, name):
        self.find(name_input).fill(name)

    def fill_email(self, email):
        self.find(email_input).fill(email)

    def fill_phone(self, phone):
        self.find(phone_input).fill(phone)

    def fill_street(self, street):
        self.find(street_input).fill(street)

    def fill_zip(self, zip_code):
        self.find(zip_input).fill(zip_code)

    def fill_city(self, city):
        self.find(city_input).fill(city)

    def select_country(self, country):
        self.find(country_select).select_option(label=country)

    def select_state(self, state):
        select_locator = self.find(state_select)
        select_locator.locator("option:nth-child(2)").wait_for(state="attached")
        select_locator.select_option(label=state)

    def fill_address_form(
            self,
            name,
            email,
            phone,
            street,
            zip_code,
            city,
            country,
            state
    ):
        self.fill_name(name)
        self.fill_email(email)
        self.fill_phone(phone)
        self.fill_street(street)
        self.fill_zip(zip_code)
        self.fill_city(city)
        self.select_country(country)
        self.select_state(state)

    def click_use_same(self):
        self.find(use_same_checkbox).click()

    def click_continue_checkout(self):
        self.find(continue_checkout_btn).click()

    def is_warning_displayed(self):
        return self.find(warning_message).is_visible()

    def should_have_warning(self):
        expect(self.find(warning_message)).to_be_visible()

    def should_not_have_warning(self):
        expect(self.find(warning_message)).to_be_hidden()

    def click_save_address(self):
        self.find(save_address_btn).click()
