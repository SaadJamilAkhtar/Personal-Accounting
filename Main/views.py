from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .authUser import checkUserParams
from .models import *
from .forms import *


@login_required()
def home(request):
    user = AccuUser.objects.get(username=request.user.username)
    cash = user.accounts.get(name='Cash')
    if request.POST:
        form = EntryForm(user, request.POST)
        if form.is_valid():
            balance = form.cleaned_data.get("amount")
            credit_acc = Account.objects.get(id=form.cleaned_data.get("credit"))
            debit_acc = Account.objects.get(id=form.cleaned_data.get("debit"))
            entry = Entry.objects.create(details=form.cleaned_data.get("entry"),
                                         credit=credit_acc, debit=debit_acc,
                                         amount=balance)
            credit_acc.entries.add(entry)
            credit_acc.updateBalance(balance, "cr")
            credit_acc.save()
            debit_acc.entries.add(entry)
            debit_acc.updateBalance(balance, "db")
            debit_acc.save()
            user.entries.add(entry)
            user.save()

    form = EntryForm(user)
    entries = user.entries.all()
    data = {
        "page": "Dashboard",
        "title": "home",
        "form": form,
        "entries": entries,
        "cash": cash
    }
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
                "status": type,
                "form": AccountForm()
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
    cash = user.accounts.get(name='Cash')
    data = {
        "page": "Accounts",
        "title": "accounts",
        "accounts": user.accounts.all(),
        "cash": cash
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


@login_required()
def resetAccounts(request):
    user = AccuUser.objects.get(username=request.user.username)
    for entry in user.entries.all():
        entry.delete()
    for account in user.accounts.all():
        account.total = 0
        account.save()
    return redirect(reverse("home"))


@login_required()
def deleteEntry(request, id):
    user = AccuUser.objects.get(username=request.user.username)
    entries = user.entries.filter(id=id)
    if entries.count() > 0:
        entry = entries.first()
        balance = entry.amount
        entry.credit.updateBalance(balance, 'db')
        entry.credit.save()
        entry.debit.updateBalance(balance, 'cr')
        entry.debit.save()
        entry.delete()
    return redirect(reverse('home'))


@login_required()
def accountDetails(request, id):
    user = AccuUser.objects.get(username=request.user.username)
    accounts = user.accounts.filter(id=id)
    if accounts.count() > 0:
        account = accounts.first()
        entries = account.entries.all()
        data = {
            "account": account,
            "entries": entries,
            "page": "Account Details",
            "title": account.name,
        }
        return render(request, 'accountDetail.html', data)


@login_required()
def profile(request, username):
    if request.user.username == username:
        user = AccuUser.objects.get(username=username)
        if request.POST:
            form = RegistrationForm()
            if form.is_valid():
                print("Yup ...")
        data = {
            "page": "Profile",
            "title": user.fullName(),
            'form': RegistrationForm(
                initial={"username": user.username, "email": user.email, "currency": user.currency,
                         "first_name": user.first_name, "last_name": user.last_name})
        }
        return render(request, 'profile.html', data)
    return redirect(reverse('home'))
