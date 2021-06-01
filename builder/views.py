from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .validator import passvalid, isEmailAddressValid


User = get_user_model()


def home(request):
    return render(request, 'builder/index.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is None and password is None:
            messages.error(request, 'Invalid email or password')
            return redirect('signup')
        else:
            msg_p = passvalid(password)
            msg_e = isEmailAddressValid(email)
            if msg_p == "Valid" and msg_e == "Valid":
                if User.objects.filter(email=email).count() == 0:
                    newuser = User.objects.create_user(email=email, password=password)
                    newuser.save()
                    messages.success(request, 'Successfully created!!')
                    return redirect('login')
                else:
                    messages.info(request, "Email already exist")
                    return redirect('signup')
            else:
                messages.error(request, 'Check your email and password. Password length have to be 8 or more.')
                return redirect('signup')
    return render(request, 'builder/signup.html')


def loginuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is not None and password is not None:
            msg_e = isEmailAddressValid(email)
            if msg_e == 'Valid':
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'User succesfully loggedin')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid email or password')
                    return redirect('login')
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    return render(request, 'builder/login.html')


@login_required()
def logoutuser(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')


@login_required()
def dashboard(request):
    return render(request, 'builder/dashboard.html')
