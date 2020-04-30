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

        self.login()

        self.base_url = 'https://www.instagram.com'

    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(3) #wait till site gets load

        self.driver.find_element_by_name('username').send_keys(self.username)

        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()

        time.sleep(2)

    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,user))

    def follow_user(self,user):
        self.nav_user(user)

        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        
        follow_button.click()


if __name__ == "__main__":
    ig_bot = InstagramBot('user','password')
    ig_bot.follow_user('gigihadid')