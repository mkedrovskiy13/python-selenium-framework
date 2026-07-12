from selenium.webdriver.common.by import By
from elements.button import Button
from elements.text import Text
from pages.base_form import BaseForm

class LinksPage(BaseForm):

    def __init__(self):
        super().__init__()
        self.name = "links page"
        self.__browser_windows_form = Text((By.XPATH, "//*[@id='linkWrapper']"), "browser windows form")
        self.unique_element = self.__browser_windows_form
        self.__home_link = Button((By.XPATH, "//*[@id='simpleLink']"), "home")

    def click_home_link(self):
        return self.__home_link.click()
