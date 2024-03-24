from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponse('Login successful!')
        else:
            return redirect('/camera-stream')  # Redirect to video feed or any other page if authentication fails
    
    elif request.method == 'GET':
        return render(request, 'login/login.html')
def register(request):
    if request.method=='POST':
        user = request.POST.get('fullname')
        passw = request.POST.get('Password')
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('number')
        gender = request.POST.get('gender')
        bdate = request.POST.get('date')
        count = request.POST.get('country') or None
        city = request.POST.get('city')
         
        user=CustomUser.objects.create_user(username=user,
                                            password=passw,
                                            name=name,
                                            email=email,
                                            addres=address,
                                            number=phone,
                                            gender=gender,
                                            birthdate=bdate,
                                            country=count,
                                            city=city 
                                            
                                            )
        login(request, user)
        return redirect('/camera-stream')  # Redirect to the home page after successful registration

    else:
        return render(request, 'registration_form.html')  # Render the registration form
        

    
