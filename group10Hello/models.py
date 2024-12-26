from django.db import models

# Create your models here.
class investment(models.Model):
    membername = models.CharField(max_length=100)
    membercpm = models.CharField(max_length=100)
    invetsmentamount = models.DecimalField(max_digits=10, decimal_places=2)
    investmentdate=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.membername
    