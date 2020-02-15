import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

from Unittest_Example.OR import ObjectRepository
from Unittest_Example.Utilities import Utilities
from Unittest_Example.TC_Login import Login

class TC1_searchUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login = Login()
        cls.browser = cls.login.Login()

    def test_1_searchUserRoles(self):
        user_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        print(">>> running test1: search user")
        self.browser.get(user_url)
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

    @classmethod
    def tearDownClass(cls):
        u = Utilities()
        print("quiting the driver")
        u.closeBrowser(cls.browser)
        # cls.browser.quit()


if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/USER/PycharmProjects/sample/PageObjModelDemo/reports'))
    unittest.main()