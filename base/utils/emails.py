from django.core.mail import send_mail


class EmailHandler:
    """ sending text and token using email """

    def __init__(self):
        ...

    def send_otp(self, email, token):
        """ send otp to use without any special text """
        print("*****************")
        print(f"Token:{token}")
        print("*****************")
