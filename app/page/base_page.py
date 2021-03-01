from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging

class BasePage:
    logging.basicConfig(level=logging.INFO)
    # 定义一个弹窗列表
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
    ]
    _error_num = 0  #
    _max_num = 3  # 循环查找次数
    # init函数内driver
    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    # find函数内
    def find(self, locator, value:str=None):
        logging.info(locator)
        logging.info(value)

        element:WebElement
        try:
            element = self._driver.find_element(*locator).text if isinstance(locator, tuple) else self._driver.find_element(locator, value).text
            # if isinstance(locator, tuple):
            #     element = self._driver.find_element(*locator)
            # else:
            #     element = self._driver.find_element(locator, value)
            self._error_num = 0 # 找到之后归零
            self._driver.implicitly_wait(10)  # 隐式等待恢复10秒
            return element
        except Exception as e:
            # 出现异常，将隐式等待时间缩小，快速处理弹窗
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1

            for ele in self._black_list:
                logging.info(ele)
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理弹窗后，再继续查找元素
                    return self.find(locator, value)
            raise e

    def find_and_get_text(self, locator, value:str=None):
        element:WebElement
        try:
            element_text = self._driver.find_element(*locator).text if isinstance(locator, tuple) else self._driver.find_element(locator, value).text
            # if isinstance(locator, tuple):
            #     element = self._driver.find_element(*locator)
            # else:
            #     element = self._driver.find_element(locator, value)
            self._error_num = 0 # 找到之后归零
            self._driver.implicitly_wait(10)  # 隐式等待恢复10秒
            return element_text
        except Exception as e:
            # 出现异常，将隐式等待时间缩小，快速处理弹窗
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1

            for ele in self._black_list:
                logging.info(ele)
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理弹窗后，再继续查找元素
                    return self.find(locator, value)
            raise e






