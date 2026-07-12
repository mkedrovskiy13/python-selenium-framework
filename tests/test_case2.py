from pages.frames_page import FramesPage
from pages.main_page import MainPage
from pages.nested_frames_page import NestedFramesPage
from pages.side_menu import SideMenu
from utils.logger import log_step

def test_case2():
    log_step("1. Открываем главную страницу")
    main_page = MainPage()
    log_step("2. Проверяем, что главная страница открыта")
    assert main_page.is_opened(), f"{main_page.name} is not opened"

    log_step("3. Кликаем на кнопку Alerts, Frame & Windows.")
    main_page.click_alerts_frame_windows()
    log_step("4. Кликаем на кнопку Nested Frames")
    side_menu = SideMenu()
    side_menu.click_nested_frames()

    nested_frames_page = NestedFramesPage()
    log_step("5. Проверяем, что открыта страница с формой Nested Frames")
    assert nested_frames_page.is_opened(), f"{nested_frames_page.name} page is not opened"

    parent_text, child_text = nested_frames_page.get_nested_frames_text()
    log_step('6. Проверяем, что в центре страницы присутствуют надписи "Parent frame" и "Child Iframe"')
    assert parent_text == "Parent frame", "Parent text is incorrect"
    assert child_text == "Child Iframe", "Child text is incorrect"

    log_step("7. Кликаем на кнопку Frames")
    side_menu.click_frames()

    frames_page = FramesPage()

    log_step("8. Проверяем, что открыта страница с формой Frames")
    assert frames_page.is_opened(), f"{frames_page.name} is not opened"

    log_step("9. Проверяем, что надпись из верхнего фрейма соответствует надписи из нижнего")
    upper_frame_text, lower_frame_text = frames_page.get_frames_text()
    assert upper_frame_text == lower_frame_text, "frame text doesnt match"
