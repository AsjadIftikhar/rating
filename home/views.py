from django.shortcuts import render, redirect
from authenticate.decorators import authenticated_user
from django.contrib.auth import logout
from home.helpers import *


# Login Page Controller
@authenticated_user
def home(request):
    context = {'user': request.user}
    return render(request, 'home/home.html', context)


@authenticated_user
def log_out(request):
    logout(request)
    return redirect('/login')


# Upload Files
@authenticated_user
def upload_files(request):
    if request.method == 'POST':
        # here you get the files needed
        file = request.FILES['sentFile']
        fileContent = pdf_to_string(file)

        print(fileContent)

    context = {}
    return render(request, 'home/upload_files.html', context)
