# Cross-Browser test with Chrome, FireFox and Edge. 3 same tests for each Browser
import unittest
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

fake = Faker()

class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def test_search_nasa_Chrome1(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='apod']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='apod']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='apod']")))
        print("Precipitation button APOD is visible ")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='apod']")))
        print("Wind button APOD is clickable")

    def test_search_nasa_Chrome2(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='asteroids-neows']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='asteroids-neows']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='asteroids-neows']")))
        print("Precipitation button Asteroids is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='asteroids-neows']")))
        print("Wind button Asteroids is clickable")

    def test_search_nasa_Chrome3(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='donki']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='donki']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='donki']")))
        print("Precipitation button DONKI is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='donki']")))
        print("Wind button DONKI is clickable")

    def test_search_nasa_Chrome4(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='earth']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='earth']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='earth']")))
        print("Precipitation button Earth is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='earth']")))
        print("Wind button Earth is clickable")

    def test_search_nasa_Chrome5(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='eonet']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='eonet']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='eonet']")))
        print("Precipitation button Earth is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='eonet']")))
        print("Wind button Earth is clickable")

    def tearDown(self):
        self.driver.quit()
class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search_nasa_firefox1(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='apod']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='apod']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='apod']")))
        print("Precipitation button APOD is visible ")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='apod']")))
        print("Wind button APOD is clickable")

    def test_search_nasa_firefox2(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='asteroids-neows']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='asteroids-neows']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='asteroids-neows']")))
        print("Precipitation button Asteroids is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='asteroids-neows']")))
        print("Wind button Asteroids is clickable")

    def test_search_nasa_firefox3(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='donki']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='donki']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='donki']")))
        print("Precipitation button DONKI is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='donki']")))
        print("Wind button DONKI is clickable")

    def test_search_nasa_firefox4(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='earth']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='earth']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='earth']")))
        print("Precipitation button Earth is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='earth']")))
        print("Wind button Earth is clickable")

    def test_search_nasa_firefox5(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='eonet']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='eonet']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='eonet']")))
        print("Precipitation button Earth is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='eonet']")))
        print("Wind button Earth is clickable")
    def tearDown(self):
        self.driver.quit()
class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
    def test_search_nasa_Edge1(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='apod']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='apod']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='apod']")))
        print("Precipitation button APOD is visible ")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='apod']")))
        print("Wind button APOD is clickable")

    def test_search_nasa_Edge2(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='asteroids-neows']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='asteroids-neows']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='asteroids-neows']")))
        print("Precipitation button Asteroids is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='asteroids-neows']")))
        print("Wind button Asteroids is clickable")

    def test_search_nasa_Edge3(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='donki']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='donki']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='donki']")))
        print("Precipitation button DONKI is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='donki']")))
        print("Wind button DONKI is clickable")

    def test_search_nasa_Edge4(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='earth']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='earth']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='earth']")))
        print("Precipitation button Earth is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='earth']")))
        print("Wind button Earth is clickable")

    def test_search_nasa_Edge5(self):
        driver = self.driver
        driver.get('https://api.nasa.gov/')
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='eonet']")))
        time.sleep(1)  # simulate long running test

        driver.find_element(By.XPATH, "//button[@id='eonet']").click()

        # Check if the search returns any result
        assert "No results found." not in driver.page_source, "No results found in Chrome"

        try:
            assert "NASA Open APIs" in driver.title
        except AssertionError:
            print("Current Title is DIFFERENT: ", driver.title)

        print("Page title in Chrome is:", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='eonet']")))
        print("Precipitation button Earth is visible")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='eonet']")))
        print("Wind button Earth is clickable")

    def tearDown(self):
        self.driver.quit()
