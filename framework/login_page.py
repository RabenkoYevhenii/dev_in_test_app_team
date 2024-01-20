from selenium.common import NoSuchElementException

from utils.credentials_operations import CredentialsOperation


class LoginPage(CredentialsOperation):
    def enter_email(self, email):
        self.enter_credential(
            credential=email,
            credential_field_xpath=(
                '//android.widget.EditText[@resource-id="com.ajaxsystems:'
                'id/authLoginEmail"]'
            ),
        )

    def enter_password(self, password):
        self.enter_credential(
            credential=password,
            credential_field_xpath=(
                '//android.widget.EditText[@resource-id="com.ajaxsystems:'
                'id/authLoginPassword"]'
            ),
        )

    def click_login_button(self):
        login_button_xpath = (
            "(//androidx.compose.ui.platform.ComposeView[@resource-id="
            '"com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.'
            "view.View/android.widget.Button"
        )
        login_button = self.find_element(login_button_xpath)
        login_button.clear()
        self.click_element(login_button)

    def is_logged_in(self):
        try:
            self.find_element(
                '//android.view.ViewGroup[@resource-id="com.'
                'ajaxsystems:id/coordinatorLayout"]'
            )
            return True
        except NoSuchElementException:
            return False
