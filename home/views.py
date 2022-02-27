from django.shortcuts import render, redirect
from authenticate.decorators import authenticated_user
from django.contrib.auth import logout


# Login Page Controller
@authenticated_user
def home(request):
    context = {'user': request.user}
    return render(request, 'home/home.html', context)


@authenticated_user
def log_out(request):
    logout(request)
    return redirect('/login')
