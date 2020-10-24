#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#

#import time, pickle
import pytest
from pages.petfriends import MainPage
from pages.elements import ManyWebElements

def test_petfriends(web_browser):
    """ Authorize to Petfriends via cookies and create a screenshot when loginpage is successfull """
    page = MainPage(web_browser)
     #verify that the user can see the all_pets page:
    assert web_browser.current_url == 'https://petfriends1.herokuapp.com/all_pets'
    # Make the screenshot of browser window:
    page.save_screenshot('result_petfriends.png')


