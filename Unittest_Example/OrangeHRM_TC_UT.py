from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import unittest
from Unittest_Example.Utilities import Utilities
from Unittest_Example.OR import ObjectRepository

class OrangeHRM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global pwd
        global newUsername
        cls.util = Utilities()

        cls.config = cls.util.readProperties("../Unittest_Example/config.properties")
        browser = cls.config["browserName"]
        timeout = int(cls.config["timeout"])

        # cls.browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

        cls.browser = cls.util.getBrowser(browser)
        cls.url = "https://opensource-demo.orangehrmlive.com/"
        cls.user_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        cls.browser.implicitly_wait(timeout)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()

    def setUp(self):
        util = Utilities()
        objRepo = ObjectRepository()

        print(">>> running setUp: login")
        self.browser.get(self.url)
        print("Launching the orangehrm ")
        print(self.browser.title)
        time.sleep(2)


        # Enhancement2 - using the object repository structure
        util.passValue("id", objRepo.username_txt_id, "admin", self.browser)                              #byType, byValue, valueToPass, driver
        util.passValue("id", objRepo.password_txt_id, "admin123", self.browser)
        util.clickElement("id", objRepo.login_btn_id, self.browser)

        # Enhancement 1 - created util class and using methods of it
        # util.passValue("id", "txtUsername", "admin", self.browser)                              #byType, byValue, valueToPass, driver
        # util.passValue("id", "txtPassword", "admin123", self.browser)
        # util.clickElement("id", "btnLogin", self.browser)

        # Initial line of code
        # self.browser.find_element_by_id("txtUsername").send_keys('admin')
        # self.browser.find_element_by_id("txtPassword").send_keys('admin123')
        # self.browser.find_element_by_id("btnLogin").click()



        welcomeadmin = self.browser.find_element_by_id("welcome").is_displayed()
        print("logged in is displayed : ", welcomeadmin)
        # open the User url

    def tearDown(self):
        print(">>> running tearDown: logout")
        time.sleep(2)
        self.browser.find_element_by_id("welcome").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

    def test_1_searchUserRoles(self):
        print(">>> running test1: search user")
        self.browser.get(self.user_url)
        print("User page is opened ")

        userRole = Select(self.browser.find_element_by_name("searchSystemUser[userType]"))
        userRole.select_by_visible_text("All")
        self.browser.find_element_by_id("searchBtn").click()
        time.sleep(2)
        usernames = self.browser.find_elements_by_xpath("//table[@id='resultTable']//tbody//a")
        counter = 0
        for n in usernames:
            counter += 1
            print(counter, n.text)
        print("search results count:", counter)

    def test_2_AddUsername(self):
        pwd = "Apple123"
        newUsername = "powernew4"
        print(">>> running test2: add user")
        self.browser.get(self.user_url)
        self.browser.find_element_by_name("btnAdd").click()
        self.browser.find_element_by_id("systemUser_employeeName_empName").send_keys("linda anderson" + Keys.TAB)
        self.browser.find_element_by_name("systemUser[userName]").send_keys(newUsername + Keys.TAB)
        checkValidationError = self.browser.find_element(By.CLASS_NAME, "validation-error").is_displayed()
        assert (checkValidationError == False)
        self.browser.find_element_by_id("systemUser_password").send_keys(pwd)
        self.browser.find_element_by_name("systemUser[confirmPassword]").send_keys(pwd)
        self.browser.find_element_by_id("btnSave").click()
        time.sleep(2)
        print("Username is saved ")

    def test_3_EditUser(self):
        pwd = "Apple123"
        newUsername = "powernew4"
        print(">>> running test3: edit user")
        self.browser.get(self.user_url)
        time.sleep(5)
        print("username: " + newUsername)
        self.browser.find_element_by_xpath("//a[contains(text(),'"+newUsername+"')]").click()
        edit = self.browser.find_element_by_id("btnSave")
        edit.click()
        print("Editing the username ")
        self.browser.find_element_by_class_name("addbutton").click()
        print("Saved the username")

    def test_4_DeleteUser(self):
        newUsername = "powernew4"
        print(">>> running test4: delete user")
        self.browser.get(self.user_url)
        self.browser.find_element_by_xpath("//a[text()='" + newUsername + "']//../..//input").click()
        self.browser.find_element_by_id("btnDelete").click()
        time.sleep(1)
        self.browser.find_element_by_id("dialogDeleteBtn").click()

if __name__ == "__main__":
    unittest.main()


# Xpath for checkbox://a[text()='fiona.grace']//../..//input
#         name = "//a[text()='" + newUsername + "']//../..//input"
