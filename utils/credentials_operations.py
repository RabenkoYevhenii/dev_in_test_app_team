from framework.page import Page


class CredentialsOperation(Page):
    def enter_credential(self, credential, credential_field_xpath):
        email_field = self.find_element(credential_field_xpath).clear()
        email_field.send_keys(credential)
