from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import unittest

from Unittest_Example.NewLogin import NewLogin
from Unittest_Example.Utilities import Utilities


class NewTC3_EditUser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.login = NewLogin()
        self.browser = self.login.login()

    def test_editUser(self):
        # pwd = "Apple123"
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

    @classmethod
    def tearDownClass(self):
        u = Utilities()
        print("Quiting the browser")
        u.closeBrowser(self.browser)


if __name__ == "__main__":
    unittest.main()