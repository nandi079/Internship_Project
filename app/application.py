from pages.main_page import MainPage
from pages.signin_page import SignInPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.signin_page = SignInPage(driver)
















