from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://www.google.co.in/search?sca_esv=565250116&q=pandas&tbm=isch&source=lnms&sa=X&ved=2ahUKEwilo8rxtKmBAxWwbmwGHXW5DmoQ0pQJegQICBAB&biw=1440&bih=416&dpr=2")
time.sleep(2)

while True:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    new_heigth = driver.execute_script("return document.body.scrollHeight")
    if height == new_heigth:
        break
    
