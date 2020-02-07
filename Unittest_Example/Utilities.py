from selenium import webdriver
from selenium.webdriver.common.by import By


class Utilities:

    def getByType(self, byType):
        if byType is "id":
            return By.ID
        elif byType is "class":
            return By.CLASS_NAME
        elif byType is "name":
            return By.NAME
        elif byType is "css":
            return By.CSS_SELECTOR
        elif byType is "linkText":
            return By.LINK_TEXT
        elif byType is "partLinkText":
            return By.PARTIAL_LINK_TEXT
        elif byType is "xpath":
            return By.XPATH

    def clickElement(self, byType, byValue, driver):
        u = Utilities()
        driver.find_element(u.getByType(byType), byValue).click()

        # if byType is "id":
        #     driver.find_element(By.ID, byValue).click()
        # elif byType is "class":
        #     driver.find_element(By.CLASS_NAME, byValue).click()
        # elif byType is "name":
        #     driver.find_element(By.NAME, byValue).click()
        # elif byType is "css":
        #     driver.find_element(By.CSS_SELECTOR, byValue).click()
        # elif byType is "linkText":
        #     driver.find_element(By.LINK_TEXT, byValue).click()
        # elif byType is "partLinkText":
        #     driver.find_element(By.PARTIAL_LINK_TEXT, byValue).click()
        # elif byType is "xpath":
        #     driver.find_element(By.XPATH, byValue).click()
        # # self.driver.find_element_by_id("btnLogin").click()

    def passValue(self, byType, byValue, valueToPass, driver):
        u = Utilities()
        driver.find_element(u.getByType(byType), byValue).send_keys(valueToPass)
        # if byType is "id":
        #     driver.find_element(By.ID, byValue).send_keys(valueToPass)
        # elif byType is "class":
        #     driver.find_element(By.CLASS_NAME, byValue).send_keys(valueToPass)
        # elif byType is "name":
        #     driver.find_element(By.NAME, byValue).send_keys(valueToPass)
        # elif byType is "css":
        #     driver.find_element(By.CSS_SELECTOR, byValue).send_keys(valueToPass)
        # elif byType is "linkText":
        #     driver.find_element(By.LINK_TEXT, byValue).send_keys(valueToPass)
        # elif byType is "partLinkText":
        #     driver.find_element(By.PARTIAL_LINK_TEXT, byValue).send_keys(valueToPass)
        # elif byType is "xpath":
        #     driver.find_element(By.XPATH, byValue).send_keys(valueToPass)

    def readProperties(self, propPath):
        properties = {}

        with open(propPath, 'r') as f:
            for line in f:
                lineText = line.rstrip()
                if ("=" not in lineText or lineText.startswith("#")): continue
                k, v = lineText.split("=",1)
                properties[k] = v
        print(properties)
        return properties

    def getBrowser(self, browserName):
        if browserName == "Chrome":
            self.browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        elif browserName == "Firefox":
            self.browser = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
        elif browserName == "IE":
            self.browser = webdriver.Ie(executable_path="../drivers/IEDriverServer_64.exe")
        else:
            self.browser = None
        # self.browser.implicitly_wait(60)
        return self.browser





'''
properties file info:

key=value   pair

'''