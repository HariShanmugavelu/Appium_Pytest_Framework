from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from views.base_view import BaseView

class EchoView(BaseView):
    MESSAGE_INPUT = (MobileBy.ACCESSIBILITY_ID, 'messageInput')
    SAVE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn')
    MESSAGE_LABEL = (MobileBy.XPATH, '//android.widget.TextView[@content-desc="Hello"]')

    def save_message(self, message):
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        self.find(self.SAVE_BUTTON).click()

    def read_message(self):
        try:
            return self.wait_for(self.MESSAGE_LABEL).text
        except TimeoutException:
            return None

    def nav_back(self):
        from views.home_view import HomeView
        self.driver.back()
        return HomeView(self.driver)
