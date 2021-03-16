from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_po.login import Login
from selenium_po.register import Register


# 主页page类
class Index:

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")
        self._driver.implicitly_wait(10)


    # 登录方法
    def goto_login(self):
        # click 登录
        sleep(2)
        self._driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)

    #立即注册
    def goto_register(self):
        # click 立即注册
        self._driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)


