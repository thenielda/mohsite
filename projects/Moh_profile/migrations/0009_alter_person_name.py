# Generated by Django 3.2.8 on 2021-10-30 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moh_profile', '0008_auto_20211029_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
