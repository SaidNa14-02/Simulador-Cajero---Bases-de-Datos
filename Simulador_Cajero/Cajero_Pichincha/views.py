from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserCreationForm, AccountCreationForm
from .forms import LoginForm
from .models import User, Account

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(
        {                        
        },
        request))

from .forms import LoginForm  # Agregar esta línea

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
    user = request.user
    account = Account.objects.filter(user=user).first()
    return render(request, 'display_bank_services.html', {'account': account})



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
    return render(request, 'register.html', {'user_form': user_form, 'account_form': account_form})

