import re
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators.categories_page_locators import proceed_to_checkout_btn
from pages.locators.product_details_page_locators import product_title, product_price, \
    product_image, custom_leg, custom_input, add_to_cart_btn, popup_custom_label, popup_custom_value, \
    add_quantity_button, quantity_input


class ProductPage(BasePage):

    def get_product_title(self):
        return self.find(product_title).inner_text().strip()

    def get_product_price(self):
        text = self.find(product_price).inner_text()
        return float(text.strip().replace("$", "").replace(",", ""))

    def select_any_other_colour(self) -> str:
        # Search for input who hasn't attributes 'checked'
        inactive_input = self.page.locator("input.js_variant_change:not([checked])").first

        inactive_input.wait_for(state="attached")

        # Get colour name
        color_name = inactive_input.get_attribute("data-value_name") or inactive_input.get_attribute("title")

        if color_name is None:
            self.page.wait_for_timeout(1000)
            color_name = inactive_input.get_attribute("data-value_name")

        inactive_input.click(force=True)

        return str(color_name).strip()

    def should_have_correct_image_variant(self, expected_colour: str):
        if not expected_colour or expected_colour == "None":
            raise AssertionError("Expected colour name is empty! Check select_any_other_colour.")

        product_img = self.find("img.product_detail_img")

        # Escape special characters and replace spaces with .*
        # This will find "Steel, Black" even if the URL is "Steel%20Black"
        clean_pattern = re.escape(expected_colour).replace(r"\ ", ".*")
        regex = re.compile(rf".*{clean_pattern}.*", re.IGNORECASE)

        expect(
            product_img,
            f"Image source should change to contain: {expected_colour}"
        ).to_have_attribute("src", regex, timeout=10000)

    def hover_product_image(self):
        self.find(product_image).hover()

    def get_product_image_src(self):
        return self.find(product_image).get_attribute("src")

    def select_custom_legs(self):
        self.find(custom_leg).click()

    def enter_custom_text(self, text):
        self.find(custom_input).fill(text)

    def add_product_to_cart(self):
        self.find(add_to_cart_btn).click()

    def get_custom_popup_label(self):
        return self.find(popup_custom_label).inner_text()

    def get_custom_popup_value(self):
        return self.find(popup_custom_value).inner_text()

    def should_have_custom_input_visible(self):
        expect(self.find(custom_input)).to_be_visible()

    def should_have_custom_popup(self, expected_label, expected_value):
        expect(self.page.get_by_text(expected_label, exact=True).first).to_be_visible()
        expect(self.page.get_by_text(expected_value, exact=True).first).to_be_visible()

    def increase_quantity(self):
        button = self.find(add_quantity_button)
        button.wait_for(state="visible")
        button.click()
        expect(self.find(quantity_input).first).not_to_have_value("1")

    def wait_for_cart_popup(self):
        self.find(proceed_to_checkout_btn).wait_for(state="visible")

    def get_quantity_value(self):
        return float(self.find(quantity_input).input_value())

    def should_have_quantity(self, expected_value):
        expect(self.find(quantity_input)).to_have_value(str(expected_value))

    def should_have_product_data(self, expected_data: dict):
        expect(self.find(product_title)).to_have_text(expected_data["title"])

        # Check the price
        expected_price_str = str(expected_data["price"]).replace(".0", "")
        expect(self.find(product_price)).to_contain_text(expected_price_str)
