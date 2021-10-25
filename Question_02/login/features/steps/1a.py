from behave import *
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)

@given('a user accesses a login page (1a)')
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'))
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()

@when('the user submits their data with correct username and password (1a)')
def when(context):
    username = context.driver.find_element_by_id('login')
    password = context.driver.find_element_by_id('inputPassword')
    username.send_keys('marayah.meneses@dellead.com')
    password.send_keys('abcd1234')
    context.driver.find_element_by_id('btnLogin').click()
    time.sleep(1)

@then('it must be redirected to a logged area (1a)')
def then(context):
    try:
        element = ec.presence_of_element_located((By.ID, 'user-name'))
        WebDriverWait(context.driver, 10).until(element)
    except TimeoutException:
        print('Timed out waiting for page to load')
    finally:
        time.sleep(1)
        context.driver.close()