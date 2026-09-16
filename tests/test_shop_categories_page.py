# test 1: Check that user can add product to cart via the Categories page and cart quantity will be displayed
# test 2: Check that user can filter product by Legs -> Custom
# test 3: Check that user can open the Product details via the Categories page and check title and price

def test_add_product_to_cart(categories_page):
    categories_page.open_page()
    categories_page.add_product_to_cart()
    categories_page.proceed_to_checkout()

    categories_page.should_have_cart_quantity(1)


def test_filter_custom_shows_only_customizable_desk(categories_page):
    categories_page.open_page()
    categories_page.select_legs()
    categories_page.wait_until_products_count_is(1)

    categories_page.should_have_single_product_with_title("Customizable Desk")


def test_product_title_and_price_are_same_on_pdp(categories_page, product_page):
    categories_page.open_page()
    categories_page.wait_until_products_loaded()

    product_data = categories_page.get_first_product_data()

    categories_page.open_first_product()

    product_page.should_have_product_data(product_data)
