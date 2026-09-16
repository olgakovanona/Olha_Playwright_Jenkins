import time

from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators.categories_page_locators import product_cards, product_title_in_card, \
    cart_btn, proceed_to_checkout_btn, checkbox_custom_legs, product_titles, product_price_in_card, cart_quantity_label
import re


class CategoriesPage(BasePage):
    page_url = ''

    def wait_until_products_loaded(self):
        self.find(product_cards).first.wait_for(state="visible")

    def add_product_to_cart(self, product_name: str = None) -> str:
        """Selects a product, adds it to cart, and returns its name.
        If product_name is provided, it finds that specific product.
        Otherwise, it picks the first available product on the page.
        """
        if product_name:
            # Find the specific card by text
            target_card = self.find(product_cards).filter(has_text=product_name).first
        else:
            # Pick the very first product card available
            target_card = self.find(product_cards).first

        # Get the actual title to verify it in the popup later
        actual_name = target_card.locator(product_title_in_card).inner_text().strip()

        target_card.hover()
        target_card.locator(cart_btn).click(force=True)

        # Wait for popup to confirm action
        expect(self.find('strong.product-name').filter(has_text=actual_name)).to_be_visible()

        return actual_name

    def should_contain_product(self, expected_title: str):
        """Verifies that the product list contains the specified title."""

        expect(
            self.find(product_titles),
            f"Product list should contain '{expected_title}'"
        ).to_contain_text([expected_title])

    def proceed_to_checkout(self):
        self.find(proceed_to_checkout_btn).click()

    def select_legs(self):
        time.sleep(0.5)
        self.find(checkbox_custom_legs).first.click()

    def get_product_titles(self):
        return self.find(product_titles).all_inner_texts()

    def wait_until_products_count_is(self, count):
        expect(self.find(product_cards)).to_have_count(count)

    def get_first_product_title(self):
        return self.find(product_title_in_card).first.inner_text().strip()

    def get_first_product_price(self):
        price_text = self.find(product_price_in_card).first.inner_text()
        return float(price_text.replace("$", "").replace(",", ""))

    def get_first_product_data(self):
        return {
            "title": self.get_first_product_title(),
            "price": self.get_first_product_price()
        }

    def open_first_product(self):
        self.find(product_title_in_card).first.click()

    def should_have_single_product_with_title(self, expected_title: str):
        titles_locator = self.find(product_titles)
        expect(titles_locator).to_have_count(1)
        expect(titles_locator).to_have_text(expected_title)

    def should_have_cart_quantity(self, expected_quantity: int):
        locator = self.find(f"{cart_quantity_label}:visible").first

        expect(locator, f"Expected product quantity: {expected_quantity}").to_have_text(str(expected_quantity))

    def should_have_products_loaded(self):
        expect(self.find(product_cards).first, "Product list is empty").to_be_visible()

    def should_contains_product(self, expected_title: str):
        (expect(self.find(product_titles), f"Product name '{expected_title}' wasn't find in product list")
         .to_contain_text([expected_title]))
