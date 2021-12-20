# Generated by Django 3.2.8 on 2021-12-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moh_profile', '0010_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_title', models.CharField(max_length=100)),
                ('document_image', models.ImageField(default='doctor.jpg', upload_to='static/images')),
                ('document_url', models.FileField(upload_to='static/images')),
                ('document_published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
