from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Portfolio)
admin.site.register(models.History)
admin.site.register(models.Statement)
admin.site.register(models.Values)
