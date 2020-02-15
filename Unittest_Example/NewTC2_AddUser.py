from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import unittest

from Unittest_Example.NewLogin import NewLogin
from Unittest_Example.Utilities import Utilities


class NewTC2_AddUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.login = NewLogin()
        self.browser = self.login.login()

    def test_addUser(self):
        self.user_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
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


    @classmethod
    def tearDownClass(self):
        u = Utilities()
        print("Quiting the browser")
        u.closeBrowser(self.browser)

if __name__ == "__main__":
    unittest.main()