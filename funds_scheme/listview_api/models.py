from django.db import models

# Create your models here.
class funds_info(models.Model):
    code = models.CharField(max_length=10**10)
    name = models.CharField(max_length=10**100)

    
    def __str__(self):
        return f"{self.code} : {self.name}"
    
