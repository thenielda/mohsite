# Generated by Django 3.2.8 on 2021-12-14 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Moh_profile', '0014_eventcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='mohevents',
            name='event_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mohevents', to='Moh_profile.mohevents'),
        ),
        migrations.AlterModelTable(
            name='eventcategory',
            table='Eventcategory',
        ),
    ]