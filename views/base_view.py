from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseView(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def get_url(self, URL):
        self.driver.execute_script('mobile: deepLink',{
            'url': 'theapp://login/alice/mypassword',
            'package': 'io.cloudgrey.the_app',
            'waitForLaunch': False
        })

    