from django.contrib import admin
from .models import Facility
from .models import User

# Register your models here.
admin.site.register(Facility)
admin.site.register(User)