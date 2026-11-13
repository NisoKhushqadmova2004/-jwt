from django.db import models

class Debt(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.username



