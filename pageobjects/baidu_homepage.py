#测试页面元素,及操作

from base_page.basepage import BasePage

class Homepage(BasePage):

    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self,text):
        self.type(self.input_box,text)

    def send_submit_btn(self):
        self.submit_s(self.search_submit_btn)
