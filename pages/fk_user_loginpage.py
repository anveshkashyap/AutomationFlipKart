from pages.webGenerics import WebGenerics
from testdata.data import *


class FK_loginPage(WebGenerics):
    def __init__(self, driver):
        WebGenerics.__init__(self, driver)
        self.driver = driver
        self.user_name_xpath = '(//div[@class="_39M2dM JB4AMj"]//input)[1]'
        self.password_xpath = '(//div[@class="_39M2dM JB4AMj"]//input)[2]'
        self.login_button_xpath = '//div[@class="_1avdGP"]/button'


    def login_fk(self):
        self.enter_word("xpath", self.user_name_xpath, UN)
        self.enter_word("xpath", self.password_xpath, PW)
        self.click_on("xpath", self.login_button_xpath)






