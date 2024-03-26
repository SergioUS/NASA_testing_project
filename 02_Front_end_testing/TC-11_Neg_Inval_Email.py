import random
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

    # # .............Cross browser.............................................
    # # from webdriver_manager.firefox import GeckoDriverManager
    # # from webdriver_manager.microsoft import EdgeChromiumDriverManager
    # # from selenium.webdriver.firefox.service import Service
    # # from selenium.webdriver.edge.service import Service


# ...........ChromeBrowser:........................................


class ChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...............  NP-T11: "Verify  that an error message when "Email" is invalid"  ......
    # .......................(Methods in UnitTest should start from "test" keyword).....
    def test11_email_invalid(self):
        driver8 = self.driver
        url = "https://api.nasa.gov/"
        driver8.get(url)
        driver8.maximize_window()
        delay()

        # >>>>>>>   Invalid email addresses:   >>>>>>>>>>>>>>

        # 1. john.doe.example.com                (missing "@" symbol)
        # 2. jane_smith123@                     (missing domain)
        # 3. @company.com                       (missing username)
        # 4. bob.smith@com                      (incorrect domain format)
        # 5. .john.doe@example.com              (incorrect format)
        # 6. bob@smith@example.com              (multiple "@" symbols)
        # 7. jane_smith123@-emailprovider.com    (hyphen at the beginning of the domain name)
        # 8. john.doe@example..com              (multiple consecutive dots in the domain name)
        # 9. jane_smith123@emailprovider.       (trailing dot in the domain name)

        badEmail = ["john.doe.example.com",
                    "jane_smith123@",
                    "@company.com",
                    ".john.doe@example.com",
                    "bob@smith@example.com",
                    "jane_smith123@-emailprovider.com",
                    "john.doe@example..com",
                    "jane_smith123@emailprovider.",
                    "bob.smith@com"]

        for email in badEmail:
            print("----------------------------------")
            try:
                # ...... FIRST NAME. Execute JavaScript to access shadow DOM and get the field .....
                FName = fake.first_name()

                element = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_first_name")').send_keys(FName)
                print("First Name: ", FName)
                # # ....... Now you can interact with the element ......
                # # ....... For example, to input text:
                # element.send_keys('Your text here')
            except NoSuchElementException:
                print("FIRST NAME field NOT DISPLAYED")

            try:
                # ....... LAST NAME. Execute JavaScript to access shadow DOM and get the field .....

                LName = fake.last_name()

                element = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_last_name")').send_keys(LName)
                print("Last Name: ", LName)  # For the records.

            except NoSuchElementException:
                print("LAST NAME field NOT DISPLAYED")

            # ?????????????????????????????? for email in badEmail:
            try:
                inputBox = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_email")').clear()
                inputBox = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_email")').send_keys(email)
                print("Invalid Email Address:  ", email)  # For the records.

            except NoSuchElementException:
                print("EMAIL field NOT DISPLAYED")

            try:
                # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
                element = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector(".btn.btn-lg.btn-primary")').click()
            except WDE:
                print("SIGNUP button NOT DISPLAYED")

                # ............. Verify the ERROR Message ........................
            try:
                # Execute JavaScript to access shadow DOM and get the "Enter an email address." message .....
                feedback_element = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_email_feedback")')

                # Now we can interact with the feedback element
                # ... Get the text of the error message:
                feedback_text = feedback_element.text
                if feedback_text != "":
                    print("Error message: ", "'", feedback_text, "'")
                    print("As Expected.")
                    print("PASSED")
                else:
                    print("==> Invalid format", email, " accepted.")
                    print("=======> BUG! <==========")
            except NoSuchElementException:
                print("No Error Message Displayed.")

            driver8.back()
            driver8.forward()


delay()


def tearDown(self):
    self.driver.quit()
