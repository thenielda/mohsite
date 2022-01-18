from django.db import models


# Create your models here.


class Health_Priorities(models.Model):
    disease = models.CharField(max_length=500)
    priority = models.IntegerField()
    content_url = models.CharField(max_length=500)

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
    event_category = models.CharField(max_length=500, null=True, blank=False)

    class Meta:
        db_table = 'Eventcategory'

    def __str__(self):
        return str(self.event_category)


class Newsauthor(models.Model):
    news_author = models.CharField(max_length=500, null=True, blank=False)

    class Meta:
        db_table = 'Newsauthor'

    def __str__(self):
        return str(self.news_author)


class Mohevents(models.Model):
    event_title = models.CharField(max_length=500)
    event_image = models.ImageField(null=True, blank=False)
    event_content = models.TextField(max_length=1000,blank=True, null=True)
    event_date = models.DateTimeField(auto_now_add=True)
    event_category = models.ForeignKey(
        'Mohevents', on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    news_author = models.ForeignKey(
        'Mohevents', on_delete=models.CASCADE, null=True, blank=True, related_name='authors')

    def __str__(self):
        return str(self.event_title)
        return str(self.event_image)
        return str(self.event_content)
        return str(self.event_date)
        return str(self.event_category)
        return str(self.news_author)


class Documents(models.Model):
    document_title = models.CharField(max_length=500)
    document_image = models.ImageField(
        default='doctor.jpg', upload_to='static/images')
    document_url = models.FileField(upload_to='static/images')
    document_published_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'documents'

    def __str__(self):
        return str(self.document_title)
        return str(self.document_image)
        return str(self.document_url)
        return str(self.document_published_date)

    class meta:
        verbose_name_plural = 'documents'

class Contact(models.Model):
    name = models.CharField(max_length=500,blank=False, null=True)
    email = models.EmailField(max_length=500,blank=False, null=True, unique=True)
    message = models.TextField(max_length=1000)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return str(self.name)
        return str(self.email)
        return str(self.message)

    class meta:
        verbose_name_plural = 'contact'
