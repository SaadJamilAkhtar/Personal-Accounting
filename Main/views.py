from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *


def home(request):
    return render(request, 'index.html', {"page": "Dashboard"})


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.POST:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
    return render(request, 'login.html')


def createExpenseAccount(request):
    if request.POST:
        form = ExpenseAccountForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Account Created Successfully !"
            type = "success"
        else:
            message = "Account Was Not Created. Try Again !"
            type = "error"
        data = {
            "message": message,
            "type": type
        }
        return render(request, '', data)  # add code later

    form = ExpenseAccountForm()
    data = {
        "form": form
    }
    return render(request, '', data)  # add code later


def createRevenueAccount(request):
    if request.POST:
        form = RevenueAccount(request.POST)
        if form.is_valid():
            form.save()
            message = "Account Created Successfully !"
            type = "success"
        else:
            message = "Account Was Not Created. Try Again !"
            type = "error"
        data = {
            "message": message,
            "type": type
        }
        return render(request, '', data)  # add code later

    form = RevenueAccount()
    data = {
        "form": form
    }
    return render(request, '', data)  # add code later
