from django.db import models

# Create your models here.





class categories(models.Model):
    name        =   models.CharField(blank=False,max_length=255)

    def __str__(self):
        return self.name

class product(models.Model):
    name         =  models.CharField(blank=False,max_length=255)
    Product_code =  models.CharField(blank=False,max_length=255) # helps for any cod type like A3315 or 3315 if Pk can used ac dode so Id auto created
    price        =  models.DecimalField(blank=False,decimal_places=2,max_digits=255)
    quantity     =  models.IntegerField(blank=False)
    categories   =  models.ManyToManyField(categories)



    def __str__(self):
        return self.name