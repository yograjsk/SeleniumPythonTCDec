import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class handleAlerts:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        self.url = "https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"

    def handleSimpleAlert(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element(By.CLASS_NAME, "btn.btn-default").click()
        time.sleep(1)
        simAlert = driver.switch_to.alert
        print(simAlert.text)
        simAlert.accept()

    def handleConfirmationAlert(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()
        time.sleep(1)
        confAlert = driver.switch_to.alert
        print(confAlert.text)
        confAlert.dismiss()
        # alertText = driver.find_element_by_id("confirm-demo").text
        # print(alertText)
        driver.find_element(By.ID, "confirm-demo")
        print(driver.find_element(By.ID, "confirm-demo").text)
        driver.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()
        time.sleep(1)
        confAlert.accept()
        print(driver.find_element(By.ID, "confirm-demo").text)

    def handleInputAlert(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Click for Prompt Box']").click()
        time.sleep(1)
        promptAlert = driver.switch_to.alert
        print(promptAlert.text)
        promptAlert.dismiss()
        print(driver.find_element(By.ID, "prompt-demo").text)
        driver.find_element(By.XPATH, "//button[text()='Click for Prompt Box']").click()
        time.sleep(1)
        promptAlert.send_keys("Shrinivas")

        promptAlert.accept()
        print(driver.find_element(By.ID, "prompt-demo").text)


ha = handleAlerts()
ha.handleSimpleAlert()
ha.handleConfirmationAlert()
ha.handleInputAlert()