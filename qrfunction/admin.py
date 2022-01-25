from django.contrib import admin
from .models import CarryLog


class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(CarryLog, PostAdmin)