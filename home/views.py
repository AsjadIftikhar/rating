from django.shortcuts import render


# Login Page Controller
def home(request):
    context = {'user': request.user}
    return render(request, 'home/home.html', context)
