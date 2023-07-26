from django.db import models
from main.models import employee
from s_account.models import Region, Zone, Wereda, stock 

# Create your models here.
class Catagories(models.Model):
    
    id=models.AutoField(primary_key=True)
    Catagory_name=models.CharField(max_length=50)
    Catagory_code=models.CharField(max_length=50)


    def __str__(self):
        return self.Catagory_name


class subcatagories(models.Model):

    id=models.AutoField(primary_key=True)

    subcatagories_name=models.CharField(max_length=100)
    subcatagories_code=models.CharField(max_length=50)  
    Catagory=models.ForeignKey(Catagories, on_delete=models.PROTECT)

    def __str__(self):
        return self.subcatagories_name

class Item(models.Model):
    
    id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=100)
    item_code=models.CharField(max_length=100)
    brand=models.CharField(max_length=50)
    Item_type=models.CharField(max_length=50,
                             choices=[('fixed','Fixed'),('periodical','periodical'),('consumable','consumable')])
    Current_Quantity=models.IntegerField()
    scrap_value=models.IntegerField(default="", null=True)
    cost=models.IntegerField(default="",null=True)
    lift_span=models.IntegerField(default="",null=True)
    Catagory=models.ForeignKey(Catagories, on_delete=models.PROTECT, null=True, blank=True)
    sub_Catagory=models.ForeignKey(subcatagories, on_delete=models.PROTECT, null=True, blank=True)
    region_name=models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default="")
    
    Zone_name=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, default="")
    
    Wereda_name=models.ForeignKey(Wereda, on_delete=models.CASCADE, null=True, default="")  
    
    stock_name=models.ForeignKey(stock, on_delete=models.CASCADE, null=True, default="")   

    DisplayFields= ['id','item_name','item_code','Catagory','brand','Current_Quantity','region_name','stock_name','Zone_name','Wereda_name']
    SearchableFields= ['item_name','item_code','brand']
    FilterFields= ['region_name','Zone_name','Wereda_name','stock_name']
    

    def __str__(self):
        return self.item_name

class Issused_item(models.Model):
     
     id=models.AutoField(primary_key=True)
     issuse_date=models.DateTimeField(default='')
     issue_to=models.ForeignKey(employee, on_delete=models.PROTECT)
     Catagory_name=models.ForeignKey(Catagories, on_delete=models.PROTECT)
     subcatagory_name=models.ForeignKey(subcatagories, on_delete=models.PROTECT, null=True)
     Item_name=models.ForeignKey(Item, on_delete=models.PROTECT)
     quantity=models.IntegerField()
     taken_Item_status=models.CharField(max_length=50,
                             choices=[('New','New'),('slightly_used','slightly_used'),('damaged','damaged')])
     Item_Description=models.TextField(max_length=500)
     issued_by=models.CharField(max_length=100)

     region_name=models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default="")
    
     Zone_name=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, default="")
    
     Wereda_name=models.ForeignKey(Wereda, on_delete=models.CASCADE, null=True, default="")  
    
     stock_name=models.ForeignKey(stock, on_delete=models.CASCADE, null=True, default="")   

     DisplayFields= ['id','Catagory_name','region_name','Catagory_name','stock_name','Zone_name','Wereda_name']
     SearchableFields= ['issue_to','item_name']
     FilterFields= ['region_name','Zone_name','Wereda_name','stock_name']
    




    #  def __str__(self):
    #     return self.issuse_To
class retrun_item(models.Model):
     
     id=models.AutoField(primary_key=True)
     return_date=models.DateTimeField()
     return_from=models.ForeignKey(employee, on_delete=models.PROTECT)
     return_to=models.ForeignKey(stock, on_delete=models.PROTECT)
     Catagory_name=models.ForeignKey(Catagories, on_delete=models.PROTECT)
     subcatagory_name=models.ForeignKey(subcatagories, on_delete=models.PROTECT, null=True)
     Item_name=models.ForeignKey(Item, on_delete=models.PROTECT)
    
     taken_Item_status=models.CharField(max_length=50,
                             choices=[('New','New'),('slightly_used','slightly_used'),('damaged','damaged')])
     return_case=models.CharField(max_length=50,
                             choices=[('due_leave','due_leave'),('due_damage','due_damage'),('change','change')])
    
     return_Description=models.TextField(max_length=500)
     issued_by=models.CharField(max_length=100)
     recipant_name=models.CharField(max_length=100)

     region_name=models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default="")
    
     Zone_name=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, default="")
    
     Wereda_name=models.ForeignKey(Wereda, on_delete=models.CASCADE, null=True, default="")  
      
     def __str__(self):
        return self.return_to
     
class oreder_item(models.Model):
    id=models.AutoField(primary_key=True) 
    ordered_date=models.DateTimeField()
    ordered_from=models.ForeignKey(stock, on_delete=models.PROTECT)
    Catagory_name=models.ForeignKey(Catagories, on_delete=models.PROTECT)
    subcatagory_name=models.ForeignKey(subcatagories, on_delete=models.PROTECT, null=True)
    ordered_item_name=models.ForeignKey(Item, on_delete=models.PROTECT)
    
    order_Item_type=models.CharField(max_length=50,
                             choices=[('argent','argent'),('3_month','3_month'),('6_month','6_month')])
    ordered_case=models.CharField(max_length=50,
                             choices=[('for direct use','for direct use'),('to store','to store')])
    
    order_Description=models.TextField(max_length=500)
    ordered_by=models.CharField(max_length=100)

    is_active=models.BooleanField(default=True)

    region_name=models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default="")
    
    Zone_name=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, default="")
    
    Wereda_name=models.ForeignKey(Wereda, on_delete=models.CASCADE, null=True, default="")  
    
    
     
    def __str__(self):
        return self.ordered_from 

class general_notify(models.Model):
    
    id=models.AutoField(primary_key=True)
    notify_date=models.DateTimeField()
    notify_by=models.CharField(max_length=100)
    notify_from=models.ForeignKey(stock, on_delete=models.PROTECT)
    notification_type=models.CharField(max_length=50,
                             choices=[('question','question'),('report','report'),('other','other')])
    
    notification=models.TextField(max_length=500)

    is_active=models.BooleanField(default=True)

    region_name=models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default="")
    
    Zone_name=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, default="")
    
    Wereda_name=models.ForeignKey(Wereda, on_delete=models.CASCADE, null=True, default="")  
    
    
    
    def __str__(self):
        return self.notify_from 




        





     


