from django.urls import path
from home.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
