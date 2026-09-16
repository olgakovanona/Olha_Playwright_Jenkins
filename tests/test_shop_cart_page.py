# test 1: Check that user can adjust quantity of the product on shop cart page
# test 2: Check that user can continue shopping va shop cart page
# test 3: Check that user can go to checkout page via shop cart page and fill in address form
import time

from utils.data_generators import (generate_random_name, generate_random_email,
                                                            generate_random_phone, generate_random_address)


def test_total_price_after_user_adjusts_product_quantities(categories_page, shop_cart_page):
    categories_page.open_page()
    categories_page.add_product_to_cart()
    categories_page.proceed_to_checkout()

    shop_cart_page.wait_until_cart_popup_disappears()

    initial_price = shop_cart_page.get_total_product_price()

    shop_cart_page.increase_quantity()
    shop_cart_page.should_have_price_multiplied(initial_price, 2)


def test_user_can_continue_shopping(categories_page, shop_cart_page):
    categories_page.open_page()

    added_product = categories_page.add_product_to_cart()

    categories_page.proceed_to_checkout()

    shop_cart_page.wait_until_cart_popup_disappears()
    shop_cart_page.click_continue_shopping()

    categories_page.wait_until_products_loaded()
    categories_page.should_have_products_loaded()
    categories_page.should_contain_product(added_product)


def test_user_can_fill_checkout_address_form_and_proceed(categories_page, shop_cart_page, checkout_page):
    """
    E2E test: user adds product to cart, goes to checkout, fills address form with random data,
    continues checkout, saves address and verifies that no warning appears.
    """

    company_name = generate_random_name()
    email = generate_random_email()
    phone = generate_random_phone()
    address_data = generate_random_address()

    categories_page.open_page()
    categories_page.add_product_to_cart()
    categories_page.proceed_to_checkout()

    shop_cart_page.wait_until_cart_popup_disappears()

    shop_cart_page.click_go_to_checkout_page()

    # fill in the shipping address form
    checkout_page.fill_address_form(
        company_name,
        email,
        phone,
        address_data["street"],
        address_data["zip"],
        address_data["city"],
        address_data["country"],
        address_data["state"]
    )

    checkout_page.click_use_same()
    checkout_page.click_continue_checkout()

    # fill in the billing address form
    checkout_page.fill_address_form(
        company_name,
        email,
        phone,
        address_data["street"],
        address_data["zip"],
        address_data["city"],
        address_data["country"],
        address_data["state"]
    )

    checkout_page.click_save_address()
    checkout_page.should_not_have_warning()
