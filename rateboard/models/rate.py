from django.db import models

class Rate(models.Model):
    source = models.CharField(max_length=100)
    buy_rate = models.DecimalField(max_digits=10, decimal_places=3)
    sell_rate = models.DecimalField(max_digits=10, decimal_places=3)
    url = models.CharField(max_length=300)
    url_logo = models.CharField(max_length=300, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        unique_together = ('source', 'timestamp')

    def __str__(self):
        return f"{self.source}: Compra {self.buy_rate} / Venta {self.sell_rate} @ {self.timestamp:%Y-%m-%d %H:%M}"
