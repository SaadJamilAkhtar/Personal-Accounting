from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .authUser import checkUserParams
from .models import *
from .forms import *


@login_required()
def home(request):
    data = {"page": "Dashboard",
            "title": "home"}
    return render(request, 'index.html', data)


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.POST:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
    return render(request, 'login.html')


def register(request):
    if request.POST:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        email = request.POST.get('email')
        username = request.POST.get('username')
        data = {}
        if checkUserParams(first_name, last_name, email, username, pass1, pass2):
            try:
                user = AccuUser.objects.create_user(username, email, pass1, first_name=first_name, last_name=last_name)
                user_ = authenticate(username=username, password=pass1)
                login(request, user_)
                cash = Account.objects.create(name="Cash")
                user.accounts.add(cash)
                user.save()
                return redirect(reverse('home'))
            except:
                data["status"] = "danger"
                data["message"] = "Username already taken"
        else:
            data["status"] = "danger"
            data[
                "message"] = "Password must be at least 8 character long, with uppercase, lowercase and numeric" \
                             " values and both passwords must match"

        return render(request, "register.html", data)
    return render(request, 'register.html')


@login_required()
def log_out(request):
    logout(request)
    return redirect('/')


@login_required()
def createAccount(request):
    if request.POST:
        user = AccuUser.objects.get(username=request.user.username)
        form = AccountForm(request.POST)
        if form.is_valid():
            acc = form.save()
            user.accounts.add(acc)
            user.save()
            message = "Account Created Successfully !"
            type = "success"
            return redirect(reverse('all-account'))
        else:
            message = "Account Was Not Created. Try Again !"
            type = "danger"
            data = {
                "page": "Register Account",
                "title": "Reg Acc",
                "message": message,
                "status": type
            }
            return render(request, 'addAccount.html', data)

    form = AccountForm()
    data = {
        "form": form,
        "page": "Register Account",
        "title": "Reg Acc"
    }
    return render(request, 'addAccount.html', data)


@login_required()
def allAccounts(request):
    user = AccuUser.objects.get(username=request.user.username)
    data = {
        "page": "Accounts",
        "title": "accounts",
        "accounts": user.accounts.all()
    }
    return render(request, 'accounts.html', data)


@login_required()
def editAccount(request, id):
    user = AccuUser.objects.get(username=request.user.username)
    accounts = user.accounts.filter(id=id)
    print(accounts)
    if accounts.count() > 0:
        account = Account.objects.get(id=id)
        if request.POST:
            form = AccountForm(request.POST, instance=account)
            if form.is_valid():
                form.save()
                return redirect(reverse("all-account"))
        form = AccountForm(instance=account)
        data = {
            "page": "edit account",
            "title": "Edit Account",
            "form": form
        }
        return render(request, 'addAccount.html', data)
    return redirect(reverse("all-account"))


@login_required()
def deleteAccount(request, id):
    user = AccuUser.objects.get(username=request.user.username)
    account = user.accounts.filter(id=id)
    if account.count() > 0:
        account.first().delete()
    return redirect(reverse("all-account"))
