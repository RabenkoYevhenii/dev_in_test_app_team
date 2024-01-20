import logging

import pytest


logging.basicConfig(filename="test_login.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(console_handler)
logging.getLogger().setLevel(logging.INFO)


@pytest.mark.parametrize(
    "email, password", [
        (
            "wrong_email@gmail.com",
            "qa_automation_password"
        ),
        (
            "qa.ajax.app.automation@gmail.com",
            "wrong_password"
        ),
        (
            "wrong_email@gmail.com",
            "wrong_password"
        )
    ]
)
def test_wrong_credentials(user_login_fixture, email, password):
    logging.info(
        f"Starting test with email: {email}, password: {password}"
    )
    login_page = user_login_fixture

    logging.info("Entering email and password")
    login_page.enter_email(email)
    login_page.enter_password(password)

    logging.info("Clicking login button")
    login_page.click_login_button()

    error_field_xpath = (
        '//android.widget.TextView[@resource-id="com.ajaxsystems:'
        'id/snackbar_text"]'
    )

    logging.info("Checking for error message presence")
    assert login_page.find_element(error_field_xpath)
    logging.info("Test completed successfully")


@pytest.mark.parametrize(
    "email, password", [(
        "qa.ajax.app.automation@gmail.com",
        "qa_automation_password"
    )]
)
def test_successful_login(user_login_fixture, email, password):
    logging.info(
        f"Starting test with email: {email}, password: {password}"
    )
    login_page = user_login_fixture

    logging.info("Entering email and password")
    login_page.enter_email(email)
    login_page.enter_password(password)

    logging.info("Clicking login button")
    login_page.click_login_button()

    logging.info("Checking if we get to the home screen")
    assert login_page.is_logged_in()
    logging.info("Test completed successfully")
