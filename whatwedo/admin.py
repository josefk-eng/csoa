from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.News)
admin.site.register(models.Prayer)
admin.site.register(models.Testimonial)
admin.site.register(models.Story)
