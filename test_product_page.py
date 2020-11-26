from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

link = ProductPageLocators.PRODUCT_LINK

def test_promo_in_link(browser):
    page = ProductPage(browser, link)
    page.should_be_promo_in_link()

def test_add_product_to_bag(browser):
    page = ProductPage(browser, link)
    page.add_to_bag()
