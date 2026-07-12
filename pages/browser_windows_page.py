from selenium.webdriver.common.by import By
from elements.button import Button
from elements.text import Text
from pages.base_form import BaseForm

class BrowserWindowsPage(BaseForm):

    def __init__(self):
        super().__init__()
        self.name = "browser windows page"
        self.__browser_windows_form = Text((By.XPATH, "//*[@id='browserWindows']"), "browser windows form")
        self.unique_element = self.__browser_windows_form
        self.new_tab_button = Button((By.XPATH, "//*[@id='tabButton']"), "new tab")
        self.sample_heading = Text((By.XPATH, "//*[@id='sampleHeading']"), "sample heading")

    def click_new_tab(self):
        self.new_tab_button.click()

    def is_sample_tab_opened(self):
        return self.sample_heading.is_present() is not None
