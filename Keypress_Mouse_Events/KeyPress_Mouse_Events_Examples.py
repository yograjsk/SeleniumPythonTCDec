from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

class execute1:
    def __init__(self):
        self.driver=webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
        # Implementing implicite wait
        self.driver.implicitly_wait(10)
        self.action = ActionChains(self.driver)

        self.driver.maximize_window()
        self.url= "https://opensource-demo.orangehrmlive.com/"

    def login(self):
        action = self.action
        self.driver.get(self.url)
        print(self.driver.title)
        action.send_keys_to_element(self.driver.find_element(By.XPATH,"//input[@id='txtUsername']"),"admin").perform()
        # self.driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123"+Keys.ENTER)
        # self.driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        ele1 = self.driver.find_element(By.ID, "pieLabel0")
        action.move_to_element(ele1).perform()

# common functions:



a = execute1()
a.login()
