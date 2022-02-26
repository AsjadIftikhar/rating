from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Sign Up Page Controller:
def registerPage(request):
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
def loginPage(request):
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
    #     name = request.POST.get('name')
    #     password = request.POST.get('password')
    #
    #     user = authenticate(request, username=name, password=password)
    #
    #     if user:
    #         login(request, user)
    #         return redirect('/home/')
    #     else:
    #         messages.info(request, 'Username OR password Incorrect')
    #         return redirect('loginPage')

    context = {}
    return render(request, 'authenticate/audible.html', context)


def PageNotFound(request):
    return render(request, 'authenticate/404.html', {})
