from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Client)
admin.site.register(Segment)
admin.site.register(CA)
admin.site.register(Profile)
