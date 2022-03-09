from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from authenticate.api import AudibleApi
from audible_books import *
from speech_text import *


# Sign Up Page Controller:
def register_page(request):
    # Default Django User Creation Form
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)


# Login Page Controller
def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)

        if user:
            login(request, user)
            return redirect('/home/')
        else:
            messages.info(request, 'Username OR password Incorrect')
            return redirect('loginPage')

    context = {}
    return render(request, 'authenticate/login.html', context)


# Login Page Controller
def audible_login(request):
    # if request.method == 'POST':
    # email = request.POST.get('Email')
    # password = request.POST.get('Password')
    # locale = request.POST.get('Locale')
    #
    # print(email, password, locale)
    api = AudibleApi()
    client = api.get_client()
    library = api.get_library()
    api.de_register()

    if request.method == 'POST':
        download_book(client, asin)
        book_text = speech_to_text()

        return render(request, 'authenticate/audible.html', context)

    if request.method == 'GET':
        # api = AudibleApi()
        # client = api.get_client()
        # library = api.get_library()
        # api.de_register()

        context = {'library': library['items']}
        return render(request, 'authenticate/audible.html', context)
    # else:
    #
    #     context = {}
    #     return render(request, 'authenticate/audible.html', context)


def page_not_found(request):
    return render(request, 'authenticate/404.html', {})
