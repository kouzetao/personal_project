from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class AddMember:

    def __init__(self, driver:WebDriver):
        self._driver = driver

    def add_memeber(self):
        # send keys name
        sleep(3)
        self._driver.find_element(By.ID, "username").send_keys("Kevin")
        self._driver.find_element(By.ID, "memberAdd_acctid").send_keys("Kevin")
        self._driver.find_element(By.ID, "memberAdd_phone").send_keys("11111111111")
        self._driver.find_element(By.NAME, "sendInvite").click()
        self._driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(3)
        return True
    def get_member(self):
        elements = self._driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:th-chile(2)")
        list = []
        for element in elements:
            list.append(element.get_attribute("title"))

        return list
