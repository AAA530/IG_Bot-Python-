from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password

        options = Options()
        options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"    #chrome binary location specified here
        # options.add_argument("--start-maximized") #open Browser in maximized mode
        # options.add_argument("--no-sandbox") #bypass OS security model
        # options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome('./chromedriver.exe',options=options)
        self.driver.get('https://www.instagram.com')




if __name__ == "__main__":
    ig_bot = InstagramBot('temp','pass')