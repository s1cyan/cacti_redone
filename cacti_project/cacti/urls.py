from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.render_main_page, name="default"),
    url(r'^home', views.render_home_page, name="home"),
    url(r'^user-registration', views.render_user_registration, name="user-registration"),
    url(r'^login', views.render_login, name='login'),
    url(r'^profile', views.render_profile_page, name='profile'),
    url(r'^friends', views.render_friends_page, name='friends'),
    url(r'^process-user-registration', views.process_user_registration, name='process-user-registration'),
    url(r'^test-render', views.render_success, name='test')
]
