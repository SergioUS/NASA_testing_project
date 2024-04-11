import time
import requests
from faker import Faker
import unittest
import random
import json
import HtmlTestRunner
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

fake = Faker()
#
# ==========    Cross browser   ========================================
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

# =========================================================================
# ...........ChromeBrowser:........................................
# =========================================================================
# ...............Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ..............Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)


# ................................................................


def delay():
    time.sleep(random.randint(1, 3))  # Delay all actions from 1 to 3 sec


class ChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    # ......TC-0: Verify the webpage is accessible.........................
    # ......(Methods in UnitTest should start from "test" keyword).......
    def test00_webpage_access(self):
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

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...............  TC-8: "Verify the error message when "First Name" left empty."  ......
    # .......................(Methods in UnitTest should start from "test" keyword).....
    def test08_first_name_empty(self):
        driver8 = self.driver
        url = "https://api.nasa.gov/"
        driver8.get(url)
        driver8.maximize_window()
        delay()
        # ......  Skip the FIRST NAME field  ...........................
        # try:
        #     # ...... FIRST NAME. Execute JavaScript to access shadow DOM and get the field .....
        #     FName = fake.first_name()
        #
        #     element = driver8.execute_script(
        #         'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
        #         '.querySelector("#user_first_name")').send_keys(FName)
        #     print("First Name: ", FName)
        #     # # ....... Now you can interact with the element ......
        #     # # ....... For example, to input text:
        #     # element.send_keys('Your text here')
        # except NoSuchElementException:
        #     print("FIRST NAME field NOT DISPLAYED")

        try:
            # ....... LAST NAME. Execute JavaScript to access shadow DOM and get the field .....

            LName = fake.last_name()

            element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_last_name")').send_keys(LName)
            print("Last Name: ", LName)  # For the records.

        except NoSuchElementException:
            print("LAST NAME field NOT DISPLAYED")

        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field .....
            email = fake.email()

            element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_email")').send_keys(email)
            print(email)  # For the records.

        except NoSuchElementException:
            print("EMAIL field NOT DISPLAYED")

        try:
            # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
            element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector(".btn.btn-lg.btn-primary")').click()

        except NoSuchElementException:
            print("SIGNUP button NOT DISPLAYED")

        # ............. Verify the ERROR Message ........................
        try:
            # Execute JavaScript to access shadow DOM and get the "Fill out this field" message .....
            feedback_element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_first_name_feedback")')

            # Now you can interact with the feedback element
            # ... Get the text of the error message:
            feedback_text = feedback_element.text
            print("Error message: ", "'", feedback_text, "'")
        except NoSuchElementException:
            print("No Error Message Displayed.")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...............  TC_9: "Verify  the error message when "Last Name" left empty."  ......
    # .......................(Methods in UnitTest should start from "test" keyword).....
    def test09_last_name_empty(self):
        driver8 = self.driver
        url = "https://api.nasa.gov/"
        driver8.get(url)
        driver8.maximize_window()
        delay()
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

        #  .....   Skip the LAST NAME field  ........................
        # try:
        #     # ....... LAST NAME. Execute JavaScript to access shadow DOM and get the field .....
        #
        #     LName = fake.last_name()
        #
        #     element = driver8.execute_script(
        #         'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
        #         '.querySelector("#user_last_name")').send_keys(LName)
        #     print("Last Name: ", LName)  # For the records.
        #
        # except NoSuchElementException:
        #     print("LAST NAME field NOT DISPLAYED")

        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field .....
            email = fake.email()

            element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_email")').send_keys(email)
            print(email)  # For the records.

        except NoSuchElementException:
            print("EMAIL field NOT DISPLAYED")

        try:
            # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
            element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector(".btn.btn-lg.btn-primary")').click()

        except NoSuchElementException:
            print("SIGNUP button NOT DISPLAYED")

        # ............. Verify the ERROR Message ........................
        try:
            # Execute JavaScript to access shadow DOM and get the "Fill out this field" message .....
            feedback_element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_last_name_feedback")')

            # Now you can interact with the feedback element
            # ... Get the text of the error message:
            feedback_text = feedback_element.text
            print("Error message: ", "'", feedback_text, "'")
        except NoSuchElementException:
            print("No Error Message Displayed.")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...............  TC-10: "Verify  the error message when "Email" left empty."  ......
    def test10_email_empty(self):
        driver8 = self.driver
        url = "https://api.nasa.gov/"
        driver8.get(url)
        driver8.maximize_window()
        delay()
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

        # ...............Empty Email Address field (clear the email field) ................................
        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field .....
            # email = fake.email()

            element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_email")').clear()
            print("Email address:  ", element)  # For the records.

        except NoSuchElementException:
            print("EMAIL field NOT DISPLAYED")

        try:
            # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
            element = driver8.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector(".btn.btn-lg.btn-primary")').click()

        except NoSuchElementException:
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
            print("Error message: ", "'", feedback_text, "'")
        except NoSuchElementException:
            print("No Error Message Displayed.")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...............  TC-11: "Verify  the error message when "Email" is invalid"  ......
    # .......................(Methods in UnitTest should start from "test" keyword).....
    def test11_email_invalid(self):
        driver8 = self.driver
        url = "https://api.nasa.gov/"
        driver8.get(url)
        driver8.maximize_window()
        delay()
        bugs_number = 0
        # ............Read the invalid emails from the JSON file  .............
        with open("tc_11_invalid_emails.json", "r") as json_file:
            loaded_invalid_emails = json.load(json_file)

        # .......Input the loaded invalid email addresses one by one .....

        for email, reason in loaded_invalid_emails.items():
            print("========================================")

            # .......  Input invalid email address  ...............
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

            # ...... FIRST NAME. Execute JavaScript to access shadow DOM and get the field .....
            try:
                FName = fake.first_name()

                element = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_first_name")').clear()
                element = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_first_name")').send_keys(FName)
                print("First Name: ", FName)
                # # ....... Now you can interact with the element ......
                # # ....... For example, to input text:
                # element.send_keys('Your text here')
            except NoSuchElementException:
                print("FIRST NAME field NOT DISPLAYED")

            # ....... LAST NAME. Execute JavaScript to access shadow DOM and get the field
            try:
                LName = fake.last_name()

                element = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_last_name")').clear()
                element = driver8.execute_script(
                    'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                    '.querySelector("#user_last_name")').send_keys(LName)
                print("Last Name: ", LName)  # For the records.

            except NoSuchElementException:
                print("LAST NAME field NOT DISPLAYED")

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

                # ---------------------------------------------------------------------------------
                try:
                    # ... Get the text of the error message:
                    feedback_text = feedback_element.text
                    # Check if feedback_text is not empty (indicating an error message)
                    assert feedback_text != "", "Expected an error message. Error message is not displayed."
                except AssertionError as e:
                    # Handle the AssertionError by printing a custom error message
                    print(f"AssertionError: {e}")
                    print("  \n<== FAILED ==> Invalid format accepted.")
                    print(f"Invalid email:   {email}\nReason:          {reason}")
                    bugs_number += 1

                else:
                    # If feedback_text is not empty, the assertion will pass.
                    print(f"Error message: '{feedback_text}'\nAs Expected.\n* PASSED *")

            except NoSuchElementException:
                print("No Error Message Displayed.")

            driver8.back()
            driver8.forward()
        print("========================================")
        assert bugs_number == 0, "Number of bugs found = {}".format(bugs_number)

        # print(f'================\nNumber of bugs found = {bugs_number}')

    delay()


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./NEG_HtmlReports', report_name='NASA_Negative_Tests'))

# ==============================================================================
# ...To run tests and generate reports: run the command from the CURRENT directory:
# >> python NASA_Negative_Tests.py
