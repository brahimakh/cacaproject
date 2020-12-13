from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = webdriver.Chrome("/Users/brahim/Downloads/chromedriver 3")
driver.get("https://www.fnac.com/Console-Sony-PS5-Edition-Standard/a14119956/w-4#omnsearchpos=1")

delay = 30 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/section/ul[2]/li/div/div[1]/div[1]/div[1]/div/p")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")