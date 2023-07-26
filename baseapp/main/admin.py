from django.contrib import admin
from .models import *
import  csv 
from import_export.admin import  ExportActionMixin, ImportExportModelAdmin

from django.http import HttpResponse
# Register your models here.

admin.site.register(sectors)
admin.site.register(department)
admin.site.register(position)



def export_employee(modeladmin, request, queryset):
    response=HttpResponse(content_type='text/csv')
    response['content-Disposition'] = 'attachment; filename="employee.csv"'
    writer=csv.writer(response)
    writer.writerow(['id','employee_name','birthday','gender','office_no','office_floor_no','','sector name','department', 'position', 'data_of_employement'])
    employee = queryset.values_list ('id','employee_name','birthday','gender','office_no','office_floor_no','sector_name','department_name', 'position_name', 'data_of_employement')
    for employees in employee:
       writer.writerow(employees) 
    return response
export_employee.short_description='Export to csv' 



# @admin.register(employee)
class employeeList(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    list_display=employee.DisplayFields
    search_fields=employee.SearchableFields
    list_filter=employee.FilterFields
    actions=[export_employee]
    
    
admin.site.register(employee,employeeList)    