from django.forms import EmailField


def isEmailAddressValid(email):
    try:
        EmailField().clean(email)
        msg = "Valid"
        return msg
    except None:
        msg = "Invalid"
        return msg


def passvalid(password):
    msg = ''
    try:
        if len(password) >= 8:
            if password.isalpha():
                msg = "Invalid"
            elif password.isnumeric():
                msg = "Invalid"
            else:
                msg = "Valid"
        else:
            msg = "Invalid"
        return msg
    except None:
        msg = "Invalid"
        return msg
