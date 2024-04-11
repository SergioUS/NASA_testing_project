import os
import time
import requests
from faker import Faker
import unittest
import HtmlTestRunner
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
    driver = None

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    # ...... Verify the webpage is accessible.........................
    # ...... (Methods in UnitTest should start from "test" keyword).......
    def test0_webpage_search(self):  # Check that an element is present on the DOM of a page and visible.
        driver1 = self.driver
        url = "https://gtmetrix.com/"
        driver1.get(url)
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
            assert "GTmetrix | Website Performance Testing and Monitoring" in driver1.title
            print("Test0: Webpage is CORRECT. Current Title is: ", driver1.title)
        except AssertionError:
            print("Webpage is different, current Title is: ", driver1.title)

        # Delay all actions from 1 to 3 sec
        delay()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .......  TC: "Evaluate the performance ... website using the GTMetrix tool."  ......

    def test1_gtmetrix(self):
        driver1 = self.driver
        url = "https://gtmetrix.com/"
        driver1.get(url)
        driver1.maximize_window()

        delay()

        # ..............Asserting that the page is correct............................
        try:
            assert driver1.find_element(By.XPATH, "//h1[contains(.,'How fast does your website load?')]")
            print("Page is Correct.")
        except AssertionError:
            print("Page title is different.", "Current Page Title is:",
                  driver1.find_element(By.XPATH, "//h1[contains(.,'How fast does your website load?')]").text)

        # .............. Filling in the input box and clicking the "Test your site" button ....................
        driver1.find_element(By.XPATH, "//input[contains(@placeholder,'Enter URL to Analyze...')]").send_keys("https"
                                                                                                              "://api"
                                                                                                              ".nasa.gov/")

        # .......... Continue to the next page...........................
        try:
            driver1.find_element(By.XPATH, "//button[normalize-space()='Test your site']").click()
        except NoSuchElementException:
            print("The BUTTON not Found")

        # ................  Verify the presence of the header "Report Generated!" ............
        try:
            WebDriverWait(driver1, 50).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Report "
                                                                                       "Generated!')]")))
            driver1.find_element(By.XPATH, "//h2[contains(text(),'Report Generated!')]")
            print("Report Generated!")

            # Delay all actions from 1 to 3 sec
            delay()

            # ...............  Create an Account: Filling in the form  .........................
            FName = fake.first_name()
            driver1.find_element(By.ID, "su-first_name").send_keys(FName)
            print("First Name: ", FName)  # For the records.

            LName = fake.last_name()
            driver1.find_element(By.ID, "su-last_name").send_keys(LName)
            print("Last Name: ", LName)  # For the records.

            email = fake.email()
            driver1.find_element(By.ID, "su-email").send_keys(email)
            print(email)  # For the records.

            fakePassword = fake.password()
            driver1.find_element(By.ID, "su-password").send_keys(fakePassword)
            print(fakePassword)  # For the records.

            password_confirm = driver1.find_element(By.ID, "su-password-confirm")
            password_confirm.send_keys(fakePassword)

            terms = driver1.find_element(By.XPATH, "//input[contains(@name,'accept_terms')]")
            terms.click()

            news = driver1.find_element(By.XPATH, "//input[contains(@name,'email_optin')]")
            news.click()

            continue_button = driver1.find_element(By.XPATH,
                                                   "//button[@type='submit'][contains(.,'Create an Account')]")
            continue_button.click()

            # .....Verify the message: "Almost done! Check your e-mail ... your account" ..........
            try:
                driver1.find_element(By.XPATH,
                                     "//p[contains(.,'Almost done! Check your e-mail for a validation link.Click on it "
                                     "to activate your account.')]")
                print("SUCCESS! 'Check your e-mail for a validation link'")

            except NoSuchElementException:
                print("Message is MISSING!")

        except TimeoutException:
            # .................ERROR - Reached the tests limit..............
            driver1.find_element(By.XPATH, "//div[@class='cta-analyze-limit']")
            print("Sorry, you've reached your test limit!")
            print("Goodbye!")

            # Capture screenshot as base64 encoded string
            screenshot_base64 = driver1.get_screenshot_as_base64()

            # Get the HTML report file path
            report_path = os.path.join(os.getcwd(), "GTMetrix_HtmlReports/AZZZ_test_report.html")

            # Embed the screenshot directly in the HTML report
            with open(report_path, "a") as report_file:
                report_file.write(f'<img src="data:image/png;base64,{screenshot_base64}" />')

    delay()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    # Specify the directory where you want to save the screenshots
    screenshot_dir = "./GTMetrix_HtmlReports"

    # Ensure the directory exists, if not, create it
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Run the test suite with HtmlTestRunner
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=screenshot_dir,
                                                           report_name='GTMetrix_test_report'))

# ==============================================================================
# ...To run tests and generate reports: run the COMMAND from the current directory:

# >> python <FileName.py>

# ...In this case, it is:

# >> python GTMetrix_Test.py
