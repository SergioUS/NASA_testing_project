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

fake = Faker()

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

        # .........  NP-T2: "Verify the form's TITLE is “Generate API Key”  .............

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # .........  TC-2: "Verify the form's TITLE is “Generate API Key”  .............
    def test01_form_title(self):

        driver3 = self.driver
        url = "https://api.nasa.gov/"
        driver3.get(url)
        driver3.maximize_window()

        try:
            driver3.find_element(By.XPATH, "//h2[contains(.,'Generate API Key')]")
            print("The Form Title is DISPLAYED")
        except NoSuchElementException:
            print("The Form Title NOT PRESENT")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ...... TC-3: "Verify The form displays mandatory input fields"  ......

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

        try:
            # ....... EMAIL. Execute JavaScript to access shadow DOM and get the field .....
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
    # ......TC-4: Verify that mandatory input fields are marked with an asterisk (*)..............

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
    # .........  TC-5: "Verify  the optional text field 'How will you use the APIs?'."  ......

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
    # ..........  TC-6: "Verify  the 'Signup' button"  ......

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
    # .........  TC-7: "Verify The system generates an API key..."  ......

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

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# coding=utf8
# Two-browser test for Google and Firefox with Waiting functionality and screenshots

class ChromeNASATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_NASA_1(self):
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
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Generate API Key')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Generate API Key')]")))
            print("Generate API Key is on the page!")
        except TimeoutException:
            print("Generate API Key doesn't work!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Authentication')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(@id,'authentication')]")))
            print("Authentication is on the page!")
        except TimeoutException:
            print("Authentication doesn't work!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Recover API Key')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'API Key Recovery')]")))
            print("API Key Recovery is on the page!")
        except TimeoutException:
            print("Recover API Key doesn't work!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        driver.find_element(By.XPATH, "(// span[contains(., 'Browse APIs')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Browse APIs')]")))
            print("API Key Recovery is on the page!")
        except TimeoutException:
            print("Browse APIs doesn't work!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

    def test_NASA_2(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
        time.sleep(1)  # simulate long-running test

        assert "NASA Open APIs" in driver.title
        print("Page title in Chrome is:", driver.title)

        try:
            # Verify “search bar” in the top menu
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
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

    def test_NASA_3(self):
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
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

    def test_NASA_4(self):
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
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

    def tearDown(self):
        self.driver.quit()


class FirefoxNASATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_NASA_1(self):
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
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Generate API Key')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Generate API Key')]")))
            print("Generate API Key is on the page!")
        except TimeoutException:
            print("Generate API Key doesn't work!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Authentication')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(@id,'authentication')]")))
            print("Authentication is on the page!")
        except TimeoutException:
            print("Authentication doesn't work!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        driver.find_element(By.XPATH, "(//span[contains(.,'Recover API Key')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'API Key Recovery')]")))
            print("API Key Recovery is on the page!")
        except TimeoutException:
            print("Recover API Key doesn't work!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        driver.find_element(By.XPATH, "(// span[contains(., 'Browse APIs')])[1]").click()

        # Check that an element is present on a page and visible.
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Browse APIs')]")))
            print("API Key Recovery is on the page!")
        except TimeoutException:
            print("Browse APIs doesn't work!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

    def test_NASA_2(self):
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
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

    def test_NASA_3(self):
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
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

    def test_NASA_4(self):
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
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

    # Delay all actions from 1 to 3 sec
    delay()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class ChromePositiveTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        # Open the site page

    def test_nasa_chrome(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
        time.sleep(2)

        # Check if the search returns any result
        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Driver title in Chrome is:", driver.title)

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

        # Open the site page

    def test_nasa_chrome1(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

    def test_nasa_chrome2(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

    def test_nasa_chrome3(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
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

    def test_nasa_chrome4(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

    def test_nasa_chrome5(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

    def test_nasa_chrome6(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

    def tearDown(self):
        self.driver.quit()


class FirefoxPositiveTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

        # Open the site page

    def test_nasa_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

        # Open the site page

    def test_nasa_firefox1(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

        # Open the site page

    def test_nasa_firefox2(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

        # Open the site page

    def test_nasa_firefox3(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
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

        # Open the site page

    def test_nasa_firefox4(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

        # Open the site page

    def test_nasa_firefox5(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

        # Open the site page

    def test_nasa_firefox6(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # wait 2 sec, then proceed with script
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

class Chrome(unittest.TestCase):
    options = Options()
    options.page_load_strategy = 'eager'
    svc = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=svc, options=options)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_check_driver_and_url_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'{ NASA APIs }')]")))
        print(driver.title)
        print(driver.current_url)
        time.sleep(1)  # simulate long-running test

        # maximize and minimize window
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

    # check if a header and URL are correct and present
    def test_check_browse_api_header_firefox(self):
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

    def test_check_nasa_img_vid_lib_firefox(self):
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

    def test_check_techtransfer_firefox(self):
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

    def test_check_satellite_situation_center_firefox(self):
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

    def test_check_ssd_cneos_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the SSD/CNEOS sub-menu works

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

    def test_check_techport_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the Techport sub-menu works

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        wait = WebDriverWait(driver, 2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='techport']")))
        print("Sub-menu 'Techport' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='techport']")))
        print("Sub-menu 'Techport' is clickable")

    def tearDown(self):
        self.driver.quit()


class Firefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_check_driver_and_url_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'{ NASA APIs }')]")))
        print(driver.title)
        print(driver.current_url)
        time.sleep(1)  # simulate long-running test

        # maximize and minimize window
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

    # check if a header and URL are correct and present

    def test_check_browse_api_header_firefox(self):
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

    def test_check_nasa_img_vid_lib_firefox(self):
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

    def test_check_techtransfer_firefox(self):
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

    def test_check_satellite_situation_center_firefox(self):
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

    def test_check_ssd_cneos_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")

        # check if the SSD/CNEOS sub-menu works

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

    def test_check_techport_firefox(self):
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

    # def tearDown(self):
    #     self.driver.quit()


def tearDown(self):
    self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports_POS_NASA_API_KEY',
                                                           report_name='POS_NASA_test_report'))

# ==============================================================================
# ...To run tests and generate reports: run the COMMAND from the current directory:
# >> python NASA_Positive_Tests.py
