"""
Cross-browser UnitTest framework script for User API Key Management Form
with Waiting and API functional and Webdriver-Manager functionality
for Chrome, FireFox and Edge browsers
......................
Ensure that:
Selenium is upgraded to v4.0.0:

         pip3 install -U selenium

Webdriver Manager for Python is installed:

            pip3 install webdriver-manager

For Tutorial "How to use Webdriver Manager" go to: https://github.com/SergioUS/webdriver_manager
"""
import time
import requests
from faker import Faker
import unittest
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# import HtmlTestRunner

# ...............Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ..............Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
# ................................................................
fake = Faker()


def delay():
    time.sleep(random.randint(1, 3))  # Delay all actions from 1 to 3 sec


# .............Cross browser.............................................
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

# ...........ChromeBrowser:........................................


class ChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ......  Verify preconditions: the webpage is accessible   .....................
    # ...................(Methods in UnitTest should start from "test" keyword).......
    def test0_webpage_search(self):
        driver1 = self.driver

        # .........Check that an element is present on the DOM of a page and visible.
        url = "https://api.nasa.gov/"
        driver1.get(url)
        driver1.maximize_window()
        driver1.minimize_window()
        driver1.maximize_window()

        # ................API testing from Selenium....................
        print("Webpage Url has", requests.get(url).status_code, "as status Code")
        code = requests.get(url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # .................Check current webpage Title with Exception functionality
        try:
            assert "NASA Open APIs" in driver1.title
            print("Webpage is CORRECT. Current Title is: ", driver1.title)
        except WDE:
            print("Webpage is different, current Title is: ", driver1.title)

        # Delay all actions from 1 to 3 sec
        delay()

    def tearDown(self):
        self.driver.quit()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  NP-T2: "Verify the form's TITLE is “Generate API Key”  .............

    def test2_title_search(self):

        driver3 = self.driver
        url = "https://api.nasa.gov/"
        driver3.get(url)
        driver3.maximize_window()

        try:
            driver3.find_element(By.XPATH, "//h2[contains(.,'Generate API Key')]")
            print("The Form Title is DISPLAYED")
        except NoSuchElementException:
            print("The Form Title NOT PRESENT")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def tearDown(self):
    self.driver.quit()
