import audible


def custom_external_callback(captcha_url):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.utils import ChromeType

    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

    driver.get(captcha_url)

    while driver.current_url == captcha_url:
        pass
    url = driver.current_url

    while driver.current_url == url:
        pass

    return driver.current_url


class AudibleApi:
    def __init__(self):
        self.auth = audible.Authenticator.from_login_external(locale="us", with_username=False,
                                                              login_url_callback=custom_external_callback,
                                                              )
        self.auth.to_file("cred.txt")

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
