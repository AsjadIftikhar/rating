import audible


class AudibleApi:
    def __init__(self, email, password, locale):
        self.auth = audible.Authenticator.from_login(email, password, locale=locale, with_username=False,
                                                     captcha_callback=self.custom_captcha_callback,
                                                     )

    def custom_captcha_callback(self, captcha_url):
        print(captcha_url)
        guess = input("Answer for CAPTCHA: ")
        guess = str(guess).strip().lower()
        return guess

    def get_client(self):
        return audible.Client(auth=self.auth)

    def de_register(self):
        self.auth.deregister_device()

# Unused Code:

# # Save credendtials to file
# auth.to_file("cred.txt")
# auth = audible.Authenticator.from_file("cred.txt")
