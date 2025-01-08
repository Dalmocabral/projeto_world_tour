from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib import messages
from .models import Award, UserAward, PirepsFlight
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')
def list_awards(request):
    list_awards = Award.objects.all()

    context = {
        'list_awards': list_awards
    }

    return render(request, 'accounts/list_awards.html', context)



@login_required(login_url='login')
def award_detail(request, award_id):
    # Obtém o objeto Award pelo ID
    award = get_object_or_404(Award, id=award_id)
    user = request.user

    # Obtém UserAward relacionado ao usuário e ao prêmio
    user_award = UserAward.objects.filter(user=user, award=award).first()
    flights = PirepsFlight.objects.filter(pilot=user, status='Aprovado')

    # Calcula o progresso do prêmio
    flight_legs = award.flight_legs.all()
    for flight_leg in flight_legs:
        flight_leg.is_completed = False
        for flight in flights:
            # Verifica se o voo corresponde à perna
            if flight.departure_airport == flight_leg.from_airport and flight.arrival_airport == flight_leg.to_airport:
                flight_leg.is_completed = True
                break

    # Prepara o contexto
    context = {
        'award': award,
        'user_award': user_award,
        'flight_legs': flight_legs,
    }

    return render(request, 'accounts/award_detail.html', context)


@login_required(login_url='login')
def my_awards(request):
    return render(request, 'accounts/my_awards.html')