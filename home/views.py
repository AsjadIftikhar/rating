from django.shortcuts import render


# Login Page Controller
def home(request):
    context = {}
    return render(request, 'home/home.html', context)
