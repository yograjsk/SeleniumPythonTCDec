from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class execute1:
   #define constructor- __init__ : “__init__” is a reseved method in python classes. It is known
    # as a constructor in object oriented concepts. This method called when an object is created from
    # the class and it allow the class to initialize the attributes of a class.
    def __init__(self):
        self.driver=webdriver.Firefox(executable_path="drivers/geckodriver.exe")
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.url= "https://opensource-demo.orangehrmlive.com/"
  # write fucntions
    def login(self):
        self.driver.get(self.url)
        print(self.driver.title)
        self.driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("admin")
        #self.driver.find_element_by_xpath(//*[@id="btnLogin"])
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element(By.LINK_TEXT,"Welcome Admin").click()
        # time.sleep(3)
        # eleWelcomeLink = self.driver.find_element(By.ID,"welcome")
        wait = WebDriverWait(self.driver, 10)
        eleWelcomeLink = wait.until(EC.element_to_be_clickable((By.ID,"welcome")))
        eleWelcomeLink.click()

        # wait = WebDriverWait(self.driver, 10, poll_frequency=1,
        #                      ignored_exceptions=[NoSuchElementException,
        #                                          ElementNotVisibleException,
        #                                          ElementNotSelectableException])

        # welcomeLink = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,"Welcome ")))
        # welcomeLink.click()
        # self.driver.find_element(By.ID,"welcome").click()
        # time.sleep(3)
        # self.driver.find_element(By.LINK_TEXT, "About").click()
        # self.driver.find_element_by_id("aboutDisplayLink"). click()
        aboutLink = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,"aboutDisplayLink")))
        aboutLink.click()
        # self.driver.find_element(By.ID,"aboutDisplayLink").click()
        info = self.driver.find_element_by_name("frmSelectEmployees").text
        print(info)

   # Now call the class by defining the  object


a = execute1()
a.login()
