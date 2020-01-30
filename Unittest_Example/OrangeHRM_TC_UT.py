from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import unittest


class OrangeHRM(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        global pwd
        global newUsername

        pwd = "Apple123"
        newUsername = "powernew1"

        cls.browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.url = "https://opensource-demo.orangehrmlive.com/"
        cls.user_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()

    def setUp(self):
        print(">>> running setUp: login")
        self.browser.get(self.url)
        print("Launching the orangehrm ")
        print(self.browser.title)
        time.sleep(2)
        self.browser.find_element_by_id("txtUsername").send_keys('admin')
        self.browser.find_element_by_id("txtPassword").send_keys('admin123')
        self.browser.find_element_by_id("btnLogin").click()
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
        print(">>> running test2: add user")
        self.browser.get(self.user_url)
        self.browser.find_element_by_name("btnAdd").click()
        self.browser.find_element_by_id("systemUser_employeeName_empName").send_keys("linda anderson")
        self.browser.find_element_by_name("systemUser[userName]").send_keys(newUsername)
        self.browser.find_element_by_id("systemUser_password").send_keys(pwd)
        self.browser.find_element_by_name("systemUser[confirmPassword]").send_keys(pwd)
        self.browser.find_element_by_id("btnSave").click()
        print("Username is saved ")

    def test_3_EditUser(self):
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