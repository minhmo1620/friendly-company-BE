from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=60)
    company_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name