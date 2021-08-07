from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views import View
from accounts.forms import LoginForm


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('page_url'))
        form = LoginForm()
        return render(request, 'logins/Login.html', context={'form':form})

    def post(self, request):
        bound_form = LoginForm(request.POST)

        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('page_url'))
        return render(request, 'logins/Login.html', context={'form': bound_form})
