import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

from Unittest_Example.OR import ObjectRepository
from Unittest_Example.Utilities import Utilities

class Login:

    def Login(self):
        # global pwd
        # global newUsername
        self.util = Utilities()

        # self.config = self.util.readProperties("../Unittest_Example/config.properties")
        self.config = self.util.readProperties("config.properties")
        browser = self.config["browserName"]
        timeout = int(self.config["timeout"])

        self.pwd = "Apple123"
        self.newUsername = "powernew4"

        self.browser = self.util.getBrowser(browser)
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.user_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        self.browser.implicitly_wait(timeout)

        util = Utilities()
        objRepo = ObjectRepository()

        print(">>> running setUp: login")
        self.browser.get(self.url)
        print("Launching the orangehrm ")
        print(self.browser.title)
        time.sleep(2)

        # Enhancement2 - using the object repository structure
        util.passValue("id", objRepo.username_txt_id, "admin", self.browser)  # byType, byValue, valueToPass, driver
        util.passValue("id", objRepo.password_txt_id, "admin123", self.browser)
        util.clickElement("id", objRepo.login_btn_id, self.browser)

        welcomeadmin = self.browser.find_element_by_id("welcome").is_displayed()
        print("logged in is displayed : ", welcomeadmin)
        # open the User url
        return self.browser


# l = Login()
# l.Login()
