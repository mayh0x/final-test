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

@given('an achiever accesses the helpdesk (2a)')
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'))
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()

    # login
    username = context.driver.find_element_by_id('login')
    password = context.driver.find_element_by_id('inputPassword')
    username.send_keys('sjy36824@eoopy.com')
    password.send_keys('abcd1234')
    context.driver.find_element_by_id('btnLogin').click()
    time.sleep(1)

    # steps
    context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul/li[2]/a/span').click()
    
@when('the achiever submits a case with the required fields filled in (2a)')
def when(context):
    while(context.driver.find_element_by_xpath('/html/body/app-root/ng-http-loader').is_displayed()):
        pass

    button = context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app-help-desk/div/app-custom-card/div/div[2]/div/app-case-list/app-new-case/app-custom-card/div/div[2]/div/app-case-form/form/div[9]/div[2]/div[2]/button')
    button.location_once_scrolled_into_view # scroll down

    case = context.driver.find_element_by_id('type')
    disp = context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app-help-desk/div/app-custom-card/div/div[2]/div/app-case-list/app-new-case/app-custom-card/div/div[2]/div/app-case-form/form/div[3]/div/div[1]/label')
    so = context.driver.find_element_by_id('so')
    browser = context.driver.find_element_by_id('browser')
    title = context.driver.find_element_by_id('title')
    desc = context.driver.find_element_by_id('description')

    case.send_keys('e')
    disp.click()
    so.send_keys('w')
    browser.send_keys('o')
    title.send_keys('test title')
    desc.send_keys('test description')

    send = context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app-help-desk/div/app-custom-card/div/div[2]/div/app-case-list/app-new-case/app-custom-card/div/div[2]/div/app-case-form/form/div[10]/button')
    send.click()

    time.sleep(1)

@then('the case stays in progress (2a)')
def then(context):
    try:
        text = ec.text_to_be_present_in_element((By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-help-desk/div/app-custom-card/div/div[2]/div/app-case-list/div/table/tbody/tr[3]/td[2]/h5/span'), 'Em andamento')
        WebDriverWait(context.driver, 5).until(text)
    except TimeoutException:
        print('Timed out waiting for page to load')
    finally:
        time.sleep(1)
        context.driver.close()