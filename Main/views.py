from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    return render(request, 'Main.html')


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
