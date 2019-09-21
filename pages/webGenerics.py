from selenium.webdriver import ActionChains

from pages.locGenerics import LocGenerics


class WebGenerics(LocGenerics):
    def __init__(self, driver):
        LocGenerics.__init__(self, driver)
        self.driver = driver

    def enter_word(self, loc_type, locator_val, input_val):
        ele = self.locator(loc_type, locator_val)
        ele.send_keys(input_val)

    def click_on(self, loc_type, locator_val):
        ele = self.locator(loc_type, locator_val)
        try:
            ele.click()
        except:
            self.wait(ele)
            ele.click

    def mouse_hover(self, loc_type, locator_val):
        action = ActionChains(self.driver)
        ele = self.locator(loc_type, locator_val)
        action.move_to_element(ele).perform()
