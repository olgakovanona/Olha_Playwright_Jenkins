import pytest
import allure
from playwright.sync_api import Page
from pages.categories_page import CategoriesPage
from pages.checkout_page import CheckoutPage
from pages.product_details_page import ProductPage
from pages.shop_cart_page import ShopCartPage


@pytest.fixture
def categories_page(page: Page):
    return CategoriesPage(page)


@pytest.fixture
def product_page(page: Page):
    return ProductPage(page)


@pytest.fixture
def shop_cart_page(page: Page):
    return ShopCartPage(page)


@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)
