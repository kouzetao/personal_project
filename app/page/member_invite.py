# 手动输入资料 page类
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class MemberInvite(BasePage):

    def addmember_by_manul(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/cth").click()  # 点击手动添加
        from app.page.contact_add import ContactAdd
        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, "//*[@class ='android.widget.Toast']").text  # 定位”添加成功“的toast
