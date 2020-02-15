from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import unittest

from Unittest_Example.NewLogin import NewLogin
from Unittest_Example.Utilities import Utilities


class NewTC4_DeleteUser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.login = NewLogin()
        self.browser = self.login.login()

    def test_deleteUser(self):
        newUsername = "powernew4"
        print(">>> running test4: delete user")
        self.browser.get(self.user_url)
        self.browser.find_element_by_xpath("//a[text()='" + newUsername + "']//../..//input").click()
        self.browser.find_element_by_id("btnDelete").click()
        time.sleep(1)
        self.browser.find_element_by_id("dialogDeleteBtn").click()

    @classmethod
    def tearDownClass(self):
        u = Utilities()
        print("Quiting the browser")
        u.closeBrowser(self.browser)


if __name__ == "__main__":
    unittest.main()