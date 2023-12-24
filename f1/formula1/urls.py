from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .forms import UserLoginForm
app_name = ''

urlpatterns = [
#path('', views.race_list, name='home'),
#path('login/', views.LoginView, name='login'),
path('login/', LoginView.as_view(template_name='login.html', authentication_form=UserLoginForm), name='login'),
path('signup/', views.signup_view, name='signup'),


path('delete_race/<int:race_id>/', views.delete_race, name='delete_race'),
path('edit_race/<int:race_id>/', views.edit_race, name='edit_race'),
path('add_race/', views.add_race, name='add_race'),
path('grand-prix-results/', views.grand_prix_results, name='grand_prix_results'),

path('race-results/<int:race_id>/', views.race_results_view, name='race_results'),
path('delete_result/<int:result_id>/', views.delete_result, name='delete_result'),
path('edit_result/<int:result_id>/', views.edit_result, name='edit_result'),
path('add_result/', views.add_result, name='add_result'),

path('drivers-info/', views.drivers_info, name='drivers_info'),
path('driver-info/<int:driver_id>/', views.driver_info, name='driver_info'),
path('add_driver/', views.add_driver, name='add_driver'),
path('delete_driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
path('edit_driver/<int:driver_id>/', views.edit_driver, name='edit_driver'),

path('teams-info/', views.teams_info, name='teams_info'),
path('team-info/<int:team_id>/', views.team_info_view, name='team_info'),
path('add_team/', views.add_team, name='add_team'),
path('delete_team/<int:team_id>/', views.delete_team, name='delete_team'),
path('edit_team/<int:team_id>/', views.edit_team, name='edit_team'),


path('tracks-info/', views.tracks_info, name='tracks_info'),
path('track-info/<int:track_id>/', views.track_info, name='track_info'),
path('add_track/', views.add_track, name='add_track'),
path('delete_track/<int:track_id>/', views.delete_track, name='delete_track'),
path('edit_track/<int:track_id>/', views.edit_track, name='edit_track'),

path('', views.home, name='home'),  # Home page
]