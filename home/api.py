import audible


def custom_captcha_callback(captcha_url):
    print(captcha_url)
    guess = input("Answer for CAPTCHA: ")
    guess = str(guess).strip().lower()
    return guess


# This is supposed to run only once
# Authorize and register in one step
auth = audible.Authenticator.from_login(
    "l164134@lhr.nu.edu.pk",
    "pMBU%ZH\S377,s!",
    locale="us",
    with_username=False,
    captcha_callback=custom_captcha_callback,
)

# Save credendtials to file
auth.to_file("cred.txt")
auth = audible.Authenticator.from_file("cred.txt")
client = audible.Client(auth=auth)

auth.deregister_device()