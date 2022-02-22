from django.urls import path
from home.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='loginPage'),
]

urlpatterns += staticfiles_urlpatterns()
