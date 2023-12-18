from models import Team
from django.http import HttpResponse
from django.shortcuts import render
from .models import Race, Team, Driver, Track, Result
import time
import datetime
def race_list(request):
    races = Race.objects.all()
    # Create Track objects for the specified tracks
    # track_data = [
    #     {
    #         'track_name': 'Bahrain International Circuit',
    #         'track_country': 'Bahrain',
    #         'track_city': 'Sakhir',
    #         'length': 5412,
    #         'description': 'The Bahrain International Circuit is a motorsport venue opened in 2004 and used for drag racing, GP2 Series, and the annual Bahrain Grand Prix.',
    #         'track_best_time': datetime.time(0,1,27,264),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Circuit de Barcelona-Catalunya',
    #         'track_country': 'Spain',
    #         'track_city': 'Montmelo',
    #         'length': 4655,
    #         'description': 'The Circuit de Barcelona-Catalunya is a motorsport race track in Montmelo, Catalonia, Spain. It has hosted the Spanish Grand Prix.',
    #         'track_best_time': datetime.time(0, 1, 18, 149),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Circuit of the Americas',
    #         'track_country': 'USA',
    #         'track_city': 'Austin',
    #         'length': 5513,
    #         'description': 'The Circuit of the Americas is a grade 1 motor racing circuit in Elroy, Texas, near Austin. It hosted the United States Grand Prix.',
    #         'track_best_time': datetime.time(0,1,36,169),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Circuit Zandvoort',
    #         'track_country': 'Netherlands',
    #         'track_city': 'Zandvoort',
    #         'length': 4307,
    #         'description': 'Circuit Zandvoort is a motorsport race track located in the dunes north of Zandvoort, Netherlands. It hosted the Dutch Grand Prix.',
    #         'track_best_time': datetime.time(0, 1, 11, 97), # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Red Bull Ring',
    #         'track_country': 'Austria',
    #         'track_city': 'Spielberg',
    #         'length': 4318,
    #         'description': 'The Red Bull Ring is a motorsport race track in Spielberg, Styria, Austria. It hosts the Austrian Grand Prix.',
    #         'track_best_time': datetime.time(0, 1, 5, 619),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Azerbaijan Grand Prix City Circuit',
    #         'track_country': 'Azerbaijan',
    #         'track_city': 'Baku',
    #         'length': 6003,
    #         'description': 'The Baku City Circuit is a motor racing street circuit located in Baku, Azerbaijan. It hosted the Azerbaijan Grand Prix.',
    #         'track_best_time': datetime.time(0,1,43,9),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'French Grand Prix Circuit Paul Ricard',
    #         'track_country': 'France',
    #         'track_city': 'Le Castellet',
    #         'length': 5842,
    #         'description': 'Circuit Paul Ricard is a motorsport race track built in 1969 near Le Castellet, in Provence-Alpes-Côte d\'Azur, France. It hosts the French Grand Prix.',
    #         'track_best_time': datetime.time(0,1,32,40),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Austrian Grand Prix Red Bull Ring',
    #         'track_country': 'Austria',
    #         'track_city': 'Spielberg',
    #         'length': 4318,
    #         'description': 'The Red Bull Ring is a motorsport race track in Spielberg, Styria, Austria. It hosts the Austrian Grand Prix.',
    #         'track_best_time': datetime.time(0,1,5,619),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'British Grand Prix Silverstone Circuit',
    #         'track_country': 'UK',
    #         'track_city': 'Silverstone',
    #         'length': 5891,
    #         'description': 'Silverstone Circuit is a motor racing circuit in England, near the villages of Silverstone and Whittlebury. It hosts the British Grand Prix.',
    #         'track_best_time': datetime.time(0,1,27,97),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Hungarian Grand Prix Hungaroring',
    #         'track_country': 'Hungary',
    #         'track_city': 'Budapest',
    #         'length': 4381,
    #         'description': 'The Hungaroring is a Hungarian motor racing track near Budapest. It has been the home of the Hungarian Grand Prix since 1986.',
    #         'track_best_time': datetime.time(0,1,13,447),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Belgian Grand Prix Circuit de Spa-Francorchamps',
    #         'track_country': 'Belgium',
    #         'track_city': 'Stavelot',
    #         'length': 7004,
    #         'description': 'Circuit de Spa-Francorchamps is a motor racing circuit located in Stavelot, Belgium. It hosts the Belgian Grand Prix.',
    #         'track_best_time': datetime.time(0,1,46,286),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Dutch Grand Prix TT Circuit Assen',
    #         'track_country': 'Netherlands',
    #         'track_city': 'Assen',
    #         'length': 4542,
    #         'description': 'TT Circuit Assen is a motorsport race track built in 1955 and located in Assen, Netherlands. It hosted the Dutch Grand Prix.',
    #         'track_best_time': datetime.time(0,1,32,647),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Italian Grand Prix Autodromo Nazionale di Monza',
    #         'track_country': 'Italy',
    #         'track_city': 'Monza',
    #         'length': 5793,
    #         'description': 'Autodromo Nazionale di Monza is a historic race track near the city of Monza, Italy. It hosts the Italian Grand Prix.',
    #         'track_best_time': datetime.time(0,1,21,46),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Russian Grand Prix Sochi Autodrom',
    #         'track_country': 'Russia',
    #         'track_city': 'Sochi',
    #         'length': 5848,
    #         'description': 'Sochi Autodrom is a motorsport race track located in Sochi, Russia. It hosted the Russian Grand Prix.',
    #         'track_best_time': datetime.time(0,1,35,761),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Turkey Grand Prix Istanbul Park',
    #         'track_country': 'Turkey',
    #         'track_city': 'Istanbul',
    #         'length': 5338,
    #         'description': 'Istanbul Park is a motor racing circuit in Tuzla, east of Istanbul, Turkey. It hosted the Turkish Grand Prix.',
    #         'track_best_time':  datetime.time(0,1,24,770),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Brazilian Grand Prix Autódromo José Carlos Pace',
    #         'track_country': 'Brazil',
    #         'track_city': 'Sao Paulo',
    #         'length': 4309,
    #         'description': 'Autódromo José Carlos Pace is a motorsport circuit located in the city of São Paulo, Brazil. It hosts the Brazilian Grand Prix.',
    #         'track_best_time':  datetime.time(0,1,11,44),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Saudi Arabian Grand Prix Jeddah Corniche Circuit',
    #         'track_country': 'Saudi Arabia',
    #         'track_city': 'Jeddah',
    #         'length': 6272,
    #         'description': 'Jeddah Corniche Circuit is a motorsport street circuit located on the Red Sea in Jeddah, Saudi Arabia. It hosted the Saudi Arabian Grand Prix.',
    #         'track_best_time':  datetime.time(0,1,30,252),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Abu Dhabi Grand Prix Yas Marina Circuit',
    #         'track_country': 'UAE',
    #         'track_city': 'Abu Dhabi',
    #         'length': 5554,
    #         'description': 'Yas Marina Circuit is the venue for the Abu Dhabi Grand Prix. It is located on Yas Island, about 30 minutes from the capital of the UAE, Abu Dhabi.',
    #         'track_best_time':  datetime.time(0,1,39,283),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Alberta Motor Speedway Edmonton',
    #         'track_country': 'Canada',
    #         'track_city': 'Edmonton',
    #         'length': 3290,
    #         'description': 'Alberta Motor Speedway is a motor racing circuit located in Edmonton, Alberta, Canada.',
    #         'track_best_time':  datetime.time(0,1,8,621),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Yas Marina Circuit Abu Dhabi',
    #         'track_country': 'UAE',
    #         'track_city': 'Abu Dhabi',
    #         'length': 5545,
    #         'description': 'Yas Marina Circuit is the venue for the Abu Dhabi Grand Prix. It is located on Yas Island, about 30 minutes from the capital of the UAE, Abu Dhabi.',
    #         'track_best_time':  datetime.time(0,1,39,283),  # Best time for any driver
    #     },
    #     {
    #         'track_name': 'Sao Paulo Street Circuit',
    #         'track_country': 'Brazil',
    #         'track_city': 'Sao Paulo',
    #         'length': 4240,
    #         'description': 'Sao Paulo Street Circuit is a temporary street circuit located in the city of São Paulo, Brazil. It hosted the Brazilian Grand Prix.',
    #         'track_best_time':  datetime.time(0,1,11,44),  # Best time for any driver
    #     },
    # ]
    #
    # # Create Track instances for each track in the list
    # for track_info in track_data:
    #     Track.objects.create(**track_info)

    # race_data = [{
    #     'track': Track.objects.get(track_name='Bahrain International Circuit'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 3, 23, 10, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 3, 24, 14, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Circuit of the Americas'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 4, 1, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 3, 2, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Circuit Zandvoort'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 4, 15, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 3, 16, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Red Bull Ring'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 4, 23, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 3, 24, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Azerbaijan Grand Prix City Circuit'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 5, 7, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 5, 8, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='French Grand Prix Circuit Paul Ricard'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 5, 25, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 6, 26, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Austrian Grand Prix Red Bull Ring'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 7, 14, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 7, 15, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='British Grand Prix Silverstone Circuit'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 7, 23, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 7, 24, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Hungarian Grand Prix Hungaroring'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 8, 13, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 8, 14, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Belgian Grand Prix Circuit de Spa-Francorchamps'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 8, 24, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 8, 25, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Dutch Grand Prix TT Circuit Assen'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 9, 4, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 9, 5, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Italian Grand Prix Autodromo Nazionale di Monza'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 9, 13, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 9, 14, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Russian Grand Prix Sochi Autodrom'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 9, 20, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 9, 21, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Turkey Grand Prix Istanbul Park'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 10, 7, 14, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 10, 8, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Brazilian Grand Prix Autódromo José Carlos Pace'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 10, 15, 22, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 10, 16, 20, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Saudi Arabian Grand Prix Jeddah Corniche Circuit'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 10, 23, 18, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 10, 24, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Abu Dhabi Grand Prix Yas Marina Circuit'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 11, 15, 18, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 11, 16, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Alberta Motor Speedway Edmonton'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 12, 4, 18, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 12, 5, 18, 0),
    # },
    # {
    #     'track': Track.objects.get(track_name='Yas Marina Circuit Abu Dhabi'),  # you should provide the track instance here, or create a new one if needed
    #     'is_sprint': False,
    #     'datetime_of_race': datetime.datetime(2023, 12, 15, 18, 0),
    #     'datetime_of_quali': datetime.datetime(2023, 12, 16, 18, 0),
    # }]
    # for race_info in race_data:
    #     Race.objects.create(**race_info)

    # drivers_data = [
    #     {'team': 'Mercedes', 'grand_slam': 12, 'fastest_lap_count': 65, 'races_count': 446, 'wins_count': 103,
    #      'name': 'Lewis Hamilton', 'abbreviation': 'HAM'},
    #     {'team': 'Mercedes', 'grand_slam': 0, 'fastest_lap_count': 1, 'races_count': 156, 'wins_count': 0,
    #      'name': 'George Russel', 'abbreviation': 'RUS'},
    #
    #     {'team': 'Red Bull Racing', 'grand_slam': 8, 'fastest_lap_count': 46, 'races_count': 234, 'wins_count': 54,
    #      'name': 'Max Verstappen', 'abbreviation': 'VER'},
    #     {'team': 'Red Bull Racing', 'grand_slam': 0, 'fastest_lap_count': 1, 'races_count': 298, 'wins_count': 4,
    #      'name': 'Sergio Perez', 'abbreviation': 'PER'},
    #
    #     {'team': 'Ferrari', 'grand_slam': 1, 'fastest_lap_count': 8, 'races_count': 249, 'wins_count': 6,
    #      'name': 'Charles Leclerc', 'abbreviation': 'LEC'},
    #     {'team': 'Ferrari', 'grand_slam': 1, 'fastest_lap_count': 8, 'races_count': 249, 'wins_count': 6,
    #      'name': 'Carlos Sainz', 'abbreviation': 'SAI'},
    #
    #     {'team': 'McLaren', 'grand_slam': 0, 'fastest_lap_count': 0, 'races_count': 146, 'wins_count': 0,
    #      'name': 'Lando Noris', 'abbreviation': 'NOR'},
    #     {'team': 'McLaren', 'grand_slam': 0, 'fastest_lap_count': 0, 'races_count': 46, 'wins_count': 0,
    #      'name': 'Oscar Piastri', 'abbreviation': 'PIA'},
    #
    #     {'team': 'Alfa Romeo', 'grand_slam': 0, 'fastest_lap_count': 2, 'races_count': 340, 'wins_count': 7,
    #      'name': 'Valtteri Bottas', 'abbreviation': 'BOT'},
    #     {'team': 'Alfa Romeo', 'grand_slam': 0, 'fastest_lap_count': 0, 'races_count': 67, 'wins_count': 0,
    #      'name': 'Guanio Zhou', 'abbreviation': 'ZHO'},
    #
    #     {'team': 'AlphaTauri', 'grand_slam': 0, 'fastest_lap_count': 3, 'races_count': 218, 'wins_count': 6,
    #      'name': 'Daniel Ricciardo', 'abbreviation': 'RIC'},
    #     {'team': 'AlphaTauri', 'grand_slam': 0, 'fastest_lap_count': 0, 'races_count': 93, 'wins_count': 0,
    #      'name': 'Yuki Tsunoda', 'abbreviation': 'TSU'},
    #
    #     {'team': 'Aston Martin', 'grand_slam': 0, 'fastest_lap_count': 9, 'races_count': 361, 'wins_count': 34,
    #      'name': 'Fernando Alonso', 'abbreviation': 'ALO'},
    #     {'team': 'Aston Martin', 'grand_slam': 0, 'fastest_lap_count': 1, 'races_count': 123, 'wins_count': 0,
    #      'name': 'Lance Stroll', 'abbreviation': 'STR'},
    #
    #     {'team': 'Haas', 'grand_slam': 0, 'fastest_lap_count': 0, 'races_count': 189, 'wins_count': 0,
    #      'name': 'Niko Hulkenberg', 'abbreviation': 'HUL'},
    #     {'team': 'Haas', 'grand_slam': 0, 'fastest_lap_count': 1, 'races_count': 207, 'wins_count': 0,
    #      'name': 'Kevin Magnusen', 'abbreviation': 'MAG'},
    #
    #     {'team': 'Alpine', 'grand_slam': 0, 'fastest_lap_count': 1, 'races_count': 123, 'wins_count': 1,
    #      'name': 'Pierre Gasly', 'abbreviation': 'GAS'},
    #     {'team': 'Alpine', 'grand_slam': 0, 'fastest_lap_count': 1, 'races_count': 183, 'wins_count': 1,
    #      'name': 'Esteban Ocon', 'abbreviation': 'OCO'},
    #
    #     {'team': 'Williams', 'grand_slam': 0, 'fastest_lap_count': 0, 'races_count': 143, 'wins_count': 0,
    #      'name': 'Alex Albon', 'abbreviation': 'ALB'},
    #     {'team': 'Williams', 'grand_slam': 0, 'fastest_lap_count': 0, 'races_count': 23, 'wins_count': 0,
    #      'name': 'Louson Sergeant', 'abbreviation': 'SER'}
    #]
    # for driver_data in drivers_data:
    #     team, _ = Team.objects.get_or_create(team_name=driver_data['team'])
    #     driver, _ = Driver.objects.get_or_create(team=team, name=driver_data['name'],
    #                                              abbreviation=driver_data['abbreviation'],
    #                                              grand_slam =  driver_data['grand_slam'],
    #                                              fastest_lap_count = driver_data['fastest_lap_count'],
    #                                              races_count = driver_data['races_count'],
    #                                              wins_count = driver_data['wins_count'])
    #     driver.save()
    #Team.objects.bulk_create([Driver(team=team['team'], grand_slam=team['grand_slam'],
    #                               fastest_lap_count=team['fastest_lap_count'], races_count=team['races_count'], wins_count = team['races_count'], name = team['name'], abbreviation = team['abbreviation']) for team in drivers_data])
    # result = [{
    #     'driver': Driver.objects.get(id=1),
    #     'race': Race.objects.get(race_id = 1),
    #     'position': 1,
    #     'position_quali': 2,
    #     'position_sprint': 1,
    #     'race_time': datetime.time(1, 30, 45),  # Replace with actual race time
    #     'quali_time': datetime.time(0, 1, 15, 34),  # Replace with actual quali time
    #     'points_race': 25.0,
    #     'points_sprint': 3.0,
    #     'fastest_lap': True,
    #     'dnf': False,
    #     'dnf_sprint': False,
    # },
    # {
    #     'driver': Driver.objects.get(id=2),
    #     'race': Race.objects.get(race_id=1),
    #     'position': 2,
    #     'position_quali': 1,
    #     'position_sprint': 1,
    #     'race_time': datetime.time(1, 30, 55),  # Replace with actual race time
    #     'quali_time': datetime.time(0, 1, 15, 412),  # Replace with actual quali time
    #     'points_race': 18.0,
    #     'points_sprint': 2.0,
    #     'fastest_lap': False,
    #     'dnf': False,
    #     'dnf_sprint': False,
    # },
    # {
    #     'driver': Driver.objects.get(id=3),
    #     'race': Race.objects.get(race_id=1),
    #     'position': 3,
    #     'position_quali': 3,
    #     'position_sprint': 3,
    #     'race_time': datetime.time(1, 31, 00),  # Replace with actual race time
    #     'quali_time': datetime.time(0, 1, 15, 546),  # Replace with actual quali time
    #     'points_race': 15.0,
    #     'points_sprint': 1.0,
    #     'fastest_lap': False,
    #     'dnf': False,
    #     'dnf_sprint': False,
    # },
    #     {
    #         'driver': Driver.objects.get(id=4),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 4,
    #         'position_quali': 4,
    #         'position_sprint': 4,
    #         'race_time': datetime.time(1, 31, 50),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 15, 681),  # Replace with actual quali time
    #         'points_race': 12.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=5),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 5,
    #         'position_quali': 5,
    #         'position_sprint': 5,
    #         'race_time': datetime.time(1, 31, 42),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 15, 793),  # Replace with actual quali time
    #         'points_race': 10.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=6),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 7,
    #         'position_quali': 8,
    #         'position_sprint': 6,
    #         'race_time': datetime.time(1, 32, 45),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 16, 65),  # Replace with actual quali time
    #         'points_race': 6.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=7),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 6,
    #         'position_quali': 7,
    #         'position_sprint': 7,
    #         'race_time': datetime.time(1, 32, 55),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 16, 96),  # Replace with actual quali time
    #         'points_race': 8.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=8),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 8,
    #         'position_quali': 16,
    #         'position_sprint': 8,
    #         'race_time': datetime.time(1, 33, 1),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 16, 961),  # Replace with actual quali time
    #         'points_race': 4.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=9),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 9,
    #         'position_quali': 9,
    #         'position_sprint': 9,
    #         'race_time': datetime.time(1, 33, 11),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 16, 999),  # Replace with actual quali time
    #         'points_race': 2.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=10),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 20,
    #         'position_quali': 10,
    #         'position_sprint': 10,
    #         'race_time': datetime.time(1, 34, 11),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 17, 56),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': True,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=11),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 11,
    #         'position_quali': 11,
    #         'position_sprint': 14,
    #         'race_time': datetime.time(1, 34, 56),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 17, 569),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=12),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 10,
    #         'position_quali': 19,
    #         'position_sprint': 15,
    #         'race_time': datetime.time(1, 34, 16),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 18, 76),  # Replace with actual quali time
    #         'points_race': 1.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=13),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 13,
    #         'position_quali': 13,
    #         'position_sprint': 13,
    #         'race_time': datetime.time(1, 34, 31),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 18, 92),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=14),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 14,
    #         'position_quali': 14,
    #         'position_sprint': 14,
    #         'race_time': datetime.time(1, 34, 51),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 18, 999),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=15),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 15,
    #         'position_quali': 18,
    #         'position_sprint': 20,
    #         'race_time': datetime.time(1, 34, 35),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 19, 461),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=16),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 16,
    #         'position_quali': 19,
    #         'position_sprint': 19,
    #         'race_time': datetime.time(1, 34, 37),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 19, 477),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=17),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 17,
    #         'position_quali': 16,
    #         'position_sprint': 18,
    #         'race_time': datetime.time(1, 34, 47),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 19, 877),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=18),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 18,
    #         'position_quali': 17,
    #         'position_sprint': 17,
    #         'race_time': datetime.time(1, 34, 54),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 19, 894),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #     {
    #         'driver': Driver.objects.get(id=19),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 19,
    #         'position_quali': 16,
    #         'position_sprint': 12,
    #         'race_time': datetime.time(1, 34, 56),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 19, 898),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },
    #      {
    #         'driver': Driver.objects.get(id=20),
    #         'race': Race.objects.get(race_id=1),
    #         'position': 12,
    #         'position_quali': 16,
    #         'position_sprint': 20,
    #         'race_time': datetime.time(1, 33, 56),  # Replace with actual race time
    #         'quali_time': datetime.time(0, 1, 19, 899),  # Replace with actual quali time
    #         'points_race': 0.0,
    #         'points_sprint': 0.0,
    #         'fastest_lap': False,
    #         'dnf': False,
    #         'dnf_sprint': False,
    #     },]
    # for result_info in result:
    #     Result.objects.create(**result_info)
    return render(request, 'race_list.html', {'races': races})

teams = [
    {"team_name": "Mercedes", "team_wins": 450, "team_races": 2000, "description": "A German automobile manufacturer and racing team."},
    {"team_name": "Ferrari", "team_wins": 288, "team_races": 2000, "description": "An Italian sports automobile manufacturer and racing team."},
    {"team_name": "Red Bull Racing", "team_wins": 214, "team_races": 2000, "description": "An Austrian-British automobile manufacturer and racing team."},
    {"team_name": "McLaren", "team_wins": 211, "team_races": 2000, "description": "A British automobile manufacturer and racing team."},
    {"team_name": "Renault", "team_wins": 201, "team_races": 2000, "description": "A French multinational automobile and cycling manufacturer."},
    {"team_name": "Alpine", "team_wins": 0, "team_races": 0, "description": "A French automobile manufacturer."},
    {"team_name": "Williams", "team_wins": 147, "team_races": 2000, "description": "A British Formula One motor racing team."},
    {"team_name": "Aston Martin", "team_wins": 0, "team_races": 0, "description": "A British luxury sports car manufacturer."},
    {"team_name": "Alfa Romeo", "team_wins": 0, "team_races": 0, "description": "An Italian manufacturer of automobiles and other vehicles."},
    {"team_name": "Haas", "team_wins": 13, "team_races": 2000, "description": "An American-Italian racing team."},
]

Team.objects.bulk_create([Team(team_name=team['team_name'], team_wins=team['team_wins'], team_races=team['team_races'], description=team['description']) for team in teams])