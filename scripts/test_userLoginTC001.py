import pytest

from pages.fk_user_loginpage import FK_loginPage
from pages.fk_user_homepage import FK_user_homepage

@pytest.mark.Smoke
@pytest.mark.usefixtures("test_setup")
class TestUserITC():
    def test_Userl_login_ITC_001(self): #
        driver = self.driver
        lp = FK_loginPage(driver)
        text = driver.title
        print(text)
        lp.login_fk()

    def test_User_logout_ITC_002(self): #
        driver = self.driver
        hp = FK_user_homepage(driver)
        text = driver.title
        print(text)
        hp.logout_fk()

