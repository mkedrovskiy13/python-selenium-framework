from selenium.webdriver.common.by import By
from utils.frame import Frame
from driver import DriverSingleton
from elements.button import Button
from pages.base_form import BaseForm
from utils.waiting import Waiting

class NestedFramesPage(BaseForm):

    def __init__(self):
        super().__init__()
        self.name = "nested frames page"
        self.alerts_button = Button((By.XPATH, "//*[@id='framesWrapper']"), "alerts")
        self.unique_element =  self.alerts_button

    def get_nested_frames_text(self):
        Frame.switch_to_frame((By.XPATH, "//*[@id='frame1']"))
        Waiting.wait_for_text((By.TAG_NAME, "body"))
        parent_text = DriverSingleton.get_driver().find_element(By.TAG_NAME, "body").text

        Frame.switch_to_frame((By.TAG_NAME, "iframe"))
        Waiting.wait_for_text((By.TAG_NAME, "p"))
        child_text = DriverSingleton.get_driver().find_element(By.TAG_NAME, "p").text

        DriverSingleton.get_driver().switch_to.default_content()
        return parent_text, child_text
