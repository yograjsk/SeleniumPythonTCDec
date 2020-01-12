import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class OrangeHRM:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="drivers/geckodriver.exe")
        # self.url = "http://www.google.com"
        self.url = "https://opensource-demo.orangehrmlive.com/"
        # self.driver.implicitly_wait(10)


    def login(self):
        # driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        self.driver.get(self.url)
        print(self.driver.title)
        # self.driver.find_element_by_id("txtUsername").send_keys("admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element(By.NAME, "txtUsername").send_keys("admin")
        # self.driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("admin")
        # self.driver.find_element(By.XPATH, '//input[@id="txtUsername"]').send_keys("admin")

        self.driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(1)
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "Welcome ").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Welcome ')]").click()
        time.sleep(1)
        # self.driver.find_element(By.LINK_TEXT, "About").click()
        self.driver.find_element(By.XPATH, "//a[text()='About']").click()

        info = self.driver.find_element(By.ID, "frmSelectEmployees").text
        print(info)
        time.sleep(1)

        # self.driver.find_element(By.CLASS_NAME, "close").click()

    def getAttributes(self):
        empInfoEle = self.driver.find_element(By.ID, "frmSelectEmployees")
        id = empInfoEle.get_attribute("id")
        name = empInfoEle.get_attribute("name")
        font = empInfoEle.value_of_css_property("font")
        fontsize = empInfoEle.value_of_css_property("font-size")
        color = empInfoEle.value_of_css_property("color")
        print(id, name, font, fontsize, color)



o = OrangeHRM()
o.login()
o.getAttributes()
