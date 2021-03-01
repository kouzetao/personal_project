from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

# 企业微信demo

class TestWeChat:
    # 设备初始化
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "GDB6R19725019609"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps['noReset'] = "true"
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True
        # 启动driver服务并设置隐式等待
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
    # teardown函数
    def teardown(self):
        self.driver.quit()
    # 执行操作`
    def test_addcontact(self):
        print("添加联系人")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()  # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()  #点击添加成员
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/cth").click()  # 点击手动添加
        name = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b7m") # 定位姓名输入框输入名字
        name.send_keys("新同事")
        phone = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fwi")  # 定位手机号输入框输入手机号
        phone.send_keys("12800000001")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fk9").click()  # 取消勾选
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/aj_").click()  # 点击保存
        sleep(1)
        print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")  # 定位”添加成功“的toast





