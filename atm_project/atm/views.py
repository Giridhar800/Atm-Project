from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account, Transaction

def home(request):
    return HttpResponse("Welcome to the ATM")

def balance(request):
    if request.method == 'POST':
        account_number = request.POST['account_number']
        try:
            account = Account.objects.get(account_number=account_number)
            balance = account.balance
            return render(request, 'balance.html', {'balance': balance})
        except Account.DoesNotExist:
            return HttpResponse("Account not found")

    return render(request, 'balance_form.html')

def withdraw(request):
    if request.method == 'POST':
        account_number = request.POST['account_number']
        amount = int(request.POST['amount'])
        try:
            account = Account.objects.get(account_number=account_number)
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                Transaction.objects.create(account=account, amount=-amount, transaction_type='Withdrawal')
                return HttpResponse("Withdrawal successful")
            else:
                return HttpResponse("Insufficient balance")
        except Account.DoesNotExist:
            return HttpResponse("Account not found")

    return render(request, 'withdraw_form.html')

def deposit(request):
    if request.method == 'POST':
        account_number = request.POST['account_number']
        amount = int(request.POST['amount'])
        try:
            account = Account.objects.get(account_number=account_number)
            account.balance += amount
            account.save()
            Transaction.objects.create(account=account, amount=amount, transaction_type='Deposit')
            return HttpResponse("Deposit successful")
        except Account.DoesNotExist:
            return HttpResponse("Account not found")

    return render(request, 'deposit_form.html')



# python manage.py shell
# from atm.models import Account
# Account.objects.create(account_number='1234567890', balance=1000.00)
# exit()


