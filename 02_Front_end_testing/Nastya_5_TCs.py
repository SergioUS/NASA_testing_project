# Cross-Browser test with Chrome and FireFox. 2 same tests for each Browser

from selenium.common.exceptions import NoSuchElementException
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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


# closing the browser
def tearDown(self):
    self.driver.quit()
