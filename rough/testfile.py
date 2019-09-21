import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from testdata.data import *

# dic = os.getcwd().replace("testfile.py", "").replace('\\', '/') + "/drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path="C:/Users/Ajay/PycharmProjects/AutomationFlipKart/drivers/chromedriver.exe")
driver.implicitly_wait(MID_WAIT)
driver.maximize_window()
driver.get(URL)

driver.find_element_by_xpath('(//div[@class="_39M2dM JB4AMj"]//input)[1]').send_keys(UN)
driver.find_element_by_xpath('(//div[@class="_39M2dM JB4AMj"]//input)[2]').send_keys(PW)
driver.find_element_by_xpath('//div[@class="_1avdGP"]/button').click()
web_ele = driver.find_element_by_xpath("(//div[@class=\"_1HmYoV _35HD7C\"])[2]//a//div[contains(text(),'Samsung')][contains(text(),'Black')][contains(text(),'64 GB')]//parent::div//following-sibling::div//div[contains(text(),'21,490')]")
web_ele.is_displayed()
web_ele.get_attribute("text")
text ="Anvesh"
text.__contains__("21490")
time.sleep(3)
action = ActionChains(driver)
driver.title

# driver.find_element_by_xpath('(//div[@class="dHGf8H"]/div/div/div)[1]').click()
dd_menu = '(//div[@class="dHGf8H"])[1]'
action.move_to_element(driver.find_element_by_xpath(dd_menu)).perform()
driver.find_element_by_xpath('//div[@class="_1Q5BxB"][contains(text(),"Logout")]').click()
driver.close()

driver.f