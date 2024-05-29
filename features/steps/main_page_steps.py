from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()


@when("Search for {expected_item}")
def search_product(context, expected_item):
    context.app.header.click_cart()


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Store product name')
def store_product_name(context):
    context.wait.until(
        EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not present on the page'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    context.wait.until(
        EC.invisibility_of_element_located(SIDE_NAV_ADD_TO_CART_BTN),
        message='Side nav, Add to Cart button did not disappear'
    )


@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):  # expected_amount = '5'
    expected_amount = int(expected_amount)  # '5' (str) => 5 (int)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'