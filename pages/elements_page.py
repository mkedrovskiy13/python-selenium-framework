from selenium.webdriver.common.by import By
from driver import DriverSingleton
from elements.button import Button
from elements.text import Text
from pages.base_form import BaseForm
from elements.table import WebTable

class ElementsPage(BaseForm):

    def __init__(self):
        super().__init__()
        self.name = "elements page"
        self.web_tables_form = Text((By.XPATH, "//h1[text()='Web Tables']"), "web tables form")
        self.unique_element = self.web_tables_form
        self.add_button = Button((By.ID, "addNewRecordButton"), "add")
        self.registration_form = Text((By.XPATH, "//*[@class='modal-body']"), "registration form")
        self.table_rows = WebTable((By.XPATH, "//tbody/tr"), "table")

    def get_rows_count(self):
        return len(self.table_rows.get_rows())

    def check_web_tables_form(self):
        return self.web_tables_form.is_visible() is not None

    def click_add_button(self):
        return self.add_button.click()

    def is_user_in_table(self, user):
        rows = DriverSingleton.get_driver().find_elements(*self.table_rows.locator)
        for row in rows:
            if all([
                user.first_name in row.text,
                user.last_name in row.text,
                user.email in row.text,
                user.age in row.text,
                user.salary in row.text,
                user.department in row.text
            ]):
                return True
        return False

    def delete_user(self, email):
        locator = (By.XPATH, f"//*[text()='{email}']/following::*[contains(@id, 'delete')]")
        DriverSingleton.get_driver().find_element(*locator).click()
