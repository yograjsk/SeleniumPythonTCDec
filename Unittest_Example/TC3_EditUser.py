import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

from Unittest_Example.TC_Login import Login
from Unittest_Example.Utilities import Utilities


class TC3_EditUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login = Login()
        cls.browser = cls.login.Login()

    def test_3_EditUser(self):
        newUsername = self.login.newUsername
        print(">>> running test3: edit user")
        self.browser.get(self.user_url)
        time.sleep(5)
        print("username: " + newUsername)
        self.browser.find_element_by_xpath("//a[contains(text(),'" + newUsername + "')]").click()
        edit = self.browser.find_element_by_id("btnSave")
        edit.click()
        print("Editing the username ")
        self.browser.find_element_by_class_name("addbutton").click()
        print("Saved the username")

    @classmethod
    def tearDownClass(cls):
        u = Utilities()
        print("quiting the driver")
        u.closeBrowser(cls.browser)
        # cls.browser.quit()

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/USER/PycharmProjects/sample/PageObjModelDemo/reports'))
    unittest.main()
