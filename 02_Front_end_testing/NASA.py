import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

# find "Google Search" field and type "NASA APIs" there
driver.find_element(By.NAME, "q").send_keys("Nasa APIs")
time.sleep(1)
# click on "Google Search" button
driver.find_element(By.NAME, "btnK").click()

# wait 2 sec, then proceed with script
time.sleep(2)

# Find and click on the Nasa APIs link
driver.find_element(By.PARTIAL_LINK_TEXT, "NASA Open APIs").click()
time.sleep(2)
assert "NASA Open APIs" in driver.title
print("NASA Open APIs Page Title is: ", driver.title)

if "NASA Open APIs" not in driver.title:
    raise Exception("Title for NASA Open APIs page is wrong!")

# Check Minimize and Maximize window functionality
driver.minimize_window()
time.sleep(1)
driver.maximize_window()
time.sleep(2)

# find information in the Menu Browse APIs
driver.find_element(By.XPATH, "//input[@id='basic-search-field-small']").send_keys("Browse APIs")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='basic-search-field-small']").clear()

# find information in the sub-menu EPIC
driver.find_element(By.XPATH, "//input[@id='search-field-big']").send_keys("EPIC")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='epic']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='search-field-big']").clear()

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

# find information in the sub-menu Exoplanet
driver.find_element(By.XPATH, "//input[@id='search-field-big']").send_keys("Exoplanet")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='exoplanet']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='search-field-big']").clear()

driver.find_element(By.XPATH, "//h2[@id='exoPlanetIntro']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//h2[@id='exoPlanetExamples']").click()
time.sleep(1)

# find information in the sub-menu Open Science Data Repository
driver.find_element(By.XPATH, "//input[@id='search-field-big']").send_keys("Open Science Data Repository")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='open-science-data-repository']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='search-field-big']").clear()

driver.find_element(By.XPATH, "//h2[contains(.,'Study')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h4[contains(.,'Example Requests:')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(.,'Study Metadata API')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//h4[contains(.,'Returns: JSON-formatted response')])[2]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(.,'Study Dataset Search API')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h4[contains(text(),'Syntax 2 (returns HTML response):')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h2[@id='other']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(text(),'Format:')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(text(),'Examples:')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h4[contains(text(),'Single Vehicle Call')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h2[contains(.,'API Requests with Python')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h2[contains(.,'Resources')]").click()
time.sleep(1)

# find information in the sub-menu Insight
driver.find_element(By.XPATH, "//input[@id='search-field-big']").send_keys("Insight")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='insight']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='search-field-big']").clear()

driver.find_element(By.XPATH,"//h1[@id='insight_weather']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//img[@src='assets/img/general/insight_photo.png']").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//h3[contains(@id,'http-request')])[3]").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//h3[contains(@id,'query-parameters')])[6]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//img[@src='./assets/insight/insight_mars_wind_rose.png']").click()
time.sleep(1)

# find information in the sub-menu Mars Rover Photos
driver.find_element(By.XPATH, "//input[@id='search-field-big']").send_keys("Mars Rover Photos")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='mars-rover-photos']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='search-field-big']").clear()

driver.find_element(By.XPATH,"//h3[contains(text(),'Rover Cameras')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(text(),'Querying by Martian sol')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//h3[contains(@id,'example-query')])[11]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(.,'Querying by Earth date')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//h3[contains(@id,'example-query')])[13]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(.,'Mission Manifest')]").click()
time.sleep(1)

# find information in the sub-menu TLE API
driver.find_element(By.XPATH, "//input[@id='search-field-big']").send_keys("TLE API")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='tle-api']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='search-field-big']").clear()

driver.find_element(By.XPATH,"//h1[contains(.,'TLE API')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[@id='tle-http-request']").click()
time.sleep(1)

driver.find_element(By.XPATH,"(//h3[contains(@id,'example-query')])[15]").click()
time.sleep(1)

# find information in the sub-menu Vesta/Moon/Mars Trek WMTS
driver.find_element(By.XPATH, "//input[@id='search-field-big']").send_keys("Vesta/Moon/Mars Trek WMTS")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='vesta-moon-mars-trek-wmts']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='search-field-big']").clear()

driver.find_element(By.XPATH,"//h1[@id='trek']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(text(),'Available Moon Mosaics')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(text(),'Available Mars Mosaics')]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//h3[contains(text(),'Available Vesta Mosaics')]").click()
time.sleep(1)

# closing the browser
driver.quit()
