from django.forms import EmailField
from django.contrib.auth import get_user_model


User = get_user_model()


def isEmailAddressValid(email):
    try:
        EmailField().clean(email)
        msg = "Valid"
        return msg
    except None:
        msg = "Invalid"
        return msg


def passvalid(password):
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


def uservalidator(email, user_sid, user_cid):
    check = User.objects.filter(email=email).first()
    check_cid = check.user_cid
    check_sid = check.user_sid
    try:
        if check_cid == user_cid:
            if check_sid == user_sid:
                user = "Valid"
            else:
                user = "Invalid"
        return user
    except None:
        user = "Invalid"
        return user
