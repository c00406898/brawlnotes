# Generated by Django 3.1.1 on 2021-10-22 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Official_1_Events',
            fields=[
                ('Year', models.IntegerField()),
                ('Region', models.CharField(choices=[('SEA', 'Southeast Asia'), ('AUS', 'Australia'), ('NA', 'North America'), ('EU', 'Europe'), ('SA', 'South America')], max_length=3)),
                ('EventName', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player_Registry',
            fields=[
                ('Region', models.CharField(choices=[('SEA', 'Southeast Asia'), ('AUS', 'Australia'), ('NA', 'North America'), ('EU', 'Europe'), ('SA', 'South America')], max_length=3)),
                ('BrawlhallaID', models.IntegerField()),
                ('SmashggName', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Placements_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField()),
                ('Region', models.CharField(choices=[('SEA', 'Southeast Asia'), ('AUS', 'Australia'), ('NA', 'North America'), ('EU', 'Europe'), ('SA', 'South America')], max_length=3)),
                ('PowerRank', models.IntegerField()),
                ('Placement', models.IntegerField()),
                ('Losses', models.CharField(max_length=100)),
                ('EventName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrawlNotes.official_1_events')),
                ('SmashggName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrawlNotes.player_registry')),
            ],
        ),
        migrations.CreateModel(
            name='Characters_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField()),
                ('Region', models.CharField(choices=[('SEA', 'Southeast Asia'), ('AUS', 'Australia'), ('NA', 'North America'), ('EU', 'Europe'), ('SA', 'South America')], max_length=3)),
                ('Characters', models.CharField(max_length=50)),
                ('NumGames', models.IntegerField()),
                ('EventName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrawlNotes.official_1_events')),
                ('SmashggName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrawlNotes.player_registry')),
            ],
        ),
    ]
