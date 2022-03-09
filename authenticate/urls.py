from django.urls import path
from authenticate.views import register_page, login_page, page_not_found, audible_login
from home.views import log_out
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', login_page, name='loginPage'),
    path('register/', register_page, name='registerPage'),
    path('login/', login_page, name='loginPage'),
    path('404/', page_not_found, name="404"),
    path('logout/', log_out, name="logout"),
    path('audible-login/', audible_login, name='audible_login'),
    path('audible-login/<str:asin>', audible_login, name='audible_login'),
]

urlpatterns += staticfiles_urlpatterns()
