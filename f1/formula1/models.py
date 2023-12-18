from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_wins = models.IntegerField()
    team_races = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.team_name


class Track(models.Model):
    track_name = models.CharField(max_length=200)
    track_country = models.CharField(max_length=200)
    track_city = models.CharField(max_length=200)
    length = models.FloatField()
    description = models.TextField()
    track_best_time = models.TimeField()

    def __str__(self):
        return self.track_name


class Race(models.Model):
    race_id = models.AutoField(primary_key=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    is_sprint = models.BooleanField()
    datetime_of_race = models.DateTimeField()
    datetime_of_quali = models.DateTimeField()

    def __str__(self):
        return f"{self.race_id} - {self.track}"


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    grand_slam = models.IntegerField()
    fastest_lap_count = models.IntegerField()
    races_count = models.IntegerField()
    wins_count = models.IntegerField()
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    position = models.IntegerField()
    position_quali = models.IntegerField()
    position_sprint = models.IntegerField()
    race_time = models.TimeField()
    quali_time = models.TimeField()
    points_race = models.FloatField()
    points_sprint = models.FloatField()
    fastest_lap = models.BooleanField()
    dnf = models.BooleanField()
    dnf_sprint = models.BooleanField()

    def __str__(self):
        return f"{self.result_id} - {self.driver}"