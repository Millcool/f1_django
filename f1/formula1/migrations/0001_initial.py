# Generated by Django 5.0 on 2023-12-16 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grand_slam', models.IntegerField()),
                ('fastest_lap_count', models.IntegerField()),
                ('races_count', models.IntegerField()),
                ('wins_count', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('race_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_sprint', models.BooleanField()),
                ('datetime_of_race', models.DateTimeField()),
                ('datetime_of_quali', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('team_wins', models.IntegerField()),
                ('team_races', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=200)),
                ('track_country', models.CharField(max_length=200)),
                ('track_city', models.CharField(max_length=200)),
                ('length', models.FloatField()),
                ('description', models.TextField()),
                ('track_best_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.IntegerField()),
                ('position_quali', models.IntegerField()),
                ('position_sprint', models.IntegerField()),
                ('race_time', models.TimeField()),
                ('quali_time', models.TimeField()),
                ('points_race', models.FloatField()),
                ('points_sprint', models.FloatField()),
                ('fastest_lap', models.BooleanField()),
                ('dnf', models.BooleanField()),
                ('dnf_sprint', models.BooleanField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formula1.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formula1.race')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formula1.team'),
        ),
        migrations.AddField(
            model_name='driver',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formula1.team'),
        ),
        migrations.AddField(
            model_name='race',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formula1.track'),
        ),
    ]