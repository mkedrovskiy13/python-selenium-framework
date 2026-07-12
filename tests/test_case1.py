from pages.alerts_page import AlertsPage
from pages.side_menu import SideMenu
from utils.alert import Alert
from pages.main_page import MainPage
from utils.name_generator import random_text
from utils.logger import log_step

def test_case1():
    log_step("1. Открываем главную страницу")
    main_page = MainPage()
    log_step("2. Проверяем, что главная страница открыта")
    assert main_page.is_opened(), f"{main_page.name} is not opened"

    log_step("3. Кликаем на кнопку Alerts, Frame & Windows.")
    main_page.click_alerts_frame_windows()

    alerts_page = AlertsPage()
    log_step("4. Кликаем на кнопку Alerts в левом меню")
    side_menu = SideMenu()
    side_menu.click_alerts()
    log_step("5. Проверяем, что на странице появилась форма Alerts")
    assert alerts_page.check_alerts_form(), f"{alerts_page.name} is not opened"

    log_step("6. Кликаем на кнопку click button to see alert")
    alerts_page.click_button_to_see_alert()
    alert = Alert()
    log_step('7. Проверяем, что открыт алерт с текстом "You clicked a button"')
    assert alert.get_text() == "You clicked a button", "Wrong alert text"

    log_step("8 .Кликаем на кнопку ОК")
    alert.accept()
    log_step("9 .Проверяем, что алерт закрылся")
    assert alert.is_closed(), "Alert is not closed"

    log_step("10. Кликаем на кнопку On button click, confirm box will appear")
    alerts_page.click_confirm_box_button()
    log_step('11. Проверяем, что открыт алерт с текстом "Do you confirm action?"')
    assert alert.get_text() == "Do you confirm action?", "Wrong alert text"

    log_step("12. Кликаем на кнопку ОК")
    alert.accept()
    log_step("13. Проверяем, что алерт закрылся")
    assert alert.is_closed(), "Alert is not closed"
    log_step('14. Проверяем, что рядом с кнопкой появилась надпись "You selected Ok"')
    assert alerts_page.get_text() == "You selected Ok", "Wrong text near the button"

    log_step("15. Кликаем на кнопку On button click, prompt box will appear")
    alerts_page.click_prompt_box_button()
    log_step('16. Проверяем, что открыт алерт с текстом "Please enter your name"')
    assert alert.get_text() == "Please enter your name", "Wrong alert text"

    random_name = random_text()
    log_step("17. Вводим случайно сгенерированный текст")
    alert.enter_text(random_name)
    log_step("18. Кликаем на кнопку ОК")
    alert.accept()
    log_step("19. Проверяем, что алерт закрылся")
    assert alert.is_closed(), "Alert is not closed"
    log_step('20. Проверяем, что рядом с кнопкой появилась надпись, соответствующая введенному в алерт')
    assert alerts_page.get_name() == random_name, "Wrong text near the button"
