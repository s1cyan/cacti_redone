from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def login_check(username_email, password):
    '''
    Checks if username exists- if so tries to login with credential
    if input was not a username checks if user exists from email and tries to login with credentials
    :param username_email: username or email - whatever is put into first box
    :param password: noot noot
    :return: T/F on success of login
    '''
    try:
        User.objects.get(username = username_email)
        user = authenticate(username = username_email,password = password)
        return True
    except ObjectDoesNotExist:
        try:
            User.objects.get(email = username_email)
            user = authenticate(email = username_email, password = password)
            return True

        except ObjectDoesNotExist:
            return False
