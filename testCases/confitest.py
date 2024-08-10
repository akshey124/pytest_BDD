from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from datetime import datetime


@pytest.fixture()
def setfup():
    serv_obj = Service("F:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.maximize_window()
    return driver



def pytest_configure(config):
    config._metadata['Project Name'] = "Amazon"
    config._metadata['Tester'] = "Akshay    "
    config._metadata['Run Time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')



def pytest_sessionfinish(session, exitstatus):
    session.config._metadata['Environment'] = 'QA'
