# 封装page类
from appium import webdriver

from app.page.base_page import BasePage
from app.page.main import Main


class App(BasePage):
    def start(self):  # 启动
        if self._driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "GDB6R19725019609"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            # 启动driver服务并设置隐式等待
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)

        return self

    def restart(self): # 重启
        pass

    def stop(self):   # 停止
        pass

    def main(self) -> Main:   # main方法
        return Main(self._driver)
