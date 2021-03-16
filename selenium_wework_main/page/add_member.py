from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember:

    def __init__(self, driver:WebDriver):
        self._driver = driver

    def add_memeber(self):
        # sendkeys name
        self._driver.find_element(By.ID, "username").send_keys("Kevin")
        pass
