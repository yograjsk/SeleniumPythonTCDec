import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Unittest_Example.TC_Login import Login
from Unittest_Example.Utilities import Utilities
import time

class TC2_AddUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        login = Login()
        cls.browser = login.Login()

    def test_2_AddUsername(self):
        newUsername = "powernew4"
        pwd = "Apple123"

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
    def tearDownClass(cls):
        u = Utilities()
        print("quiting the driver")
        u.closeBrowser(cls.browser)
        # cls.browser.quit()

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/USER/PycharmProjects/sample/PageObjModelDemo/reports'))
    unittest.main()

