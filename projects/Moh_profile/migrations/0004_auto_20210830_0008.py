# Generated by Django 3.2.6 on 2021-08-29 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Moh_profile', '0003_covid19_health_priorities_mohevents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covid19',
            old_name='Currently_admitted_in_treatment_units',
            new_name='currently_admitted_in_treatment_units',
        ),
        migrations.RenameField(
            model_name='covid19',
            old_name='New_discharges_from_treatment_units',
            new_name='new_discharges_from_treatment_units',
        ),
        migrations.RenameField(
            model_name='covid19',
            old_name='Total_deaths',
            new_name='total_deaths',
        ),
    ]
