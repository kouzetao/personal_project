
# 注册页面 page类
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:

    def __init__(self, driver:WebDriver):
        self._driver = driver

    def register(self):
        sleep(2)
        self._driver.find_element(By.ID, "corp_name").send_keys("人生无限科技有限公司")
        sleep(2)
        return True
