from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .forms import UserLoginForm
app_name = ''

urlpatterns = [
#path('', views.race_list, name='home'),
path('grand-prix-results/', views.grand_prix_results, name='grand_prix_results'),
#path('login/', views.LoginView, name='login'),
path('login/', LoginView.as_view(template_name='login.html', authentication_form=UserLoginForm), name='login'),
path('signup/', views.signup_view, name='signup'),
path('race-results/<int:race_id>/', views.race_results_view, name='race_results'),
path('drivers-info/', views.drivers_info, name='drivers_info'),
path('driver-info/<int:driver_id>/', views.driver_info, name='driver_info'),
path('teams-info/', views.teams_info, name='teams_info'),
path('team-info/<int:team_id>/', views.team_info_view, name='team_info'),
path('', views.home, name='home'),  # Home page
]