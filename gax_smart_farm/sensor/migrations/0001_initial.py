# Generated by Django 3.0.6 on 2020-05-24 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('irrigation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=255)),
                ('longitude', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(choices=[('valve', 'Valvula'), ('moisture', 'Humedad'), ('other', 'Otra')], max_length=255)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node', to='irrigation.Sector')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'node',
            },
        ),
        migrations.CreateModel(
            name='Moisture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moisture', to='sensor.Node')),
            ],
            options={
                'db_table': 'moisture',
            },
        ),
    ]
