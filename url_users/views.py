from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserLoginForm, UserSigninForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout

def signupview(request):
    if request.method == 'POST':
        form = UserSigninForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponse("Signed Up")
    else:
        form = UserSigninForm()

    return render(request, 'auth/signup.html', {'form':form})

def loginview(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Invalid Credentials')
    else:
        form = UserLoginForm()
    
    return render(request, 'auth/login.html', {'form':form})

@csrf_exempt
def logoutview(request):
    logout(request)
    return redirect('home')