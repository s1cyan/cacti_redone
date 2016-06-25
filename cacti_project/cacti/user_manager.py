from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class UserError(Exception):
    pass


class UserManager(object):
    def __init__(self):
        pass

    def create_regular_user(self, username, email, password):
        """
        Checks if the user exists in the database and raises an error. Otherwise
        create a user.
        :param username: string
        :param email: string
        :param password: string
        :return: User
        """
        try:
            _user = User.objects.get(username=username, email=email)
            return None
        except ObjectDoesNotExist:
            # Create the user
            _user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
        return _user

    def authenticate_user(self, _user):
        pass
