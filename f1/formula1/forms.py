from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Result, Race, Driver, Team, Track


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'wins', 'races', 'description']


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'team', 'grand_slam', 'fastest_lap_count', 'races_count', 'wins_count', 'abbreviation']


class RaceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = ['track', 'is_sprint', 'datetime_of_race', 'datetime_of_quali']


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['name', 'country', 'city', 'length', 'description', 'track_best_time']


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            'driver',
            'race',
            'position',
            'position_quali',
            'position_sprint',
            'race_time',
            'quali_time',
            'points_race',
            'points_sprint',
            'fastest_lap',
            'dnf',
            'dnf_sprint'
        ]
        widgets = {
            'race_time': forms.TimeInput(format='%H:%M:%S'),
            'quali_time': forms.TimeInput(format='%H:%M:%S'),
        }