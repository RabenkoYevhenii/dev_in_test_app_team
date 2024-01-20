import pytest
from selenium.common import NoSuchElementException, TimeoutException

from framework.login_page import LoginPage


@pytest.fixture(scope="function")
def user_login_fixture(driver):
    login_page = LoginPage(driver)
    try:
        login_button = login_page.find_element(
            "(//androidx.compose.ui.platform.ComposeView[@resource-id="
            '"com.ajaxsystems:id/compose_view"])[1]/android.view.View/android'
            ".view.View/android.widget.Button"
        )
        login_page.click_element(login_button)
    except NoSuchElementException:
        pass
    except TimeoutException:
        pass
    yield login_page
