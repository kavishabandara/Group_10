from django.db import models

# Create your models here.
class investment(models.Model):
    membername = models.CharField(max_length=100)
    membercpm = models.CharField(max_length=100)
    invetsmentamount = models.CharField(max_length=100)
    investmentdate=models.CharField(max_length=100)

    def __str__(self):
        return self.title