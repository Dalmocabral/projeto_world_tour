from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib import messages
from .models import Award
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
# Create your views here.


def index(request):
    return render(request, 'accounts/index.html')

# Página de login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login em vez de login para evitar conflitos
            return redirect('dashboard')
        else:
            messages.error(request, 'Email or password is incorrect')
            return redirect('login')
    return render(request, 'accounts/login.html')

# Página de logout
def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco           
            return redirect('login')  # Redireciona para a página de login (ou qualquer outra página)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def list_awards(request):
    list_awards = Award.objects.all()

    context = {
        'list_awards': list_awards
    }

    return render(request, 'accounts/list_awards.html', context)


def my_awards(request):
    return render(request, 'accounts/my_awards.html')