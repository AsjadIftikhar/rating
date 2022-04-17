from django.urls import path
from home.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home_or_history, name='home_or_history'),
    path('history', user_history, name='history'),
    path('link', home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
