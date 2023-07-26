from django.db import models
from s_account.models import Region,Zone,Wereda,stock
from datetime import date
# Create your models here.


class sectors(models.Model):

    id=models.AutoField(primary_key=True)
    sector_name=models.CharField(max_length=100)
    def __str__(self):
        return self.sector_name
    
class department(models.Model):

    id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=100)
    # sectors_name=models.ForeignKey(sectors, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.department_name
    
class position(models.Model):

    id=models.AutoField(primary_key=True)
    position_name=models.CharField(max_length=100)
    # department_name=models.ForeignKey(department, on_delete=models.CASCADE)
    # sectors_name=models.ForeignKey(sectors, on_delete=models.CASCADE)
    def __str__(self):
        return self.position_name
class employee(models.Model):

    id=models.AutoField(primary_key=True)
    employee_name=models.CharField(max_length=100)
    birthday=models.DateTimeField()
    gender=models.CharField(max_length=6,
                             choices=[('malle','Male'),('FEMALE','Female')])
    data_of_employement=models.DateTimeField()
    office_floor_no=models.CharField(max_length=50)
    office_no=models.CharField(max_length=50)

    is_active=models.BooleanField(default=True)
    region_name=models.ForeignKey(Region, on_delete=models.PROTECT, default="")
    zone_name=models.ForeignKey(Zone, on_delete=models.PROTECT, default="")
    wereda_name=models.ForeignKey(Wereda, on_delete=models.PROTECT, default="")
    stock_name=models.ForeignKey(stock, on_delete=models.PROTECT, default="")
    sector_name=models.ForeignKey(sectors, on_delete=models.PROTECT)
    department_name=models.ForeignKey(department, on_delete=models.PROTECT)
    position_name=models.ForeignKey(position, on_delete=models.PROTECT)
    DisplayFields= ['id','employee_name','gender','sector_name','department_name','position_name','data_of_employement']
    SearchableFields= ['employee_name','gender']
    FilterFields= ['region_name','zone_name','wereda_name','stock_name']
    
    class Meta:
        db_table = "employee"
        verbose_name='employee'
        verbose_name_plural='employee'
        
 
    # @property    
    # def age(self):
    #     if(self.dob !=None):
    #             age=date.today().year -self.dob.year
    #             return age
    
    def __unicode__ (self):
        return self.employee_name    
  
    def __str__ (self):
        return self.employee_name    
  
