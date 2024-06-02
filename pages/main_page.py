from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    #OFF_PLAN_LINK = (By.CSS_SELECTOR, "address[id='w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b']")
    OFF_PLAN_LINK = (By.XPATH, "//a[@class='_1-link-menu w-inline-block w--current']")
    #OFF_PLAN_LINK = (By.XPATH, "//div[@class='menu-text' and text()='Off-Plan']")
    FILTER_LINK = (By.XPATH, "//a[@class='filter-button w-inline-block']")
    NEWLY_LAUNCHED_FILTER = (By.XPATH, "//div[@class='tag-text-proparties'and text()='Newly Launched']")
    NEW_LAUNCHED_LISTING = (By.XPATH, "//div[@w-el-text='Status']")
    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def click_on_text(self):
        sleep(10)
        self.wait_until_visible(*self.OFF_PLAN_LINK)
        self.click(*self.OFF_PLAN_LINK)
        sleep(5)

    def open_filter_window(self):
        self.click(*self.FILTER_LINK)
        sleep(3)

    def open_newlaunch_filter(self):
        self.click(*self.NEWLY_LAUNCHED_FILTER)
        sleep(7)

    def verify_newlaunch_tag(self):
        all_listing = self.find_elements(*self.NEW_LAUNCHED_LISTING)  # [WebEl1, WebEl2, WebEl3, WebEl4]

        for listing in all_listing:
            title = listing.find_element(*self.NEW_LAUNCHED_LISTING).text
            assert title, 'Newly Launched'
