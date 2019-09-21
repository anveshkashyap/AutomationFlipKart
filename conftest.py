import os
import time

import pytest
from selenium import webdriver

from testdata.data import *


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def test_setup(request):
    if request.param == "chrome":
        dic = os.getcwd().replace("conftest.py", "").replace('\\', '/') + "/drivers/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=dic)
        driver.implicitly_wait(MID_WAIT)
        driver.maximize_window()
        driver.get(URL)
        request.cls.driver = driver
        yield
        driver.close()
    if request.param == "firefox":
        dic = os.getcwd().replace("conftest.py", "").replace('\\', '/') + "/drivers/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=dic)
        driver.implicitly_wait(MID_WAIT)
        driver.maximize_window()
        driver.get(URL)
        request.cls.driver = driver
        yield
        driver.close()

