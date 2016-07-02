from django.shortcuts import render
from user_manager import UserManager
from forms import LoginForm
from login_check import login_check

# Global managers
_user_manager = UserManager()


def render_main_page(request):
    return render(request, "default.html")


# Create your views here.
def render_home_page(request):
    return render(request, "home.html")


def render_user_registration(request):
    context_dict = {
        'action_user_registration': 'process-user-registration'
    }
    return render(request, "user_registration.html", context_dict)


def process_user_registration(request):
    _user = _user_manager.create_regular_user(username=request.POST['username'],
                                              password=request.POST['password'],
                                              email=request.POST['email'])
    if _user is not None:
        return render(request, "successful_registration.html")
    else:
        context_dict = {
            'error': True
        }
        return render(request, "user_registration.html", context_dict)


def render_profile_page(request):
    return render(request, "profile.html")


def render_friends_page(request):
    return render(request, 'friends.html')


def render_login(request):
    # Grab the username/email and the password
    if request.method == 'POST':
        is_user_authenticated = login_check(request.POST['username'], request.POST['password'])
        print 'Is Authenticated? %s' % is_user_authenticated
        context_dict = {'error' : not is_user_authenticated}
        if is_user_authenticated:
            # TODO: Use HTTP Redirect
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', context_dict)

    return render(request, 'login.html')


def render_success(request):
    return render(request, "successful_registration.html")
