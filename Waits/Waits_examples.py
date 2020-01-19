from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

class execute1:
    def __init__(self):
        self.driver=webdriver.Firefox(executable_path="drivers/geckodriver.exe")
        # Implementing implicite wait
        self.driver.implicitly_wait(10)

        # self.driver.maximize_window()
        self.url= "https://opensource-demo.orangehrmlive.com/"

    def login(self):
        self.driver.get(self.url)
        print(self.driver.title)
        self.driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

        # Explicite wait example code
        # wait = WebDriverWait(self.driver, 10)
        # welcome = wait.until(EC.element_to_be_clickable((By.ID,"welcome")))
        # welcome.click()
        # about = wait.until(EC.element_to_be_clickable((By.ID,"aboutDisplayLink")))
        # about.click()

        # Fluent wait example
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        welcome = wait.until(EC.element_to_be_clickable((By.ID, "welcome")))
        welcome.click()
        about = wait.until(EC.element_to_be_clickable((By.ID,"aboutDisplayLink")))
        about.click()

        info = self.driver.find_element_by_name("frmSelectEmployees").text
        print(info)

a = execute1()
a.login()
