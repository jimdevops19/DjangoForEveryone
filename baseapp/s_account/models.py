from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    
    id=models.AutoField(primary_key=True)
    region_name=models.CharField(max_length=50, default="")
    DisplayFields=['id','region_name']
    def __str__(self):
        return self.region_name
    

class Zone(models.Model):
    
    id=models.AutoField(primary_key=True)
    zone_name=models.CharField(max_length=50, default="")
    region_name=models.ForeignKey(Region, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.zone_name

class Wereda(models.Model):
    
    id=models.AutoField(primary_key=True)
    Wereda_name=models.CharField(max_length=50, default="")
    
    region_name=models.ForeignKey(Region, on_delete=models.CASCADE)
    zone_name=models.ForeignKey(Zone, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.Wereda_name

class stock(models.Model):
    
    id=models.AutoField(primary_key=True)
    stock_name=models.CharField(max_length=50, default="")
    
    
    region_name=models.ForeignKey(Region, on_delete=models.CASCADE)
    Wereda_name=models.ForeignKey(Wereda, on_delete=models.CASCADE)
    zone_name=models.ForeignKey(Zone, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.stock_name
    
class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birthday=models.DateTimeField()
    gender=models.CharField(max_length=6,
                             choices=[('malle','M'),('FEMALE','F')])
    user_type_data=(('federal_admin',"Federal Admin"),('regional_admin',"regional admin"),('zone_admin',"zone admin"),('wereda_admin',"wereda admin"),('building_admin',"building admin"), ('stock_admin',"stock admin"),('stock_personnel',"stock personnel"))
    
    user_type=models.CharField(choices=user_type_data, max_length=50)

    region_name=models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default="")
    
    Zone_name=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, default="")
    
    Wereda_name=models.ForeignKey(Wereda, on_delete=models.CASCADE, null=True, default="")  
    
    stock_name=models.ForeignKey(stock, on_delete=models.CASCADE, null=True, default="")   
   

    def __str__(self):
        return self.user.username