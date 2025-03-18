from django.contrib import admin
from .models import CustomUser,OwnerProfile , ManagerProfile , AdminProfile

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(OwnerProfile)
admin.site.register(ManagerProfile)
admin.site.register(AdminProfile)