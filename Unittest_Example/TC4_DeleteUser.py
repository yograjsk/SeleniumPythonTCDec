import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

from Unittest_Example.TC_Login import Login
from Unittest_Example.Utilities import Utilities


class TC4_DeleteUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login = Login()
        cls.browser = cls.login.Login()

    def test_4_DeleteUser(self):
        newUsername = self.login.newUsername
        self.user_url = self.login.user_url
        print(">>> running test4: delete user")
        self.browser.get(self.user_url)
        self.browser.find_element_by_xpath("//a[text()='" + newUsername + "']//../..//input").click()
        self.browser.find_element_by_id("btnDelete").click()
        time.sleep(1)
        self.browser.find_element_by_id("dialogDeleteBtn").click()

    @classmethod
    def tearDownClass(cls):
        u = Utilities()
        print("quiting the driver")
        u.closeBrowser(cls.browser)
        print("quiting the driver")
        # cls.browser.quit()

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/USER/PycharmProjects/sample/PageObjModelDemo/reports'))
    unittest.main()
