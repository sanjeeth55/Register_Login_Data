from django.contrib import messages
from django.shortcuts import render, redirect
from employee.models import Employee
from .forms import LoginForm
from django.contrib.auth.hashers import make_password, check_password
from .decorators import employee_login_required


def login_view(request):
    if 'employee_id' in request.session:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']

            try:
                try:
                    employee = Employee.objects.get(user_name=identifier)
                except Employee.DoesNotExist:
                    employee = Employee.objects.get(email=identifier)

            except Employee.DoesNotExist:
                messages.error(request, "Employee not found")
                return redirect('login')

            if not employee.password.startswith('pbkdf2_'):
                if password == employee.password:
                    employee.password = make_password(password)
                    employee.save()
                else:
                    messages.error(request, "Invalid password")
                    return redirect('login')
            else:
                if not check_password(password, employee.password):
                    messages.error(request, "Invalid password")
                    return redirect('login')

            request.session['employee_id'] = employee.id
            request.session['employee_username'] = employee.user_name
            return redirect('home')

    else:
        form = LoginForm()

    return render(request, 'login_page.html', {'form': form})


def register(request):
    if 'employee_id' in request.session:
        return redirect('login')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Employee.objects.filter(user_name=username).exists():
            messages.error(request, 'User already exists')
            return redirect('register')

        Employee.objects.create(
            user_name=username,
            email=email,
            password=make_password(password)
        )

        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'register.html')


@employee_login_required
def home(request):
    username = request.session.get('employee_username')
    return render(request, 'home.html', {'username': username})


def logout_view(request):
    request.session.flush()
    messages.success(request, "You have been logged out")
    return redirect('login')


@employee_login_required
def about(request):
    return render(request, 'about.html')


@employee_login_required
def features(request):
    return render(request, 'features.html')


@employee_login_required
def contact(request):
    return render(request, 'contact.html')