from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

class customer(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    
    
  
    class Meta:  
        db_table = "customer"

class Categrory(models.Model):
    cname=models.CharField(max_length=100)

    def __str__(self):
        return self.cname
        
    class Meta:
        db_table='category'
    

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Categrory,on_delete=models.CASCADE)
    price = models.IntegerField()
    weight = models.IntegerField()
    disc = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop/images', null=True, blank=True)

    def __str__(self):
        return self.product_name


    