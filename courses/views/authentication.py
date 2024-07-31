from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, login
from django.contrib import messages
from courses.forms import RegisterForm, LoginForm
from django.contrib.auth import logout


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'courses/../../templates/authentication/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('index')
            else:
                messages.error(request, 'Authentication failed.')
        else:
            for error in form.errors.values():
                messages.error(request, error)
        return render(request, 'courses/../../templates/authentication/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'courses/../../templates/authentication/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password.')
        return render(request, 'courses/../../templates/authentication/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')