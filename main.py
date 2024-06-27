import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

class JobFinder:

    #Starts the Program
    def __init__(self):

        options = uc.ChromeOptions()
        self.seleniumDriver = uc.Chrome()

    def LoginToJobs(self):

        self.seleniumDriver.get("https://www.ziprecruiter.com/authn/login")
        time.sleep(5)

        self.seleniumDriver.find_element(By.ID, "email").send_keys("")
        time.sleep(5)
        self.seleniumDriver.find_element(By.ID, "password").send_keys("")
        time.sleep(5)
        button = self.seleniumDriver.find_element(By.ID, "submit_button")
        self.seleniumDriver.execute_script("arguments[0].click();", button)
        time.sleep(20)


    def EndProgram(self):
        self.seleniumDriver.quit()




JobFinder().LoginToJobs()