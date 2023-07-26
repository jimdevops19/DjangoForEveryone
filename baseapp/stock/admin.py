from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Catagories)
admin.site.register(subcatagories)


# admin.site.register(Item)
@admin.register(Item)
class ItemsList(admin.ModelAdmin):
    list_display=Item.DisplayFields
    search_fields=Item.SearchableFields
    list_filter=Item.FilterFields

# admin.site.register(Issused_item)
@admin.register(Issused_item)
class ItemsList(admin.ModelAdmin):
    list_display=Issused_item.DisplayFields
    search_fields=Item.SearchableFields
    list_filter=Item.FilterFields
admin.site.register(retrun_item)
admin.site.register(oreder_item)
admin.site.register(general_notify)

