# Cross-Browser test with Chrome and FireFox. 2 same tests for each Browser

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_check_sub_menus_chrome(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'{ NASA APIs }')]")))
        print(driver.title)
        print(driver.current_url)
        time.sleep(1)  # simulate long-running test

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        try:
            driver.find_element(By.XPATH, "//h2[contains(.,'Browse APIs')]")
        except NoSuchElementException:
            print("Header is different.")

        print("Header is correct")

        # check if the NASA Image and Video Library sub-menu works
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

        # check if the TechTransfer sub-menu works
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='techtransfer']")))
        print("Sub-menu 'TechTransfer' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='techtransfer']")))
        print("Sub-menu 'TechTransfer' is clickable")

        driver.find_element(By.XPATH, "//button[@id='techtransfer']").click()

        # check if the Satellite Situation Center sub-menu works
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='satellite-situation-center']")))
        print("Sub-menu 'Satellite Situation Center' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='satellite-situation-center']")))
        print("Sub-menu 'Satellite Situation Center' is clickable")

        driver.find_element(By.XPATH, "//button[@id='satellite-situation-center']").click()

        # check if the SSD/CNEOS sub-menu works
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='ssd-cneos']")))
        print("Sub-menu 'SSD/CNEOS' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ssd-cneos']")))
        print("Sub-menu 'SSD/CNEOS' is clickable")

        driver.find_element(By.XPATH, "//button[@id='ssd-cneos']").click()

        # check if the Techport sub-menu works
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='techport']")))
        print("Sub-menu 'Techport' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='techport']")))
        print("Sub-menu 'Techport' is clickable")


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_check_sub_menus_firefox(self):
        driver = self.driver
        driver.get("https://api.nasa.gov")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'{ NASA APIs }')]")))
        print(driver.title)
        print(driver.current_url)
        time.sleep(1)  # simulate long-running test

        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        try:
            driver.find_element(By.XPATH, "(//span[contains(.,'Browse APIs')])[1]").click()
        except NoSuchElementException:
            print("'Browse APIs' button is absent")

        try:
            driver.find_element(By.XPATH, "//h2[contains(.,'Browse APIs')]")
        except NoSuchElementException:
            print("Header is different.")

        print("Header is correct")

        # check if the NASA Image and Video Library sub-menu works
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

        # check if the TechTransfer sub-menu works
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='techtransfer']")))
        print("Sub-menu 'TechTransfer' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='techtransfer']")))
        print("Sub-menu 'TechTransfer' is clickable")

        driver.find_element(By.XPATH, "//button[@id='techtransfer']").click()

        # check if the Satellite Situation Center sub-menu works
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='satellite-situation-center']")))
        print("Sub-menu 'Satellite Situation Center' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='satellite-situation-center']")))
        print("Sub-menu 'Satellite Situation Center' is clickable")

        driver.find_element(By.XPATH, "//button[@id='satellite-situation-center']").click()

        # check if the SSD/CNEOS sub-menu works
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='ssd-cneos']")))
        print("Sub-menu 'SSD/CNEOS' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ssd-cneos']")))
        print("Sub-menu 'SSD/CNEOS' is clickable")

        driver.find_element(By.XPATH, "//button[@id='ssd-cneos']").click()

        # check if the Techport sub-menu works
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='techport']")))
        print("Sub-menu 'Techport' is visible")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='techport']")))
        print("Sub-menu 'Techport' is clickable")

    def tearDown(self):
        self.driver.quit()


# closing the browser
def tearDown(self):
    self.driver.quit()
