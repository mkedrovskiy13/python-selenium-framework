from selenium.webdriver.common.by import By
from elements.button import Button
from pages.base_form import BaseForm
from elements.img import Img

class MainPage(BaseForm):

    def __init__(self):
        super().__init__()
        self.name = "main page"
        self.unique_element = Img((By.XPATH, "//*[@class='banner-image']"),"image")
        self.alerts_button = Button((By.XPATH, "//*[contains(@href, 'alert')]"), "alerts")
        self.elements_button = Button((By.XPATH, "//*[contains(@href, 'elements')]"), "elements")

    def click_alerts_frame_windows(self):
        return self.alerts_button.click()

    def click_elements_button(self):
        return self.elements_button.click()
