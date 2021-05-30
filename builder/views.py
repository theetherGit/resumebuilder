from django.shortcuts import render

def home(request):
    return render(request, 'builder/index.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
    return render(request, 'builder/signup.html')

def login(request):
    return render(request, 'builder/login.html')