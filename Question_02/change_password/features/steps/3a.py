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

@given('a user accesses the profile page (3a)')
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'))
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()

    # login
    username = context.driver.find_element_by_id('login')
    password = context.driver.find_element_by_id('inputPassword')
    username.send_keys('marayah.meneses@dellead.com')
    password.send_keys('abcd1234')
    context.driver.find_element_by_id('btnLogin').click()
    time.sleep(1)

    # steps
    context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[3]/li[1]/a').click()

@when('the user clicks "Mudar senha", fills in the fields and submits (3a)')
def when(context):
    while(context.driver.find_element_by_xpath('/html/body/app-root/ng-http-loader').is_displayed()):
        pass

    button = context.driver.find_element_by_id('change')
    button.location_once_scrolled_into_view # scroll down

    context.driver.find_element_by_id('change').click()
    input1 = context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app-profile/div/div/app-custom-card[2]/div/div[2]/div/form/div[4]/div/div[1]/div/input')
    input2 = context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app-profile/div/div/app-custom-card[2]/div/div[2]/div/form/div[4]/div/div[2]/div/input')
    input1.send_keys('abcd1234')
    input2.send_keys('abcd1234')
    send = context.driver.find_element_by_id('save')
    send.click()

@then('it should see "Perfil atualizado!" (3a)')
def then(context):
    try:
        success = ec.text_to_be_present_in_element((By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-alert-system/div/div/div[1]'), 'Perfil atualizado!')
        WebDriverWait(context.driver, 10).until(success)
    except TimeoutException:
        print('Timed out waiting for page to load')
    finally:
        time.sleep(1)
        context.driver.close()