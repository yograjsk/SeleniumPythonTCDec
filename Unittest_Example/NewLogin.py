import time

from Unittest_Example.OR import ObjectRepository
from Unittest_Example.Utilities import Utilities


class NewLogin:

    def login(self):
        objRepo = ObjectRepository()
        self.util = Utilities()
        self.config = self.util.readProperties("config.properties")
        browser = self.config["browserName"]
        timeout = int(self.config["timeout"])

        self.browser = self.util.getBrowser(browser)
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.browser.implicitly_wait(timeout)


        print(">>> running setUp: login")
        self.browser.get(self.url)
        print("Launching the orangehrm ")
        print(self.browser.title)
        time.sleep(2)

        self.util.passValue("id", objRepo.username_txt_id, "admin", self.browser)                              #byType, byValue, valueToPass, driver
        self.util.passValue("id", objRepo.password_txt_id, "admin123", self.browser)
        self.util.clickElement("id", objRepo.login_btn_id, self.browser)

        welcomeadmin = self.browser.find_element_by_id("welcome").is_displayed()
        print("logged in is displayed : ", welcomeadmin)

        return self.browser
