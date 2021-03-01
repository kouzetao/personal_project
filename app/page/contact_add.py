# 输入资料 page类
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self):  # 输入姓名
        name = self.find(MobileBy.ID, "com.tencent.wework:id/b7m") # 定位姓名输入框输入名字
        name.send_keys("新同事")
        return self

    def input_phone(self):  # 输入手机号
        phone = self.find(MobileBy.ID, "com.tencent.wework:id/fwi")  # 定位手机号输入框输入手机号
        phone.send_keys("12800000001")
        return self

    def click_push(self):  # 取消邀请通知
        self.find(MobileBy.ID, "com.tencent.wework:id/fk9").click()  # 取消勾选
        return self

    def click_save(self):  # 点击”保存“
        self.find(MobileBy.ID, "com.tencent.wework:id/aj_").click()  # 点击保存
        from app.page.member_invite import MemberInvite
        return MemberInvite(self._driver)

