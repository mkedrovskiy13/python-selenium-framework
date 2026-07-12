from selenium.webdriver.common.by import By
from elements.button import Button

class SideMenu:
    def __init__(self):
        self.side_menu = Button((By.XPATH, "//*[text()='Elements']"), "side menu")
        self.alerts_button = Button((By.XPATH, "//span[text()='Alerts']"), "alerts")
        self.nested_frames_button = Button((By.XPATH, "//span[text()='Nested Frames']"), "nested frames")
        self.browser_windows_button = Button((By.XPATH, "//span[text()='Browser Windows']"), "browser windows")
        self.links_button = Button((By.XPATH, "//*[contains(@href, 'links')]"), "links")
        self.frames_button = Button((By.XPATH, "//*[text()='Frames']"), "frames")
        self.web_tables = Button((By.XPATH, "//span[text()='Web Tables']"), "web tables")

    def click_alerts(self):
        return self.alerts_button.click()

    def click_nested_frames(self):
        return self.nested_frames_button.click()

    def click_browser_windows(self):
        return self.browser_windows_button.click()

    def click_side_menu(self):
        return self.side_menu.click()

    def click_links(self):
        return self.links_button.click()

    def click_frames(self):
        return self.frames_button.click()

    def click_web_tables(self):
        return self.web_tables.click()
