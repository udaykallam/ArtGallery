from django.db import models
from adminapp.models import Product

class Artist(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    email=models.EmailField(blank=False)
    phone = models.CharField(max_length=15, blank=False, unique=True)
    password=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="artist_table"

    def __str__(self):
        return self.username

class ArtistRequest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    action_choices = [
        ('change_price', 'Change Price'),
        ('delete_product', 'Delete Product'),
    ]
    action = models.CharField(max_length=15, choices=action_choices)
    new_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.product.title} - {self.get_action_display()}"
