from framework.page import Page


class CredentialsOperation(Page):
    def enter_credential(self, credential, credential_field_xpath):
        credential_field = self.find_element(credential_field_xpath).clear()
        credential_field.send_keys(credential)
