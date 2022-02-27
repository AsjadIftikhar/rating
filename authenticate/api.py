import audible


class AudibleApi:
    def __init__(self, email, password, locale, view_func):
        # self.auth = audible.Authenticator.from_login(email, password, locale=locale, with_username=False,
        #                                              # captcha_callback=view_func,
        #                                              )
        self.auth = audible.Authenticator.from_login_external(locale=locale, with_username=False,
                                                              # login_url_callback=self.custom_captcha_callback,
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

    def get_library(self):
        library = self.get_client().get(
            'library',
            num_results=1000,
            response_groups=','.join([
                'series',
                'product_desc',
                'product_attrs',
            ]),
            sort_by='Author',
        )
        print(library)
        return library

# Unused Code:

# # Save credendtials to file
# auth.to_file("cred.txt")
# auth = audible.Authenticator.from_file("cred.txt")
