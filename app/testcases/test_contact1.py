from app.page.app import App


class TestContact:

    def setup(self):
        self.app = App() # 创建实例app
        self.main = self.app.start().main()  # 启动

    def test_addcontact(self):
        invitpage = self.main.goto_addresslist().add_member().addmember_by_manul(). \
            input_name().input_phone().click_push().click_save()

        assert '成功' in invitpage.get_toast()