from django import forms
from django.forms import ModelForm
from .models import Covid19


class Covid19form(ModelForm):
    class Meta:
        model = Covid19
        fields = ('new_cases','active_cases','new_recovered','currently_admitted','new_tests_conducted','new_discharges','new_deaths')
