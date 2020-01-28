from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

'''
Practice:
Create the user from the url: users_url by clicking on the Add button and filling up the form
Check whether the created user is listed in the users list
If the user is available the scenario is passed else its failed
'''

class OrangeHRM:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)

        self.url = "https://opensource-demo.orangehrmlive.com"
        self.users_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"

    def login(self):
        self.driver.get(self.url)
        self.driver.find_element(By.NAME, "txtUsername").send_keys("admin")
        self.driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(2)
        logedIn = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Welcome ").is_displayed()
        print("logged in into application: ", logedIn)

    def scenario1(self):
        # self.driver.get(self.url)
        # self.driver.find_element(By.NAME, "txtUsername").send_keys("admin")
        # self.driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
        # self.driver.find_element(By.ID, "btnLogin").click()
        # time.sleep(2)
        # logedIn = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Welcome ").is_displayed()
        # print("logged in into application: ", logedIn)
        self.driver.get(self.users_url)

        userRole_dropdown = Select(self.driver.find_element(By.ID, "searchSystemUser_userType"))
        userRole_dropdown.select_by_visible_text("All")
        self.driver.find_element(By.ID, "searchBtn").click()
        time.sleep(2)
        usernames = self.driver.find_elements(By.XPATH, "//table[@id='resultTable']//tbody//a")

        counter = 0
        for n in usernames:
            counter += 1
            print(counter, "username", n.text)
            # print(counter, "role", n.text)
            # print(counter, "status", n.text)
        print("search results count:", counter)
        # print(usernames)

    def scenario_Upload(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
        self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/uploadTestFile/importData(2).csv")
        # uploadFile = self.driver.find_element(By.ID, "pimCsvImport_csvFile")
        # uploadFile.send_keys("C:/uploadTestFile/importData(2).csv")
        self.driver.find_element(By.ID, "btnSave").click()
        time.sleep(5)
        msg = self.driver.find_element(By.CLASS_NAME, "inner").text
        print(msg)

    def scenario_Download(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
        self.driver.find_element(By.CLASS_NAME, "download").click()
        time.sleep(5)
        # msg = self.driver.find_element(By.CLASS_NAME, "inner").text
        # print(msg)



o = OrangeHRM()
# o.scenario1()
o.login()
o.scenario_Upload()
o.scenario_Download()
