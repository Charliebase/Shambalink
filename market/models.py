from django.db import models

class Produce(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, help_text="WhatsApp or phone number")
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
