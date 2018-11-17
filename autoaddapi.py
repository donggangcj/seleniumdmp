#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : autoaddapi.py
@Author: donggangcj
@Date  : 2018/11/14
@Desc  : 
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
Auto add the test api to dmp
---------------------------
"""
from random import randrange

from selenium import webdriver


def autoaddjob(path='test.txt', sleep_time=2):
    """
    Auto add the api to the dmp
    :param path:the data path
    :param time:the sleep time
    """
    browser = webdriver.Chrome()
    #  implict wait 10 second because ajax
    browser.implicitly_wait(10)
    browser.get('http://10.138.228.202:81/gateway/createApi')
    browser.find_element_by_css_selector('div.mb10 input.dao-control').send_keys('admin')
    browser.find_element_by_css_selector('div.mb20 input.dao-control').send_keys('dangerous')
    browser.find_element_by_class_name('blue').click()
    with open(path) as f:
        for item in f.readlines():
            api = item.split()
            time.sleep(sleep_time)
            browser.find_elements_by_partial_link_text('API')[1].click()

            # api1 = ('testtest', '/cosmo/test/test')

            # WebDriverWait(browser, 20).until(
            #     expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'button.dao-btn'))
            # )
            browser.find_element_by_css_selector('button.dao-btn').click()
            # WebDriverWait(browser, 20).until(
            #     expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'input'))
            # )
            browser.find_elements_by_css_selector('input')[0].send_keys(api[0])
            browser.find_elements_by_css_selector('input')[1].send_keys(api[1])
            browser.find_element_by_css_selector('div.dao-setting-section a').click()
            browser.find_elements_by_css_selector('div.dao-setting-content span.dao-switch-core')[1].click()

            browser.find_element_by_css_selector('div.el-input--suffix input').click()
            index = randrange(2)
            time.sleep(sleep_time)
            browser.find_elements_by_css_selector('li.el-select-dropdown__item')[index].click()
            browser.find_element_by_css_selector('div.dao-setting-content button').click()
