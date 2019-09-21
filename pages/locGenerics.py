from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LocGenerics():
    def __init__(self, driver):
        self.driver = driver
    
    def locator(self, loc_type, locator_val):
        if loc_type == "id":
            web_ele = self.driver.find_element_by_id(locator_val)
        if loc_type == "class":
            web_ele = self.driver.find_element_by_class_name(locator_val)
        if loc_type == "name":
            web_ele = self.driver.find_element_by_name(locator_val)
        if loc_type == "tagname":
            web_ele = self.driver.find_element_by_tag_name(locator_val)
        if loc_type == "css":
            web_ele = self.driver.find_element_by_css_selector(locator_val)
        if loc_type == "linktext":
            web_ele = self.driver.find_element_by_link_text(locator_val)
        if loc_type == "partiallinktext":
            web_ele = self.driver.find_element_by_partial_link_text(locator_val)
        if loc_type == "xpath":
            web_ele = self.driver.find_element_by_xpath(locator_val)
        return web_ele
    
    def mul_locator(self, loc_type, locator_val):
        if loc_type == "id":
            web_ele = self.driver.find_elements_by_id(locator_val)
        if loc_type == "class":
            web_ele = self.driver.find_elements_by_class_name(locator_val)
        if loc_type == "name":
            web_ele = self.driver.find_elements_by_name(locator_val)
        if loc_type == "tagname":
            web_ele = self.driver.find_elements_by_tag_name(locator_val)
        if loc_type == "css":
            web_ele = self.driver.find_elements_by_css_selector(locator_val)
        if loc_type == "linktext":
            web_ele = self.driver.find_elements_by_link_text(locator_val)
        if loc_type == "partiallinktext":
            web_ele = self.driver.find_elements_by_partial_link_text(locator_val)
        if loc_type == "xpath":
            web_ele = self.driver.find_elements_by_xpath(locator_val)
        return web_ele

    def wait(self, ele):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.driver.find_element_by_xpath(ele)))
