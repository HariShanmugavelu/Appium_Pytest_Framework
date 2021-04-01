from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from views.base_view import BaseView
from views.echo_view import EchoView
from views.login_view import LoginView
from views.secret_view import SecretView

class HomeView(BaseView):
    ECHO_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Echo Box')
    LOGIN_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Login Screen')

    def nav_to_echo_box(self):
        self.wait_for(self.ECHO_ITEM).click()
        return EchoView(self.driver)

    def nav_to_login_screen(self):
        self.wait_for(self.LOGIN_ITEM).click()
        return LoginView(self.driver)

    def deeplink_login(self):
        self.get_url("theapp://login/alice/mypassword")
        return SecretView(self.driver)
        
