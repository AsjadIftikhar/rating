from django.urls import path
from home.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='loginPage'),
    path('upload/', uploadFiles, name='upload'),
]

urlpatterns += staticfiles_urlpatterns()
