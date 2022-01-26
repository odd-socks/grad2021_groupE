from django.contrib import admin
from .models import FacilityUser


class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(FacilityUser, PostAdmin)