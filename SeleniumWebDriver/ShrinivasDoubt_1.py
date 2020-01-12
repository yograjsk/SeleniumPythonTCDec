import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class OrangeHRM:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")
        # >> Always access the file via the relative path of the file location like the line above
        # >> Avoid absolute path for any file in below manner.
        # self.driver = webdriver.Firefox(executable_path="C:\Users\USER\PycharmProjects\DecPythonBatch\SeleniumWebDriver\drivers\geckodriver.exe")
        # self.url = "http://www.google.com"
        self.url = "https://opensource-demo.orangehrmlive.com/"
        # self.driver.implicitly_wait(10)

    def login(self):
         # driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
         self.driver.get(self.url)
         print(self.driver.title)
        # self.driver.find_element_by_id("txtUsername").send_keys("admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
         self.driver.find_element(By.NAME, "txtUsername").send_keys("admin")
         self.driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
         self.driver.find_element(By.ID, "btnLogin").click()
         time.sleep(2)
         self.driver.find_element(By.PARTIAL_LINK_TEXT, "Welcome ").click()

         #  time.sleep(2)
         self.driver.find_element(By.LINK_TEXT, "About").click()
         info = self.driver.find_element(By.ID, "frmSelectEmployees").text
         print(info)

o = OrangeHRM()
o.login()


