from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django.http import JsonResponse


# Login Page View
class LoginPageView(View):
    template_name = "auth/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    


# Suporte Page View
class SuportePageView(View):
    template_name = "auth/suporte.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
