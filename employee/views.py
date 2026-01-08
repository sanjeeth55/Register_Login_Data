from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from employee.models import Employee



#login page to validate the login credantials

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        employees = Employee.objects.filter(user_name=username,password=password)
        
        if employees.exists():
            print(employees)
            for i in employees:
                if i.user_name == username and i.password == password:
                    return redirect('home')
                else:
                    return render(request, 'login_page.html')
        else:           
            messages.error(request, 'username ane password not found')
            return render(request, 'login_page.html')     
    return render(request, 'login_page.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        employees = Employee.objects.filter(user_name = username,password=password)
        print(username, password, email)

        if employees.exists():
            messages.error(request, 'user name is alread existed')
            return render(request, 'register.html')
        
        Employee.objects.create(user_name=username, email=email, password=password)
        messages.error(request, 'Register has been successful completed, Login to access the site')
        return redirect('home')   
    
    return render(request, 'register.html')
 
 
# @login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def logout(request):
    return redirect('login')
