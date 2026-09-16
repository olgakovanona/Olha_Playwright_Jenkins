# test 1: Check that user can select another color, e.g. black of the product via product details page
# test 2: Check that user can custom the product via product details page and add it to cart
# test 3: Check that user can add several products to the cart via product details page
import time


def test_user_can_select_another_product_colour(categories_page, product_page):
    categories_page.open_page()
    categories_page.open_first_product()

    selected_colour = product_page.select_any_other_colour()

    product_page.hover_product_image()

    product_page.should_have_correct_image_variant(selected_colour)


def test_user_can_custom_product(categories_page, product_page):
    categories_page.open_page()
    categories_page.wait_until_products_loaded()
    categories_page.open_first_product()

    product_page.select_custom_legs()
    product_page.should_have_custom_input_visible()

    product_page.enter_custom_text("test")
    product_page.add_product_to_cart()

    product_page.should_have_custom_popup("Custom", "test")


def test_user_can_add_several_product_items_to_cart(categories_page, product_page):
    categories_page.open_page()
    categories_page.wait_until_products_loaded()
    categories_page.open_first_product()

    product_page.increase_quantity()
    product_page.add_product_to_cart()
    product_page.wait_for_cart_popup()

    product_page.should_have_quantity(2)
