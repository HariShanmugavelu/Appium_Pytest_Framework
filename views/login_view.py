from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from views.base_view import BaseView
from views.secret_view import SecretView

class LoginView(BaseView):
    USERNAME = (MobileBy.ACCESSIBILITY_ID, 'username')
    PASSWORD = (MobileBy.ACCESSIBILITY_ID, 'password')
    LOGIN_BUTTON = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="loginBtn"]')

    def login(self):
        self.wait_for(self.USERNAME).send_keys('alice')
        self.find(self.PASSWORD).send_keys('mypassword')
        self.find(self.LOGIN_BUTTON).click()
        return SecretView(self.driver)

    def check_login_screen(self):
        return self.wait_for(self.USERNAME).text
