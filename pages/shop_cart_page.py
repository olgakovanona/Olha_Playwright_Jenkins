from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators.product_details_page_locators import add_quantity_button
from pages.locators.shop_cart_locators import total_product_price, continue_shopping_btn, \
    checkout_btn
from pages.locators.categories_page_locators import proceed_to_checkout_btn


class ShopCartPage(BasePage):
    def wait_until_cart_popup_disappears(self):
        self.find(proceed_to_checkout_btn).wait_for(state="hidden")

    def increase_quantity(self):
        self.find(add_quantity_button).click()

    def get_total_product_price(self):
        price_text = self.find(total_product_price).inner_text()
        return float(price_text.replace(",", "").strip().replace("$", ""))

    def click_continue_shopping(self):
        self.find(continue_shopping_btn).click()

    def click_go_to_checkout_page(self):
        self.find(checkout_btn).click()

    def should_have_price_multiplied(self, initial_price: float, multiplier: int):
        expected_price = initial_price * multiplier

        # Format the number with a comma as a thousands separator and 2 decimal places (e.g., 1,725.00)
        expected_price_str = f"{expected_price:,.2f}"

        (expect(self.find(total_product_price), f"Total price should be updated to {expected_price_str}")
         .to_contain_text(expected_price_str))

        # Final precision check to ensure the numeric value is exactly correct
        actual_price = self.get_total_product_price()
        assert round(actual_price, 2) == round(expected_price, 2), \
            f"Expected price {expected_price}, but got {actual_price}"
