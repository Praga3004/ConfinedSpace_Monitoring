from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        print(username,password)
        user = CustomUser.objects.create_user(username=username, password=password)
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login successful!')
        else:
            return HttpResponse('Login failed. Please try again.')
    elif request.method == 'GET':
        return render(request, 'login/login.html')

    
