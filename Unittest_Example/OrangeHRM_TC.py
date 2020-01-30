from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class OrangeHRM:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.url = "https://opensource-demo.orangehrmlive.com/"
        self.user_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"

    def login(self):
        # browser = self.browser
        self.browser.get(self.url)
        print("Launching the orangehrm ")
        print(self.browser.title)
        time.sleep(2)
        # login
        self.browser.find_element_by_id("txtUsername").send_keys('admin')
        self.browser.find_element_by_id("txtPassword").send_keys('admin123')
        self.browser.find_element_by_id("btnLogin").click()
        welcomeadmin = self.browser.find_element_by_id("welcome").is_displayed()
        print("logged in is displayed : ", welcomeadmin)
        # open the User url
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
            # print(counter, "role", n.text)
            # print(counter, "status", n.text)
        print("search results count:", counter)
        # print(usernames)
        # Add button
        addbutton = self.browser.find_element_by_name("btnAdd")
        addbutton.click()
        # Employees details :

        pwd = "Apple123"
        newUsername = "powernew1"
        employeesname = self.browser.find_element_by_id("systemUser_employeeName_empName")
        employeesname.send_keys("linda anderson")
        username = self.browser.find_element_by_name("systemUser[userName]")
        username.send_keys(newUsername)

        password = self.browser.find_element_by_id("systemUser_password")
        password.send_keys(pwd)
        confirmpassword = self.browser.find_element_by_name("systemUser[confirmPassword]")
        confirmpassword.send_keys(pwd)
        savebutton = self.browser.find_element_by_id("btnSave")
        savebutton.click()
        print("Username is saved ")
        time.sleep(5)
        self.browser.find_element_by_xpath("//a[contains(text(),'power')]").click()
        edit = self.browser.find_element_by_id("btnSave")
        edit.click()
        print("Editing the username ")
        self.browser.find_element_by_class_name("addbutton").click()
        print("Saved the username")

#         Delete the record
        self.browser.find_element_by_xpath("//a[text()='" + newUsername + "']//../..//input").click()
        self.browser.find_element_by_id("btnDelete").click()

# Xpath for checkbox://a[text()='fiona.grace']//../..//input
# Xpath for checkbox:
#         name = "//a[text()='" + newUsername + "']//../..//input"


web = OrangeHRM()
web.login()
