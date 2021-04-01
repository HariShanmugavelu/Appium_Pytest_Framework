from appium import webdriver
from os import path
import pytest
from views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
ANDROID_APP = path.join(CUR_DIR, 'TheApp.apk')
IOS_APP = path.join(CUR_DIR,'TheApp.app')
APPIUMS = ['https://jp-tyo.headspin.io:7014/v0/e4d1c9ebac3643d98b8a1f7c6e4af316/wd/hub', 'https://jp-tyo.headspin.io:7014/v0/e4d1c9ebac3643d98b8a1f7c6e4af316/wd/hub']

ANDROID_CAPS = [{
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'appPackage': 'io.cloudgrey.the_app',
    'appActivity': 'io.cloudgrey.the_app.MainActivity',
    'deviceName': 'Pixel 3a',
    'udid': '98KAY15CRV',
    'headspin:capture.video': True,
    'headspin:autoDownloadChromedriver': True,
}, {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'appPackage': 'io.cloudgrey.the_app',
    'appActivity': 'io.cloudgrey.the_app.MainActivity',
    'deviceName': 'SO-01K',
    'udid': 'BH9029X391',
    'headspin:capture.video': True,
    'headspin:autoDownloadChromedriver': True,
}]

IOS_CAPS = {
    'platformName': 'iOS',
    'platformVersion':'13.6',
    'automationName': 'XCUITest',
    'deviceName': 'iPhone 11',
    'app': IOS_APP
}

def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android')

@pytest.fixture
def worker_num(worker_id):
    # 'master', 'gw1', 'gw2' 
    if worker_id == 'master':
        worker_id = 'gw0'
    return int(worker_id[2:])

@pytest.fixture
def server(worker_num):
    if worker_num >= len(APPIUMS):
        raise Exception('Too many workers for the number of Appium servers')
    return APPIUMS[worker_num]

@pytest.fixture
def caps(platform, worker_num):
    cap_set = ANDROID_CAPS if platform == 'android' else IOS_CAPS
    if worker_num >= len(cap_set):
        raise Exception('Too many workers for the number of caps')
    return cap_set[worker_num]

@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['headspin', 'android']:
        raise ValueError('--platform value must be headspin or android')
    return plat

@pytest.fixture
def driver(server, caps, platform):
    driver = webdriver.Remote(server, caps)
    driver._platform = platform
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return HomeView(driver)
