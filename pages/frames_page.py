from selenium.webdriver.common.by import By
from driver import DriverSingleton
from elements.text import Text
from pages.base_form import BaseForm
from utils.frame import Frame
from utils.waiting import Waiting

class FramesPage(BaseForm):

    __frame_text = (By.XPATH, "//*[@id='sampleHeading']")

    def __init__(self):
        super().__init__()
        self.name = "frames page"
        self.frames_wrapper = Text((By.XPATH, "//*[@id='framesWrapper']"), "frames wrapper")
        self.unique_element = self.frames_wrapper

    def get_frames_text(self):

        Frame.switch_to_frame((By.XPATH, "//*[@id='frame1']"))
        upper_text = Waiting.wait_for_visible(self.__frame_text).text

        DriverSingleton.get_driver().switch_to.default_content()

        Frame.switch_to_frame((By.XPATH, "//*[@id='frame2']"))
        lower_text = Waiting.wait_for_visible(self.__frame_text).text

        DriverSingleton.get_driver().switch_to.default_content()
        return upper_text, lower_text
