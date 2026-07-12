from selenium.webdriver.common.by import By
from elements.button import Button
from elements.text import Text
from elements.text_field import TextField
from pages.base_form import BaseForm
from models.user_model import User

class RegistrationForm(BaseForm):

    def __init__(self):
        super().__init__()
        self.unique_element = Text((By.ID, "userForm"), "registration form")
        self.submit_button = Button((By.ID, "submit"), "submit")
        self.first_name = TextField((By.ID, "firstName"), "first name")
        self.last_name = TextField((By.ID, "lastName"), "last name")
        self.email = TextField((By.ID, "userEmail"), "user email")
        self.age = TextField((By.ID, "age"), "age")
        self.salary = TextField((By.ID, "salary"), "salary")
        self.department = TextField((By.ID, "department"), "department")

    def fill_form(self, user: User):
        self.first_name.enter_text(user.first_name)
        self.last_name.enter_text(user.last_name)
        self.email.enter_text(user.email)
        self.age.enter_text(user.age)
        self.salary.enter_text(user.salary)
        self.department.enter_text(user.department)

    def submit(self):
        self.submit_button.click()

    def check_registration_form(self):
        return self.unique_element.is_visible()
