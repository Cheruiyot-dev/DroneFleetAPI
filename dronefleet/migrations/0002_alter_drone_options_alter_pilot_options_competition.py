# Generated by Django 5.1 on 2024-08-24 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dronefleet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drone',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='pilot',
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_in_feet', models.IntegerField()),
                ('distance_achievement_date', models.DateTimeField()),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dronefleet.drone')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='dronefleet.pilot')),
            ],
            options={
                'ordering': ('-distance_in_feet',),
            },
        ),
    ]
