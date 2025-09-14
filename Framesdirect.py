
# Libraries Used
import csv
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Step 1 - Configuration and Data Fetching
# Setup Selenium and WebDriver
print("Setting up webdriver...")
chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
chrome_option.add_argument("--window-size=1920,3000")
chrome_option.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.265 Safari/537.36"
)
print("done stting up..")

# Install the chrome driver (This is a one time thing)
print("Installing Chrome WD")
service = Service(ChromeDriverManager().install())
print("Final Setup")
driver = webdriver.Chrome(service=service, options=chrome_option)
print("Done")

# Make connection and get URL content
url = "https://www.framesdirect.com/eyeglasses/"
print(f"Visting {url} page")
driver.get(url)

# Further instruction: wait for JS to load the files
try:
    print("Waiting for product tiles to load")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'catalog-page'))
    )
    print("Done...Proceed to parse the data")
except (TimeoutError, Exception) as e:
    print(f"Error waiting for {url}: {e}")
    driver.quit()
    print("Closed")
