from django.urls import path

from . import views

app_name = ''

urlpatterns = [
#path('', views.race_list, name='home'),
path('grand-prix-results/', views.grand_prix_results, name='grand_prix_results'),
]