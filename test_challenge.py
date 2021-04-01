from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from os import path
import time

from views.base_view import BaseView

# Test 1: test login works
def test_login_works(home):
    login = home.nav_to_login_screen()
    secret = login.login()
    assert secret.read_message() == 'You are logged in as alice'


# # Test 2: test logout works
def test_logout_works(home):
    secret = home.deeplink_login()
    assert secret.read_message() == 'You are logged in as alice'
    login = secret.logout()
    assert login.check_login_screen() == 'Username'

