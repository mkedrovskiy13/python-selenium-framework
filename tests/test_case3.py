import time
import pytest

from pages.registration_form import RegistrationForm
from pages.side_menu import SideMenu
from utils.data_loader import TestDataLoader
from pages.elements_page import ElementsPage
from pages.main_page import MainPage
from utils.logger import log_step

users = TestDataLoader.load_users()
user = users[0]

@pytest.mark.parametrize("user", users)
def test_case3(user):
    log_step("1. Открываем главную страницу")
    main_page = MainPage()
    log_step("2. Проверяем, что главная страница открыта")
    assert main_page.is_opened(), f"{main_page.name} is not opened"

    log_step("3. Кликаем на кнопку Elements")
    side_menu = SideMenu()
    main_page.click_elements_button()
    elements_page = ElementsPage()
    log_step("4. Кликаем на кнопку Web Tables")
    side_menu.click_web_tables()
    log_step("5. Проверяем, что открыта страница с формой Web tables")
    assert elements_page.check_web_tables_form(), "Web tables form is not opened"

    log_step("6. Кликаем на кнопку add")
    elements_page.click_add_button()
    registration_form = RegistrationForm()
    log_step("7. Проверяем, что открыта страница с формой регистрации")
    assert registration_form.check_registration_form(), "Registration form is not opened"

    log_step("8. заполняем форму регистрации")
    registration_form.fill_form(user)
    log_step("9. Кликаем на кнопку submit")
    registration_form.submit()
    time.sleep(2)
    log_step("10. Проверяем, что форма регистрации закрыта")
    assert registration_form.check_registration_form() == False, "Registration form is not closed"
    log_step("11. Проверяем, что в таблице появились данные пользователя")
    assert elements_page.is_user_in_table(user), "User is not in table"

    rows_before_delete = elements_page.get_rows_count()

    log_step("12. Удаляем пользователя")
    elements_page.delete_user(user.email)
    log_step("13. Проверяем, что пользователь удален")
    assert elements_page.is_user_in_table(user) == False, "User was not deleted from table"
    log_step("14. Проверяем, что количество записей в таблице изменилось")
    assert rows_before_delete != elements_page.get_rows_count(), "The number of rows has not changed"
