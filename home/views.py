from django.shortcuts import render, redirect
from authenticate.decorators import authenticated_user
from django.contrib.auth import logout
from .helpers import *


# Login Page Controller
@authenticated_user
def home(request):
    if request.method == 'POST':
        # here you get the files needed
        file = request.FILES['sentFile']
        print(file)
        file_content = pdf_to_string(file)

        print(file_content)

        context = {'user': request.user}
        return render(request, 'home/home.html', context)
    else:
        context = {'user': request.user}
        return render(request, 'home/home.html', context)


@authenticated_user
def log_out(request):
    logout(request)
    return redirect('/login')

