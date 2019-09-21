import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.fk_user_homepage import FK_user_homepage
from pages.fk_user_loginpage import FK_loginPage

@pytest.mark.FTC
@pytest.mark.usefixtures("test_setup")
class TestUserSearchFTC():
    def test_User_search_FTC_001(self): #
        driver = self.driver
        lp = FK_loginPage(driver)
        lp.login_fk() # login as a user
        hp = FK_user_homepage(driver) # creating object of homepage
        hp.search_item("samsung a50") # searching for an item.
        time.sleep(10)
        # wait = WebDriverWait(driver, 15)
        # ele = driver.find_element_by_xpath("//div[contains(text(), 'Samsung Galaxy A50 (Black, 64 GB)')]")
        # wait.until(expected_conditions.visibility_of_element_located(ele))
        print(driver.title)
        hp.logout_fk()


