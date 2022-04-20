from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=60)
    company_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name
class company_data (models.Model):
    entry_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    job_industry = models.CharField(max_length=100)
    full_time = models.BooleanField()
    min_average = models.FloatField()
    max_average = models.FloatField()
    average = models.FloatField()
    approval_rate = models.FloatField()
    def __str__(self):
        return self.company_name
