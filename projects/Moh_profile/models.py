from django.db import models

# Create your models here.


class Health_Priorities(models.Model):
    disease = models.CharField(max_length=100)
    priority = models.IntegerField()
    content_url = models.CharField(max_length=300)

    def __str__(self):
        return str(self.disease)
        return str(self.priorities)
        return str(self.content_url)


class Covid19(models.Model):
    new_cases = models.IntegerField()
    cumulative_confirmed_cases = models.IntegerField()
    active_cases = models.IntegerField()
    total_recovered = models.IntegerField()
    currently_admitted_in_treatment_units = models.IntegerField()
    new_discharges_from_treatment_units = models.IntegerField()
    total_tests_conducted = models.IntegerField()
    total_deaths = models.IntegerField()
    new_cases_date = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plural = 'Covid19'

    def __str__(self):
        return str(self.new_cases)
        return str(self.cumulative_confirmed_cases)
        return str(self.active_cases)
        return str(self.total_recovered)
        return str(self.currently_admitted_in_treatment_units)
        return str(self.new_discharges_from_treatment_units)
        return str(self.total_tests_conducted)
        return str(self.total_deaths)
        return str(self.new_cases_date)


class Mohevents(models.Model):
    event_title = models.CharField(max_length=100)
    event_image = models.ImageField(default='doctor.jpg')
    Content_url = models.CharField(max_length=300)
    event_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.event_title)
        return str(self.event_image)
        return str(self.content_url)
        return str(self.event_date)
