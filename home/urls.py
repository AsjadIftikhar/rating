from django.urls import path
from home.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('/history', user_history, name='history'),
    path('/library', all_books, name='library'),

]

urlpatterns += staticfiles_urlpatterns()
