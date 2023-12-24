from .models import Result, Race, Driver, Team, Track
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, TeamForm, DriverForm, RaceForm, TrackForm, ResultForm
from django.contrib.auth import login, authenticate
from django.utils.dateparse import parse_datetime
from django.utils.dateparse import parse_time
import time
import datetime




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


def grand_prix_results(request):
    races = Race.objects.all()
    tracks = Track.objects.all()
    return render(request, 'grand_prix_results.html', {'races': races, 'tracks':tracks})


def add_race(request):
    if request.method == "POST":
        track_id = request.POST.get('track')
        datetime_of_race = request.POST.get('datetime_of_race')
        datetime_of_quali = request.POST.get('datetime_of_quali')
        is_sprint = request.POST.get('is_sprint') == 'on'

        track = Track.objects.get(id=track_id)

        new_race = Race(
            track=track,
            datetime_of_race=parse_datetime(datetime_of_race),
            datetime_of_quali=parse_datetime(datetime_of_quali),
            is_sprint=is_sprint,
        )

        new_race.save()
        return redirect('grand_prix_results')  # Перенаправление на страницу со списком гонок

    # Если метод не POST, возвращаем форму для добавления гонки
    return render(request, 'race_add.html')


def race_results_view(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    results = Result.objects.filter(race=race).order_by('position')
    drivers = Driver.objects.all()
    return render(request, 'race_result.html', {'race': race, 'results': results, 'drivers': drivers})


def delete_race(request, race_id):
    if request.method == "POST":
        race = Race.objects.get(id=race_id)
        race.delete()
        return redirect('grand_prix_results')

    return redirect('grand_prix_results')


def edit_race(request, race_id):
    race = get_object_or_404(Race, id=race_id)

    if request.method == 'POST':
        form = RaceForm(request.POST, instance=race)
        if form.is_valid():
            form.save()
            return redirect('race_results', race_id=race.id)

    else:
        form = RaceForm(instance=race)
    return render(request, 'race_edit.html', {'form': form})


def delete_result(request, result_id):
    result = Result.objects.get(id=result_id)
    if request.method == "POST":
        result.delete()
        return redirect('race_results', race_id=result.race.id)

    return redirect('race_results', race_id=result.race.id)


def edit_result(request, result_id):
    result = get_object_or_404(Result, id=result_id)

    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('race_results', race_id=result.race.id)

    else:
        form = ResultForm(instance=result)
    return render(request, 'result_edit.html', {'form': form})


def add_result(request):
    if request.method == "POST":
        driver_id = request.POST.get('driver')
        race_id = request.POST.get('race')
        position = request.POST.get('position')
        position_quali = request.POST.get('position_quali')
        position_sprint = request.POST.get('position_sprint')
        race_time = request.POST.get('race_time')
        quali_time = request.POST.get('quali_time')
        points_race = request.POST.get('points_race')
        points_sprint = request.POST.get('points_sprint')
        fastest_lap = request.POST.get('fastest_lap') == 'on'
        dnf = request.POST.get('dnf') == 'on'
        dnf_sprint = request.POST.get('dnf_sprint') == 'on'

        driver = Driver.objects.get(id=driver_id)
        race = Race.objects.get(id=race_id)

        new_result = Result(
            driver=driver,
            race=race,
            position=int(position),
            position_quali=int(position_quali),
            position_sprint=int(position_sprint),
            race_time=parse_time(race_time) if race_time else None,
            quali_time=parse_time(quali_time) if quali_time else None,
            points_race=float(points_race),
            points_sprint=float(points_sprint),
            fastest_lap=fastest_lap,
            dnf=dnf,
            dnf_sprint=dnf_sprint
        )

        new_result.save()
        return redirect('race_results', race_id=race.id)  # Перенаправление на страницу результатов гонки

    # Если метод не POST, возвращаем форму для добавления результата
    return render(request, 'result_add.html')

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


def delete_driver(request, driver_id):
    if request.method == "POST":
        driver = Driver.objects.get(id=driver_id)
        driver.delete()
        return redirect('drivers_info')

    return redirect('drivers_info')


def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_info', driver_id=driver.id)

    else:
        form = DriverForm(instance=driver)
    return render(request, 'driver_edit.html', {'form': form})



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
        return redirect('teams_info')

    return redirect('teams_info')


def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_info', team_id = team.id)

    else:
        form = TeamForm(instance=team)
    return render(request, 'team_edit.html', {'form': form})


def tracks_info(request):
    tracks = Track.objects.all()
    return render(request, 'tracks_info.html', {'tracks': tracks})


def track_info(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'track_info.html', {'track': track})


def add_track(request):
    if request.method == "POST":
        name = request.POST.get('name')
        country = request.POST.get('country')
        city = request.POST.get('city')
        length = request.POST.get('length')
        description = request.POST.get('description')
        track_best_time = request.POST.get('track_best_time')

        new_track = Track(
            name=name,
            country=country,
            city=city,
            length=float(length),
            description=description,
            track_best_time=track_best_time,
        )

        new_track.save()
        return redirect('tracks_info')  # Перенаправление на страницу со списком треков

    # Если метод не POST, возвращаем форму для добавления трека
    return render(request, 'track_add.html')


def delete_track(request, track_id):
    if request.method == "POST":
        track = Track.objects.get(id=track_id)
        track.delete()
        return redirect('tracks_info')  # Убедитесь, что у вас есть URL с именем 'tracks_info'

    return redirect('tracks_info')


def edit_track(request, track_id):
    track = get_object_or_404(Track, id=track_id)

    if request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return redirect('track_info', track_id=track.id)

    else:
        form = TrackForm(instance=track)
    return render(request, 'track_edit.html', {'form': form})

