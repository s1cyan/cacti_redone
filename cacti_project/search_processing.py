from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def lookup(username_or_email):

    try:
        user = User.objects.get(username = username_or_email)
        return user
    except ObjectDoesNotExist:
        try:
            user = User.objects.get(email = username_or_email)
            return user
        except ObjectDoesNotExist:
            return
