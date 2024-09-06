from selenium import webdriver
from selenium.webdriver.common.by import By

# Custom Imports
from chrome import chrome_browser
from firefox import firefox_browser
from safari import safari_browser

driver = webdriver.Chrome()
driver.get("https://www.getcalley.com/page-sitemap.xml")
driver.implicitly_wait(5)

# list to store urls
all_links = []

# iterate and store all links
tables = driver.find_elements(By.TAG_NAME, "table")

for table in tables:
    links = table.find_elements(By.TAG_NAME, "a")

    # Extrach href attributes of each links
    for link in links:
        href = link.get_attribute("href")
        if href:
            all_links.append(href)
driver.quit()


# list of browsers
browsers = ["Chrome", "Firefox", "Safari"]

for browser in browsers:
    if browser == "Chrome":
        chrome_browser.chrome_test(all_links)
    elif browser == "Firefox":
        firefox_browser.firefox_test(all_links)
    elif browser == "Safari":
        pass
        # Need An Apple device to run  this as Safari browser is not available for windows and linux
        # but if you have a Mac device, just uncomment the below function call.
        #safari_browser.safari_test(all_links)
