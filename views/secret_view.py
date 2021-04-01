from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from views.base_view import BaseView


class SecretView(BaseView):
    LOGOUT_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[@text="Logout"]')
    MESSAGE_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@text="You are logged in as alice"]')

    def read_message(self):
        try:
            return self.wait_for(self.MESSAGE_LABEL).text
        except TimeoutException:
            return None

    def logout(self):
        self.find(self.LOGOUT_BUTTON).click()
        from views.login_view import LoginView
        return LoginView(self.driver)
