# coding=utf8
# Two browsers test for Google and Firefox with Waiting functionality and screenshots
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner


class ChromeNASATest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_NASA_1(self):
        driver = self.driver
        driver.get("https://api.nasa.gov/")

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
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
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
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
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
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
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
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
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
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
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
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
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
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
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/img/favicons/favicon-192.png']")))
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


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))
