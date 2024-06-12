from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions

from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


    #driver_path = GeckoDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ####
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('--window-size=1920,1080')
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
     #    options=options,
      #   service=service
    #)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #bs_user = 'nandinisarkar_SA5mDb'
    #bs_key = 'RsMZ3Z1HxxvquWC5kV2q'
    #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    #options = Options()
    #bstack_options = {
     #   'os': 'Windows',
      #  'osVersion': '10',
       # 'browserName': 'chrome',
        #'sessionName': '22-User can filter by sale status Newly Launch'
    #}
    #options.set_capability('bstack:options', bstack_options)
    #context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)  # excess to main_page, header, search_result_page

    #Chrome Dev Tools Mobile Emulation
    mobile_emulation = {
        "deviceName": "iPhone SE"
    }

    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)

    context.driver = webdriver.Chrome(service=service, options=chrome_options)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()



    # BROWSERS WITH DRIVERS: provide path to the driver file ### not very using this function browser
    #service = Service(executable_path='C:\Users\Nandini\python-selenium-automation\operadriver_win32')
    #context.driver = webdriver.chrome(service=service)












