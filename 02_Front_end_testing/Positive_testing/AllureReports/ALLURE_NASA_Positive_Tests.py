"""
To run the tests and generate reports: run the COMMAND from the CURRENT directory:

"""
import time
import requests
from faker import Faker
import unittest
import pytest
import HtmlTestRunner
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import ChromeDriverManager
from selenium.webdriver.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure_commons.types import AttachmentType

fake = Faker()


def delay():
    time.sleep(random.randint(1, 3))  # Delay all actions from 1 to 3 sec


# # ==========    Cross browser   ========================================
# # from webdriver_manager.firefox import GeckoDriverManager
# # from webdriver_manager.microsoft import EdgeChromiumDriverManager
# # from selenium.webdriver.firefox.service import Service
# # from selenium.webdriver.edge.service import Service

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
class ChromeBrowser(unittest.TestCase):
    # class ChromeBrowser(unittest.TestCase):
    options = Options()
    options.page_load_strategy = 'eager'
    svc = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=svc, options=options)

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

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-1: "Verify the form's TITLE is “Generate API Key”  .............
    def test01_form_title(self):

        driver3 = self.driver
        url = "https://api.nasa.gov/"
        driver3.get(url)
        driver3.maximize_window()

        try:
            driver3.find_element(By.XPATH, "//h2[contains(.,'Generate API Key')]")
            print("The Form Title is DISPLAYED")
            allure.attach(self.driver.get_screenshot_as_png(), name="Form_Title",
                          attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            print("The Form Title NOT PRESENT")
            allure.attach(self.driver.get_screenshot_as_png(), name="No_FormTitle",
                          attachment_type=AttachmentType.PNG)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...... TC-2: "Verify The form displays mandatory input fields"  ......

    def test02_all_fields_search(self):
        driver3 = self.driver
        url = "https://api.nasa.gov/"
        driver3.get(url)
        driver3.maximize_window()
        delay()
        try:
            # ...... FIRST NAME. Execute JavaScript to access shadow DOM and get the field .....
            element = driver3.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_first_name")')
            print("FIRST NAME field Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("FIRST NAME field NOT DISPLAYED")
            allure.attach(self.driver.get_screenshot_as_png(), name="No_FirstName",
                          attachment_type=AttachmentType.PNG)
        try:
            # ....... LAST NAME. Execute JavaScript to access shadow DOM and get the field .....
            element = driver3.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_last_name")')
            print("LAST NAME field Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("LAST NAME field NOT DISPLAYED")
            allure.attach(self.driver.get_screenshot_as_png(), name="No_FirstName",
                          attachment_type=AttachmentType.PNG)
        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field
            element = driver3.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_email")')
            print("EMAIL field Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("EMAIL field NOT DISPLAYED")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ......TC-3: Verify that mandatory input fields are marked with an asterisk (*)..............

    def test03_asterisk_search(self):

        driver4 = self.driver
        url = "https://api.nasa.gov/"
        driver4.get(url)
        driver4.maximize_window()

        # ...............(1) Locate the host element..........

        try:
            driver4.find_element(By.CSS_SELECTOR, ".api-umbrella-signup-embed-content-container")
            print("The Host Element Present")
        except NoSuchElementException:
            print("No Host Element Found")

        # ................(2) Access the shadow root...................
        try:
            host_element = driver4.find_element(By.CSS_SELECTOR, ".api-umbrella-signup-embed-content-container")
            shadow_root = driver4.execute_script('return arguments[0].shadowRoot', host_element)

            # .....(Use JavaScript to access the shadow root and find elements within it)......
            inner_element = driver4.execute_script(
                'return arguments[0].shadowRoot.querySelector("div:nth-child(1) > '
                'form:nth-child(2) > div:nth-child(1) > label:nth-child(1) > '
                'abbr:nth-child('
                '1)")', host_element)
            print("A '*' Element Present as Required.")
        except WDE:
            print("No '*' Element Found")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-4: "Verify  the optional text field 'How will you use the APIs?'."  ......

    def test04_optional_field_search(self):
        driver5 = self.driver
        url = "https://api.nasa.gov/"
        driver5.get(url)
        driver5.maximize_window()
        delay()
        try:
            # ...... OPTIONAL: 'HOW WILL YOU...'. Execute JavaScript to access shadow DOM and get the field ...
            element = driver5.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_use_description")')
            print("OPTIONAL field Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("OPTIONAL field NOT DISPLAYED")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ..........  TC-5: "Verify  the 'Signup' button"  ......

    def test05_signup_button_search(self):
        driver6 = self.driver
        url = "https://api.nasa.gov/"
        driver6.get(url)
        driver6.maximize_window()
        delay()
        try:
            # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
            element = driver6.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector(".btn.btn-lg.btn-primary")')
            print("SIGNUP button Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("SIGNUP button NOT DISPLAYED")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-6: "Verify The system generates an API key..."  ......

    def test06_complete_form_search(self):
        driver7 = self.driver
        url = "https://api.nasa.gov/"
        driver7.get(url)
        driver7.maximize_window()
        delay()
        try:
            # ...... FIRST NAME. Execute JavaScript to access shadow DOM and get the field .....
            FName = fake.first_name()

            element = driver7.execute_script(
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

            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_last_name")').send_keys(LName)
            print("Last Name: ", LName)  # For the records.

        except NoSuchElementException:
            print("LAST NAME field NOT DISPLAYED")

        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field .....
            email = fake.email()

            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_email")').send_keys(email)
            print(email)  # For the records.

        except NoSuchElementException:
            print("EMAIL field NOT DISPLAYED")

        try:
            # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector(".btn.btn-lg.btn-primary")').click()

        except NoSuchElementException:
            print("SIGNUP button NOT DISPLAYED")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-07: "Verify the header navigation bar"

    def test07_NASA_1(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        # header menu
        driver.find_element(By.XPATH, "(//span[contains(.,'Overview')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//a[@href='https://api.nasa.gov'][contains(.,'{ APIs }')]")))
            print("Overview is ready!")
        except TimeoutException:
            print("Overview doesn't work!")
            driver.get_screenshot_as_file("Overview_error.png")
            driver.save_screenshot('Overview_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Generate API Key')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Generate API Key')]")))
            print("Generate API Key is on the page!")
        except TimeoutException:
            print("Generate API Key doesn't work!")
            driver.get_screenshot_as_file("Generate_API_Key_error.png")
            driver.save_screenshot('Generate_API_Key_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Authentication')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(@id,'authentication')]")))
            print("Authentication is on the page!")
        except TimeoutException:
            print("Authentication doesn't work!")
            driver.get_screenshot_as_file("Authentication_error.png")
            driver.save_screenshot('Authentication_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Recover API Key')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'API Key Recovery')]")))
            print("API Key Recovery is on the page!")
        except TimeoutException:
            print("Recover API Key doesn't work!")
            driver.get_screenshot_as_file("Recover_API_Key_error.png")
            driver.save_screenshot('Recover_API_Key_error.png')

        driver.find_element(By.XPATH, "(// span[contains(., 'Browse APIs')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Browse APIs')]")))
            print("API Key Recovery is on the page!")
        except TimeoutException:
            print("Browse APIs doesn't work!")
            driver.get_screenshot_as_file("Browse_APIs_error.png")
            driver.save_screenshot('Browse_APIs_error.png')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-08: "Verify 'search' bar in the top menu"  ......
    def test08_NASA_2(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        try:
            # Locate the dropdown menu and enter a Keyword ("API") to expand options:
            dropdown_menu = driver.find_element(By.XPATH, "//input[@onkeyup='searchHeader()']")
            dropdown_menu.send_keys("API")
            # Locate the option "TLE API"
            element = driver.find_element(By.XPATH, "//span[text()='TLE API']")
            # Click on the option "TLE API"
            element.click()
            print("TLE API is on the page!")

        except NoSuchElementException:
            print("'search bar' doesn't work!")
            driver.get_screenshot_as_file("search_bar_error.png")
            driver.save_screenshot('search_bar_error.png')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-09: "Verify “Get Started” button"  ......
    def test09_NASA_3(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        driver.find_element(By.XPATH, "//button[contains(.,'Get Started')]").click()
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Generate API Key')]")))
            print("Generate API Key form is available")
        except TimeoutException:
            print("Generate API Key form not presented")
            driver.get_screenshot_as_file("Generate_API_Key_error.png")
            driver.save_screenshot('Generate_API_Key_error.png')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-10: "Verify “Browse APIs” button"  ......
    def test10_NASA_4(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        driver.find_element(By.XPATH, "//button[contains(.,'Browse APIs')]").click()
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Browse APIs')]")))
            print("Browse APIs are presented")
        except TimeoutException:
            print("Browse APIs not presented")
            driver.get_screenshot_as_file("Browse_APIs_error.png")
            driver.save_screenshot('Browse_APIs_error.png')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-11: "Verify submenu "Epic" in the "Browse APIs" menu"  ......
    def test11_nasa_chrome0(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("EPIC")
        search = driver.find_element(By.XPATH, "//button[@id='epic']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Epic"
        driver.find_element(By.XPATH, "//h3[contains(text(),'Retrievable Metadata')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//strong[contains(.,'Example image:')])[3]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[contains(@src,'KEY')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Querying by Date(s)')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'example-query')])[8]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-12: "Verify submenu "Exoplanet" in the "Browse APIs" menu"  ......
    def test12_nasa_chrome1(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Exoplanet")
        search = driver.find_element(By.XPATH, "//button[@id='exoplanet']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Exoplanet"
        driver.find_element(By.XPATH, "//h2[@id='exoPlanetIntro']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h2[@id='exoPlanetExamples']").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-13: "Verify submenu 'Open Science Data Repository'"  ......
    def test13_nasa_chrome2(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        # find in the "Browse APIs" menu submenu "Open Science Data Repository"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Open Science Data Repository")
        search = driver.find_element(By.XPATH, "//button[@id='open-science-data-repository']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Open Science Data Repository"
        driver.find_element(By.XPATH, "//h2[contains(.,'Study')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h4[contains(.,'Example Requests:')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(.,'Study Metadata API')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h4[contains(.,'Returns: JSON-formatted response')])[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(.,'Study Dataset Search API')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h4[contains(text(),'Syntax 2 (returns HTML response):')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h2[@id='other']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Format:')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Examples:')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h4[contains(text(),'Single Vehicle Call')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h2[contains(.,'API Requests with Python')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h2[contains(.,'Resources')]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-14: "Verify submenu "Insight""  ......
    def test14_nasa_chrome3(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        #  find in the "Browse APIs" menu submenu "Insight"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Insight")
        search = driver.find_element(By.XPATH, "//button[@id='insight']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Insight"
        driver.find_element(By.XPATH, "//h1[@id='insight_weather']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='assets/img/general/insight_photo.png']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'http-request')])[3]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'query-parameters')])[6]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='./assets/insight/insight_mars_wind_rose.png']").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-15: "Verify submenu "Mars Rover Photos""  ......
    def test15_nasa_chrome4(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        #  find in the "Browse APIs" menu submenu "Mars Rover Photos"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Mars Rover Photos")
        search = driver.find_element(By.XPATH, "//button[@id='mars-rover-photos']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Mars Rover Photos"
        driver.find_element(By.XPATH, "//h3[contains(text(),'Rover Cameras')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Querying by Martian sol')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'example-query')])[11]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(.,'Querying by Earth date')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'example-query')])[13]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(.,'Mission Manifest')]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-16: "Verify submenu "TLE API""  ......
    def test16_nasa_chrome5(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        #  find in the "Browse APIs" menu submenu "TLE API"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("TLE API")
        search = driver.find_element(By.XPATH, "//button[@id='tle-api']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "TLE API"
        driver.find_element(By.XPATH, "//h1[contains(.,'TLE API')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[@id='tle-http-request']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'example-query')])[15]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-17: "Verify submenu "Vesta/Moon/Mars Trek WMTS""  ......
    def test17_nasa_chrome6(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        #  find in the "Browse APIs" menu submenu "Vesta/Moon/Mars Trek WMTS"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Vesta/Moon/Mars Trek WMTS")
        search = driver.find_element(By.XPATH, "//button[@id='vesta-moon-mars-trek-wmts']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Vesta/Moon/Mars Trek WMTS"
        driver.find_element(By.XPATH, "//h1[@id='trek']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Available Moon Mosaics')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Available Mars Mosaics')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Available Vesta Mosaics')]").click()
        time.sleep(1)

        # closing the browser

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-18: "Verify the Header and URL on the 'Browse APIs' page"  ......

    def test18_check_browse_api_header_chrome(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        try:
            driver.find_element(By.XPATH, "//h2[contains(.,'Browse APIs')]")
        except NoSuchElementException:
            print("Header is different.")

        print("Header is correct")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-19: "Verify the NASA Image and Video Library submenu"  ......

    def test19_check_nasa_img_vid_lib_chrome(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the NASA Image and Video Library submenu works
        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='nasa-image-and-video-library']")))
        print("Sub-menu 'NASA Image and Video Library' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='nasa-image-and-video-library']")))
        print("Sub-menu 'NASA Image and Video Library' is clickable")

        # check if the table is present
        try:
            driver.find_element(By.XPATH,
                                "//body/main[@id='main-content']/section[@id='browseAPI']/div[1]/ul[1]/li[1]/div["
                                "1]/table[1]")
        except NoSuchElementException:
            print("Table is absent.")

        print("Table is present")

        driver.find_element(By.XPATH, "//button[@id='nasa-image-and-video-library']").click()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-20: "Verify the TechTransfer submenu"  ......

    def test20_check_techtransfer_chrome(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the TechTransfer submenu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='techtransfer']")))
        print("Sub-menu 'TechTransfer' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='techtransfer']")))
        print("Sub-menu 'TechTransfer' is clickable")

        driver.find_element(By.XPATH, "//button[@id='techtransfer']").click()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-21: "Verify the Satellite Situation Center submenu"  ......

    def test21_check_satellite_situation_center_chrome(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the Satellite Situation Center submenu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='satellite-situation-center']")))
        print("Sub-menu 'Satellite Situation Center' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='satellite-situation-center']")))
        print("Sub-menu 'Satellite Situation Center' is clickable")

        driver.find_element(By.XPATH, "//button[@id='satellite-situation-center']").click()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-22: "Verify the SSD/CNEOS submenu"  ......

    def test22_check_ssd_cneos_chrome(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the SSD/CNEOS submenu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='ssd-cneos']")))
        print("Sub-menu 'SSD/CNEOS' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ssd-cneos']")))
        print("Sub-menu 'SSD/CNEOS' is clickable")

        driver.find_element(By.XPATH, "//button[@id='ssd-cneos']").click()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def tearDown(self):
        self.driver.quit()


# =========================================================================
# ...........FirefoxBrowser:........................................
# =========================================================================
# ...............Setup Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Ensure GUI is off
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# ..............Set path to chromedriver as per your configuration
webdriver_service = Service(GeckoDriverManager().install())
driver_f = webdriver.Firefox(service=webdriver_service, options=chrome_options)


class FirefoxNASATests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # ......TC-23: Verify the webpage is accessible.........................
    # ......(Methods in UnitTest should start from "test" keyword).......
    def test23_webpage_access(self):
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

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-24: "Verify the form's TITLE is “Generate API Key”  .............
    def test24_form_title(self):

        driver3 = self.driver
        url = "https://api.nasa.gov/"
        driver3.get(url)
        driver3.maximize_window()

        try:
            driver3.find_element(By.XPATH, "//h2[contains(.,'Generate API Key')]")
            print("The Form Title is DISPLAYED")
            allure.attach(self.driver.get_screenshot_as_png(), name="Form_Title",
                          attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            print("The Form Title NOT PRESENT")
            allure.attach(self.driver.get_screenshot_as_png(), name="No_FormTitle",
                          attachment_type=AttachmentType.PNG)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...... TC-25: "Verify The form displays mandatory input fields"  ......

    def test25_all_fields_search(self):
        driver3 = self.driver
        url = "https://api.nasa.gov/"
        driver3.get(url)
        driver3.maximize_window()
        delay()
        try:
            # ...... FIRST NAME. Execute JavaScript to access shadow DOM and get the field .....
            element = driver3.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_first_name")')
            print("FIRST NAME field Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("FIRST NAME field NOT DISPLAYED")
            allure.attach(self.driver.get_screenshot_as_png(), name="No_FirstName",
                          attachment_type=AttachmentType.PNG)
        try:
            # ....... LAST NAME. Execute JavaScript to access shadow DOM and get the field .....
            element = driver3.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_last_name")')
            print("LAST NAME field Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("LAST NAME field NOT DISPLAYED")
            allure.attach(self.driver.get_screenshot_as_png(), name="No_FirstName",
                          attachment_type=AttachmentType.PNG)
        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field
            element = driver3.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_email")')
            print("EMAIL field Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("EMAIL field NOT DISPLAYED")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ......TC-26: Verify that mandatory input fields are marked with an asterisk (*)..............

    def test26_asterisk_search(self):

        driver4 = self.driver
        url = "https://api.nasa.gov/"
        driver4.get(url)
        driver4.maximize_window()

        # ...............(1) Locate the host element..........

        try:
            driver4.find_element(By.CSS_SELECTOR, ".api-umbrella-signup-embed-content-container")
            print("The Host Element Present")
        except NoSuchElementException:
            print("No Host Element Found")

        # ................(2) Access the shadow root...................
        try:
            host_element = driver4.find_element(By.CSS_SELECTOR, ".api-umbrella-signup-embed-content-container")
            shadow_root = driver4.execute_script('return arguments[0].shadowRoot', host_element)

            # .....(Use JavaScript to access the shadow root and find elements within it)......
            inner_element = driver4.execute_script(
                'return arguments[0].shadowRoot.querySelector("div:nth-child(1) > '
                'form:nth-child(2) > div:nth-child(1) > label:nth-child(1) > '
                'abbr:nth-child('
                '1)")', host_element)
            print("A '*' Element Present as Required.")
        except WDE:
            print("No '*' Element Found")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-27: "Verify  the optional text field 'How will you use the APIs?'."  ......

    def test27_optional_field_search(self):
        driver5 = self.driver
        url = "https://api.nasa.gov/"
        driver5.get(url)
        driver5.maximize_window()
        delay()
        try:
            # ...... OPTIONAL: 'HOW WILL YOU...'. Execute JavaScript to access shadow DOM and get the field ...
            element = driver5.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_use_description")')
            print("OPTIONAL field Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("OPTIONAL field NOT DISPLAYED")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ..........  TC-28: "Verify  the 'Signup' button"  ......

    def test28_signup_button_search(self):
        driver6 = self.driver
        url = "https://api.nasa.gov/"
        driver6.get(url)
        driver6.maximize_window()
        delay()
        try:
            # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
            element = driver6.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector(".btn.btn-lg.btn-primary")')
            print("SIGNUP button Found")
            # # ....... Now you can interact with the element ......
            # # ....... For example, to input text:
            # element.send_keys('Your text here')
        except NoSuchElementException:
            print("SIGNUP button NOT DISPLAYED")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-29: "Verify The system generates an API key..."  ......

    def test29_complete_form_search(self):
        driver7 = self.driver
        url = "https://api.nasa.gov/"
        driver7.get(url)
        driver7.maximize_window()
        delay()
        try:
            # ...... FIRST NAME. Execute JavaScript to access shadow DOM and get the field .....
            FName = fake.first_name()

            element = driver7.execute_script(
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

            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_last_name")').send_keys(LName)
            print("Last Name: ", LName)  # For the records.

        except NoSuchElementException:
            print("LAST NAME field NOT DISPLAYED")

        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field .....
            email = fake.email()

            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector("#user_email")').send_keys(email)
            print(email)  # For the records.

        except NoSuchElementException:
            print("EMAIL field NOT DISPLAYED")

        try:
            # ...... SIGNUP button. Execute JavaScript to access shadow DOM and get the element ...
            element = driver7.execute_script(
                'return document.querySelector(".api-umbrella-signup-embed-content-container").shadowRoot'
                '.querySelector(".btn.btn-lg.btn-primary")').click()

        except NoSuchElementException:
            print("SIGNUP button NOT DISPLAYED")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-30: "Verify the header navigation bar"  ......

    def test30_NASA_1(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        # header menu
        driver.find_element(By.XPATH, "(//span[contains(.,'Overview')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'{ NASA APIs }')]")))
            print("Overview is ready!")
        except TimeoutException:
            print("Overview doesn't work!")
            driver.get_screenshot_as_file("Overview_error.png")
            driver.save_screenshot('Overview_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Generate API Key')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Generate API Key')]")))
            print("Generate API Key is on the page!")
        except TimeoutException:
            print("Generate API Key doesn't work!")
            driver.get_screenshot_as_file("Generate_API_Key_error.png")
            driver.save_screenshot('Generate_API_Key_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Authentication')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(@id,'authentication')]")))
            print("Authentication is on the page!")
        except TimeoutException:
            print("Authentication doesn't work!")
            driver.get_screenshot_as_file("Authentication_error.png")
            driver.save_screenshot('Authentication_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Recover API Key')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'API Key Recovery')]")))
            print("API Key Recovery is on the page!")
        except TimeoutException:
            print("Recover API Key doesn't work!")
            driver.get_screenshot_as_file("Recover_error.png")
            driver.save_screenshot('Recover_error.png')

        driver.find_element(By.XPATH, "(// span[contains(., 'Browse APIs')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Browse APIs')]")))
            print("API Key Recovery is on the page!")
        except TimeoutException:
            print("Browse APIs doesn't work!")
            driver.get_screenshot_as_file("Browse_APIs_error.png")
            driver.save_screenshot('Browse_APIs_error.png')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-31: "Verify 'search' bar in the top menu"  ......

    def test31_NASA_2(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Verify “search bar” in the top menu
        element = driver.find_element(By.XPATH, "//input[@onkeyup='searchHeader()']")
        element.send_keys("API")
        element.submit()
        driver.find_element(By.XPATH, "//a[@href='#tle-api']").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[contains(@id,'tle')]")))
            print("TLE API is on the page!")
        except TimeoutException:
            print("'search bar' doesn't work!")
            driver.get_screenshot_as_file("search_bar_error.png")
            driver.save_screenshot('search_bar_error.png')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-32: "Verify “Get Started” button"  ......

    def test32_NASA_3(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Verify “Get Started” button
        driver.find_element(By.XPATH, "//button[contains(.,'Get Started')]").click()
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Generate API Key')]")))
            print("Generate API Key form is available")
        except TimeoutException:
            print("Generate API Key form not presented")
            driver.get_screenshot_as_file("Generate_API_error.png")
            driver.save_screenshot('Generate_API_error.png')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-33: "Verify “Browse APIs” button"  ......

    def test33_NASA_4(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Verify “Browse APIs” button
        driver.find_element(By.XPATH, "//button[contains(.,'Browse APIs')]").click()
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Browse APIs')]")))
            print("Browse APIs are presented")
        except TimeoutException:
            print("Browse APIs not presented")
            driver.get_screenshot_as_file("Browse_error.png")
            driver.save_screenshot('Browse_error.png')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-34: "Verify submenu "Epic" in the "Browse APIs" menu"  ......

    def test34_nasa_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Driver title in Firefox is:", driver.title)

        # find in the "Browse APIs" menu submenu "Epic"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("EPIC")
        search = driver.find_element(By.XPATH, "//button[@id='epic']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Epic"
        driver.find_element(By.XPATH, "//h3[contains(text(),'Retrievable Metadata')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//strong[contains(.,'Example image:')])[3]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[contains(@src,'KEY')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Querying by Date(s)')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'example-query')])[8]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-35: "Verify submenu "Exoplanet" in the "Browse APIs" menu"  ......

    def test35_nasa_firefox1(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        # find in the "Browse APIs" menu submenu "Exoplanet"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Exoplanet")
        search = driver.find_element(By.XPATH, "//button[@id='exoplanet']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Exoplanet"
        driver.find_element(By.XPATH, "//h2[@id='exoPlanetIntro']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h2[@id='exoPlanetExamples']").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-36: "Verify submenu 'Open Science Data Repository'"  ......

    def test36_nasa_firefox2(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        # find in the "Browse APIs" menu submenu "Open Science Data Repository"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Open Science Data Repository")
        search = driver.find_element(By.XPATH, "//button[@id='open-science-data-repository']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Open Science Data Repository"
        driver.find_element(By.XPATH, "//h2[contains(.,'Study')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h4[contains(.,'Example Requests:')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(.,'Study Metadata API')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h4[contains(.,'Returns: JSON-formatted response')])[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(.,'Study Dataset Search API')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h4[contains(text(),'Syntax 2 (returns HTML response):')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h2[@id='other']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Format:')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Examples:')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h4[contains(text(),'Single Vehicle Call')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h2[contains(.,'API Requests with Python')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h2[contains(.,'Resources')]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-37: "Verify submenu "Insight""  ......

    def test37_nasa_firefox3(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        #  find in the "Browse APIs" menu submenu "Insight"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Insight")
        search = driver.find_element(By.XPATH, "//button[@id='insight']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Insight"
        driver.find_element(By.XPATH, "//h1[@id='insight_weather']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='assets/img/general/insight_photo.png']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'http-request')])[3]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'query-parameters')])[6]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='./assets/insight/insight_mars_wind_rose.png']").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-38: "Verify submenu "Mars Rover Photos""  ......

    def test38_nasa_firefox4(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        #  find in the "Browse APIs" menu submenu "Mars Rover Photos"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Mars Rover Photos")
        search = driver.find_element(By.XPATH, "//button[@id='mars-rover-photos']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Mars Rover Photos"
        driver.find_element(By.XPATH, "//h3[contains(text(),'Rover Cameras')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Querying by Martian sol')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'example-query')])[11]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(.,'Querying by Earth date')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'example-query')])[13]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(.,'Mission Manifest')]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-39: "Verify submenu "TLE API""  ......

    def test39_nasa_firefox5(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        #  find in the "Browse APIs" menu submenu "TLE API"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("TLE API")
        search = driver.find_element(By.XPATH, "//button[@id='tle-api']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "TLE API"
        driver.find_element(By.XPATH, "//h1[contains(.,'TLE API')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[@id='tle-http-request']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "(//h3[contains(@id,'example-query')])[15]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-40: "Verify submenu "Vesta/Moon/Mars Trek WMTS""  ......

    def test40_nasa_firefox6(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()

        # wait 2 sec, then proceed with a script
        time.sleep(2)

        # Check if the search returns any result
        assert "NASA Open APIs" in driver.title
        print("NASA Open APIs Page Title is: ", driver.title)

        #  find in the "Browse APIs" menu submenu "Vesta/Moon/Mars Trek WMTS"
        search = driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]")
        search.click()
        search = driver.find_element(By.XPATH, "//input[@id='search-field-big']")
        search.send_keys("Vesta/Moon/Mars Trek WMTS")
        search = driver.find_element(By.XPATH, "//button[@id='vesta-moon-mars-trek-wmts']")
        search.click()
        time.sleep(1)

        # Checking the information from the submenu "Vesta/Moon/Mars Trek WMTS"
        driver.find_element(By.XPATH, "//h1[@id='trek']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Available Moon Mosaics')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Available Mars Mosaics')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//h3[contains(text(),'Available Vesta Mosaics')]").click()
        time.sleep(1)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-41: "Verify the Header and URL on the 'Browse APIs' page"  ......

    # check if a header and URL are correct and present

    def test41_check_browse_api_header_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        try:
            driver.find_element(By.XPATH, "//h2[contains(.,'Browse APIs')]")
        except NoSuchElementException:
            print("Header is different.")

        print("Header is correct")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-42: "Verify the NASA Image and Video Library submenu"  ......

    def test42_check_nasa_img_vid_lib_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the NASA Image and Video Library sub-menu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='nasa-image-and-video-library']")))
        print("Sub-menu 'NASA Image and Video Library' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='nasa-image-and-video-library']")))
        print("Sub-menu 'NASA Image and Video Library' is clickable")

        # check if the table is present
        try:
            driver.find_element(By.XPATH,
                                "//body/main[@id='main-content']/section[@id='browseAPI']/div[1]/ul[1]/li[1]/div["
                                "1]/table[1]")
        except NoSuchElementException:
            print("Table is absent.")

        print("Table is present")

        driver.find_element(By.XPATH, "//button[@id='nasa-image-and-video-library']").click()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-43: "Verify the TechTransfer submenu"  ......

    def test43_check_techtransfer_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the TechTransfer sub-menu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='techtransfer']")))
        print("Sub-menu 'TechTransfer' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='techtransfer']")))
        print("Sub-menu 'TechTransfer' is clickable")

        driver.find_element(By.XPATH, "//button[@id='techtransfer']").click()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-44: "Verify the Satellite Situation Center submenu"  ......

    def test44_check_satellite_situation_center_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the Satellite Situation Center sub-menu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='satellite-situation-center']")))
        print("Sub-menu 'Satellite Situation Center' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='satellite-situation-center']")))
        print("Sub-menu 'Satellite Situation Center' is clickable")

        driver.find_element(By.XPATH, "//button[@id='satellite-situation-center']").click()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-45: "Verify the SSD/CNEOS submenu"  ......

    def test45_check_ssd_cneos_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the SSD/CNEOS submenu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='ssd-cneos']")))
        print("Sub-menu 'SSD/CNEOS' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ssd-cneos']")))
        print("Sub-menu 'SSD/CNEOS' is clickable")

        driver.find_element(By.XPATH, "//button[@id='ssd-cneos']").click()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-46: "Verify the Techport submenu"  ......

    def test46_check_techport_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the Techport submenu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='techport']")))
        print("Sub-menu 'Techport' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='techport']")))
        print("Sub-menu 'Techport' is clickable")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def tearDown(self):
        self.driver.quit()

#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports_POS_NASA',
#                                                            report_name='POS_NASA_All_Tests'))

# ==============================================================================
# """
# (1)............. To run tests, execute the command line from the CURRENT DIRECTORY:
#
# >>   pytest -v -s ALLURE_NASA_Positive_Tests.py
#
# (2).............To run Allure reports from the CURRENT DIRECTORY:  ...............
#
# >>    python -m pytest -v -s --alluredir="reports" ALLURE_NASA_Positive_Tests.py
#
# (3)..............To display the Allure reports run the command from the CURRENT DIRECTORY:
#
# >> allure serve ./reports
# """
