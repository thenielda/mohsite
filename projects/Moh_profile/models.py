from django.db import models

# Create your models here.


class Health_Priorities(models.Model):
    disease = models.CharField(max_length=100)
    priority = models.IntegerField()
    content_url = models.CharField(max_length=300)

    def __str__(self):
        return str(self.disease)
        return str(self.priority)
        return str(self.content_url)

        class meta:
            verbose_name_plural = 'Health_priorities'


class Covid19(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    new_cases = models.IntegerField()
    active_cases = models.IntegerField()
    new_recovered = models.IntegerField()
    currently_admitted = models.IntegerField()
    new_tests_conducted = models.IntegerField()
    new_discharges = models.IntegerField()
    new_deaths = models.IntegerField()

    class meta:
        db_table = 'covid19'

    def __str__(self):
        return str(self.date)
        return str(self.new_cases)
        return str(self.active_cases)
        return str(self.new_recovered)
        return str(self.currently_admitted)
        return str(self.new_tests_conducted)
        return str(self.new_discharges)
        return str(self.new_deaths)

class Eventcategory(models.Model):
    event_category = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'Eventcategory'

    def __str__(self):
        return str(self.event_category)


class Mohevents(models.Model):
    event_title = models.CharField(max_length=100)
    event_image = models.ImageField( null=False, blank=False)
    event_content = models.TextField(max_length=1000)
    event_date = models.DateTimeField(auto_now_add=True)
    event_category = models.ForeignKey('Mohevents', on_delete=models.CASCADE, null=True, blank=True,related_name = 'Mohevents')

    def __str__(self):
        return str(self.event_title)
        return str(self.event_image)
        return str(self.event_content)
        return str(self.event_date)
        return str(self.event_category)




class Documents(models.Model):
    document_title = models.CharField(max_length=100)
    document_image = models.ImageField(
        default='doctor.jpg', upload_to='static/images')
    document_url = models.FileField(upload_to='static/images')
    document_published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.document_title)
        return str(self.document_image)
        return str(self.document_url)
        return str(self.document_published_date)
