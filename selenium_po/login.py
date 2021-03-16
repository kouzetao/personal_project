from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_po.register import Register


# 登录页面 page类
class Login:
    # 给driver指定WebDriver类型
    def __init__(self, driver:WebDriver):
        self._driver = driver

    # 扫码
    def saoma(self):
        pass

    # 企业注册
    def goto_register(self):
        # click 企业注册
        self._driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)

