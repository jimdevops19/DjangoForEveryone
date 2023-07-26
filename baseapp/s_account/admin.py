from django.contrib import admin
from s_account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Region, Zone, stock, Wereda










class AccountInline(admin.StackedInline):
    model=Account
    can_delete=False
    verbose_name_plural='Main_info'

class CustomizeUserAdmin(UserAdmin):
    inlines=(AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)     

@admin.register(Region)
class Regions(admin.ModelAdmin):
    list_display=Region.DisplayFields


admin.site.register(Zone)
admin.site.register(Wereda)
admin.site.register(stock)