from selenium.webdriver.common.by import By
from elements.button import Button
from elements.text import Text
from pages.base_form import BaseForm

class AlertsPage(BaseForm):
    name = "alerts page"
    def __init__(self):
        super().__init__()
        self.name = "alerts page"
        self.alerts_form = Text((By.XPATH, "//*[@id='javascriptAlertsWrapper']"), "alertsform")
        self.button_to_see_alert = Button((By.XPATH, "//*[@id='alertButton']"), "button to see alert")
        self.unique_element = self.button_to_see_alert
        self.confirm_box_button = Button((By.XPATH, "//*[@id='confirmButton']"), "confirm box")
        self.confirm_result = Text((By.XPATH, "//*[@id='confirmResult']"), "confirm result")
        self.prompt_box_button = Button((By.XPATH, "//*[@id='promtButton']"), "prompt box")
        self.random_name = Text((By.XPATH, "//*[@id='promptResult']"), "random name")

    def check_alerts_form(self):
        return self.alerts_form.is_visible() is not None

    def click_button_to_see_alert(self):
        return self.button_to_see_alert.click()

    def click_confirm_box_button(self):
        return self.confirm_box_button.click()

    def get_text(self):
        return self.confirm_result.get_text()

    def click_prompt_box_button(self):
        return self.prompt_box_button.click()

    def get_name(self):
        return self.random_name.get_text().split(' ')[2]

    def check_browser_windows_form(self):
        return self.alerts_form.is_visible() is not None
