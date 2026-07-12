from driver import DriverSingleton
from pages.browser_windows_page import BrowserWindowsPage
from pages.links_page import LinksPage
from pages.main_page import MainPage
from pages.side_menu import SideMenu
from utils.logger import log_step
from utils.tab import Tab

def test_case4():
    log_step("1. Открываем главную страницу")
    main_page = MainPage()
    log_step("2. Проверяем, что главная страница открыта")
    assert main_page.is_opened(), f"{main_page.name} is not opened"

    log_step("3. Кликаем на кнопку Alerts, Frame & Windows.")
    main_page.click_alerts_frame_windows()
    log_step("4. Кликаем на кнопку Browser Windows")
    side_menu = SideMenu()
    side_menu.click_browser_windows()

    browser_windows_page = BrowserWindowsPage()
    log_step("5. Проверяем, что открыта страница с формой Browser Windows")
    assert browser_windows_page.is_opened(), f"{browser_windows_page.name} is not opened"

    original_tab = DriverSingleton.get_driver().current_window_handle

    log_step("6. Кликаем на кнопку New Tab")
    browser_windows_page.click_new_tab()
    log_step("7. Переключаемся на новую вкладку")
    Tab.switch_to_new_tab()
    log_step("8. Проверяем, что открыта новая вкладка")
    assert len(DriverSingleton.get_driver().window_handles) == 2, "New tab didn't open"
    log_step("9. Проверяем, что открыта страница sample page")
    assert browser_windows_page.is_sample_tab_opened(), "Sample page is not opened"

    log_step("10. Закрываем текущую вкладку")
    Tab.close_current_tab()
    log_step("11. Переключаемся на прошлую вкладку")
    Tab.switch_to_tab(original_tab)
    log_step("12. Проверяем, что открыта страница с формой Browser Windows")
    assert browser_windows_page.is_opened(), f"{browser_windows_page.name} is not opened"

    log_step("13. Кликаем на меню Elements")
    side_menu.click_side_menu()
    log_step("14. Кликаем на кнопку Links")
    side_menu.click_links()

    links_page = LinksPage()
    log_step("15. Проверяем, что открыта страница с формой Links")
    assert links_page.is_opened(), f"{links_page.name} is not opened"

    links_tab = DriverSingleton.get_driver().current_window_handle

    log_step("16. Кликаем на ссылку Home")
    links_page.click_home_link()
    log_step("17. Переключаемся на новую вкладку")
    Tab.switch_to_new_tab()
    log_step("18. Проверяем, что главная страница открыта")
    assert main_page.is_opened(), f"{main_page.name} is not opened"
    log_step("19. Переключаемся на прошлую вкладку")
    Tab.switch_to_tab(links_tab)
    log_step("20. Проверяем, что открыта страница с формой Links")
    assert links_page.is_opened(), f"{links_page.name} is not opened"
