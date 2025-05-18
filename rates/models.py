from django.db import models

class Rate(models.Model):
    currency = models.CharField(max_length=10)
    rate = models.DecimalField(decimal_places=6, max_digits=10)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    source = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.currency} - {self.rate} ({self.date} {self.time} from {self.source})"
