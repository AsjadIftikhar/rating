from django.urls import path
from authenticate.views import registerPage, loginPage, PageNotFound
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', loginPage, name='loginPage'),
    path('register/', registerPage, name='registerPage'),
    path('login/', loginPage, name='loginPage'),
    path('404/', PageNotFound, name="404"),
]

urlpatterns += staticfiles_urlpatterns()
