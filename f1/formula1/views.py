from .models import Result, Race, Driver, Team
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
import time
import datetime

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
    teams = Team.objects.all()  # Получение всех команд
    return render(request, 'drivers_info.html', {'drivers': drivers, 'teams': teams})


def driver_info(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    return render(request, 'driver_info.html', {'driver': driver})
def add_driver(request):
    if request.method == "POST":
        name = request.POST.get('name')
        abbreviation = request.POST.get('abbreviation')
        team_id = request.POST.get('team')
        grand_slam = request.POST.get('grand_slam')
        fastest_lap_count = request.POST.get('fastest_lap_count')
        races_count = request.POST.get('races_count')
        wins_count = request.POST.get('wins_count')

        team = Team.objects.get(id=team_id)

        new_driver = Driver(
            name=name,
            abbreviation=abbreviation,
            team=team,
            grand_slam=int(grand_slam),
            fastest_lap_count=int(fastest_lap_count),
            races_count=int(races_count),
            wins_count=int(wins_count),
        )

        new_driver.save()
        drivers = Driver.objects.all()  # Получение всех гонщиков
        teams = Team.objects.all()  # Получение всех команд
        return redirect('drivers_info') 

def team_info_view(request, team_id):
    team = get_object_or_404(Team,  pk=team_id)
    return render(request, 'team_info.html', {'team': team})

def teams_info(request):
    teams = Team.objects.all()  # Получение всех гонщиков
    return render(request, 'teams_info.html', {'teams': teams})

def add_team(request):
    if request.method == "POST":
        team_name = request.POST.get('team_name')
        team_wins = request.POST.get('team_wins')
        team_races = request.POST.get('team_races')
        description = request.POST.get('description')

        new_team = Team(
            team_name=team_name,
            team_wins=team_wins,
            team_races=team_races,
            description=description
        )
        
        new_team.save()

        return redirect('teams_info') 
    

def delete_team(request, team_id):
    if request.method == "POST":
        team = Team.objects.get(id=team_id)
        team.delete()
        return redirect('teams_info') # Redirect to the teams list page

    # Redirect or show an error if not a POST request
    return redirect('teams_info')


def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == "POST":
        # Update team with new data from form
        team.team_name = request.POST.get('team_name')
        team.team_wins = request.POST.get('team_wins')
        team.team_races = request.POST.get('team_races')
        team.description = request.POST.get('description')
        team.save()

        # Redirect to team info or list
        return redirect('teams_info')
