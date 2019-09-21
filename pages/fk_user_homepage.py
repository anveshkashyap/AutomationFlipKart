import time

from selenium.webdriver.common.keys import Keys

from pages.webGenerics import WebGenerics


class FK_user_homepage(WebGenerics):
    def __init__(self, driver):
        WebGenerics.__init__(self, driver)
        self.driver = driver
        self.user_dropDown_menu_xpath = '(//div[@class="dHGf8H"])[1]/div'
        self.logout_link_xpath = '//div[@class="_1Q5BxB"][contains(text(),"Logout")]'
        self.searchBox_name = "q"
        self.serach_button_xpath = '//button'
        self.item_xpath = "//div[contains(text(),'Samsung Galaxy A50 (Black, 64 GB)')]"

    def search_item(self, input_val):
        self.enter_word("name", self.searchBox_name, input_val+Keys.ENTER)


    def logout_fk(self):
        self.mouse_hover("xpath", self.user_dropDown_menu_xpath)
        self.click_on("xpath", self.logout_link_xpath)
