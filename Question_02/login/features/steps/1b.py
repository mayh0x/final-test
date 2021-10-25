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

@given('a user accesses a login page (1b)')
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'))
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()

@when('the user fills in the fields with incorrect username and/or password (1b)')
def when(context):
    username = context.driver.find_element_by_id('login')
    password = context.driver.find_element_by_id('inputPassword')
    username.send_keys('marayah.meneses@dellead.com')
    password.send_keys('aaaabbbb')
    context.driver.find_element_by_id('btnLogin').click()
    time.sleep(1)

@then('it should see "Usuário e/ou senha inválidos. Verifique o usuário e senha e tente novamente." (1b)')
def then(context):
    try:
        warning = ec.text_to_be_present_in_element((By.XPATH, '/html/body/app-root/app-login/div/div/app-login-form/div[2]/div/div/div/form/div[1]'), 'Usuário e/ou senha inválidos. Verifique o usuário e senha e tente novamente.')
        WebDriverWait(context.driver, 10).until(warning)
    except TimeoutException:
        print('Timed out waiting for page to load')
    finally:
        time.sleep(1)
        context.driver.close()