from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.support.select import Select
import time
from Unittest_Example.NewLogin import NewLogin
from Unittest_Example.Utilities import Utilities


class NewTC1_SearchUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.login = NewLogin()
        self.browser = self.login.login()

    def test_searchUser(self):
        self.user_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
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

    @classmethod
    def tearDownClass(self):
        u = Utilities()
        print("Quiting the browser")
        u.closeBrowser(self.browser)


if __name__ == "__main__":
    unittest.main()
