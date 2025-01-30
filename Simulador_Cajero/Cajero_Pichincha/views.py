from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
<<<<<<< HEAD
from .forms import CustomUserCreationForm, AccountCreationForm, LoginForm, DepositForm, WithdrawForm
=======
from .forms import CustomUserCreationForm, AccountCreationForm, LoginForm, TransferForm
>>>>>>> origin/main
import logging
from .models import User, Account, Transaction

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Cajero_Pichincha:display_bank_services')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def display_bank_services(request):
    user = User.objects.get(username=request.user)
    account = Account.objects.get(user=request.user)
    transactions = Transaction.objects.filter(account=account).order_by('-timestamp')[:3]
    return render(request, 'display_bank_services.html', {
        'user': user,
        'account': account,
        'transactions': transactions
    })

    logger = logging.getLogger(__name__)
    

def logout_view(request):
    print("Iniciando proceso de logout")  # Debug
    print(f"Usuario antes de logout: {request.user}")  # Debug
    
    try:
        logout(request)
        print(f"Usuario después de logout: {request.user}")  # Debug
        messages.success(request, 'Has cerrado sesión exitosamente')
        print("Redirigiendo a index")  # Debug
        return redirect('Cajero_Pichincha:index')
    except Exception as e:
        print(f"Error en logout: {str(e)}")  # Debug
        return redirect('Cajero_Pichincha:index')
    
def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        account_form = AccountCreationForm(request.POST)
        if user_form.is_valid() and account_form.is_valid():
            user = user_form.save()
            account = account_form.save(commit=False)
            account.user = user
            account.save()
            return redirect('Cajero_Pichincha:login')
    else:
        user_form = CustomUserCreationForm()
        account_form = AccountCreationForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'account_form': account_form
    })
<<<<<<< HEAD

@login_required
def deposit(request):
    account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            account.deposit(amount)
            Transaction.objects.create(
                account=account,
                transaction_type='DEPOSIT',
                amount=amount,
            )
            messages.success(request, f"Depósito de ${amount} realizado con éxito.")
            return redirect('Cajero_Pichincha:display_bank_services')
    else:
        form = DepositForm()

    return render(request, 'deposit.html', {'form': form, 'account': account})

@login_required
def withdraw(request):
    account = Account.objects.filter(user=request.user).first()
    
    if not account:
        messages.error(request, "No tienes una cuenta asociada.")
        return redirect('Cajero_Pichincha:display_bank_services')

    if request.method == "POST":
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']

            if amount > account.funds:
                messages.error(request, "Fondos insuficientes.")
            else:
                # Restar el dinero de la cuenta
                account.funds -= amount
                account.save()

                # Registrar la transacción
                Transaction.objects.create(
                    account=account,
                    transaction_type='withdraw',
                    amount=amount
                )

                messages.success(request, f"Has retirado ${amount} exitosamente.")
                return redirect('Cajero_Pichincha:display_bank_services')
    else:
        form = WithdrawForm()

    return render(request, 'withdraw.html', {'form': form, 'account': account})
=======
    
@login_required
def transfer_money(request):
    account = Account.objects.get(user=request.user)
    destination_account = None

    if request.method == 'POST':
        transfer_form = TransferForm(request.POST)
        if transfer_form.is_valid():
            try:
                amount = transfer_form.cleaned_data['amount']
                account_number = transfer_form.cleaned_data['account_number']
                destination_account = Account.objects.get(account_number=account_number)
                
                if account.funds >= amount:
                    account.funds -= amount
                    destination_account.funds += amount
                    
                    account.save()
                    destination_account.save()
                    
                    Transaction.objects.create(
                        account=account,
                        transaction_type='TRANSFERENCIA',
                        amount=amount,
                        destination=account_number
                    )
                    
                    return redirect('Cajero_Pichincha:display_bank_services')
                else:
                    transfer_form.add_error('amount', 'Fondos insuficientes')
                    
            except Account.DoesNotExist:
                transfer_form.add_error('account_number', 'La cuenta destino no existe')
    else:
        transfer_form = TransferForm()
        # Verificar cuenta destino cuando se ingresa
        account_number = request.GET.get('account_number')
        if account_number:
            try:
                destination_account = Account.objects.get(account_number=account_number)
            except Account.DoesNotExist:
                pass

    return render(request, 'display_transfer.html', {
        'transfer_form': transfer_form,
        'account': account,
        'destination_account': destination_account
    })
    
>>>>>>> origin/main
