# import requests
# from bs4 import BeautifulSoup

# data = requests.get("https://www.youtube.com/watch?v=0uiPOxUcLgg&list=PLc20sA5NNOvrsn3a78ewy2VTCXVV47NB4&index=5")

# soup = BeautifulSoup(data.text,"lxml")
# # print(soup.find(id="description"))
# print(soup)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Path to the chromedriver executable
service = Service('C:/Users/Asus/Downloads/chrome-win64/chrome-win64/chrome.exe')

# Set up the driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open YouTube video URL
video_url = 'https://www.youtube.com/watch?v=3SdiUH7hoCc&list=PLc20sA5NNOvrsn3a78ewy2VTCXVV47NB4&index=10'
driver.get(video_url)

# Give the page some time to 
print("loading page...")
driver.implicitly_wait(5)  # Adjust as necessary
print("page loaded successfully")
# Get the page source
page_source = driver.page_source

# Close the driver
driver.quit()

# Print the page source
print("worked here")
print(page_source)
