from behave import given, when, then
from time import sleep


@given('Open the Relly main page')
def open_page(context):
    context.app.main_page.open_main()
    context.app.signin_page.verify_signin_page()
    sleep(3)


@then('Input email {expected_field} is entered')
def input_field(context,expected_field):
    context.app.signin_page.input_field(expected_field)


@then('Input password field {expected_field} is entered')
def password_field(context,expected_field):
    context.app.signin_page.password_field(expected_field)


@then('Click on Continue button')
def submit_login(context):
    context.app.signin_page.click_submit_login()


@then('Verify {user} logged in')
def verify_login(context,user):
    context.app.signin_page.verify_user_loggedin(user)


@then('Click on Off-plan at the left side menu')
def click_on_text(context):
    context.app.main_page.click_on_text()


@then('Open filter window')
def open_filter_window(context):
    context.app.main_page.open_filter_window()


@then('Filter by sale status of “Newly Launched”')
def open_newlaunch_filter(context):
    context.app.main_page.open_newlaunch_filter()


@then('Verify each product contains the Newly Launched tag')
def verify_newlaunch_tag(context):
    context.app.main_page.verify_newlaunch_tag()
