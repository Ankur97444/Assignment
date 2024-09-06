import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By



# url, username & password
site_url =  "https://demo.dealsdray.com/"
username = "prexo.mis@dealsdray.com"
password = "prexo.mis@dealsdray.com"

# file path
file = os.getcwd()

serv_obj = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=serv_obj)

driver.get(site_url)
driver.maximize_window()


# Enter username
driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "username").send_keys(username)

# Enter password
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys(password)

# wait
time.sleep(3)

# submit
driver.find_element(By.CLASS_NAME, "MuiButton-root").click()

# wait for the page to load
time.sleep(3)

driver.find_element(By.CLASS_NAME, "compactNavItem").click()
driver.find_element(By.CSS_SELECTOR, "a[href='/mis/orders']").click()

# wait
time.sleep(3)

driver.find_element(By.CLASS_NAME, "MuiBox-root").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[2]/button").click()

# upload file
time.sleep(3)
upload_file = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/input")
upload_file.send_keys(f"{file}/demo-data.xlsx")

# submit file
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/div[3]/button").click()

# validate upload
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[3]/button").click()

# wait for alert & accept
time.sleep(3)
driver.switch_to.alert.accept()

# screenshot
timestamp = time.strftime("%y-%m-%d-%H-%M-%S")
screenshot_file = f"{file}/Screenshot-{timestamp}.png"
driver.save_full_page_screenshot(screenshot_file)

time.sleep(2)
driver.quit()




