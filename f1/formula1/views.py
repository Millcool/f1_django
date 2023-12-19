from .models import Result, Race, Driver, Team
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

def grand_prix_results(request):
    races = Race.objects.all()
    return render(request, 'grand_prix_results.html', {'races': races})


def home(request):
    races = Race.objects.all()
    return render(request, 'home.html', {'races': races})


def LoginView(request):
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def race_results_view(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    results = Result.objects.filter(race=race).order_by('position')
    return render(request, 'race_result.html', {'race': race, 'results': results})

def drivers_info(request):
    drivers = Driver.objects.all()  # Получение всех гонщиков
    return render(request, 'drivers_info.html', {'drivers': drivers})


def driver_info(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    return render(request, 'driver_info.html', {'driver': driver})


def team_info_view(request, team_id):
    team = get_object_or_404(Team,  pk=team_id)
    return render(request, 'team_info.html', {'team': team})

def teams_info(request):
    teams = Team.objects.all()  # Получение всех гонщиков
    return render(request, 'teams_info.html', {'teams': teams})
