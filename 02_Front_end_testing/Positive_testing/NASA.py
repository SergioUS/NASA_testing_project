import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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

        # closing the browser

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))
# find pic with user account
