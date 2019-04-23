from django.contrib import admin
from .models import TechType, ProductTech, TechReview

# Register your models here.
admin.site.register(TechType)
admin.site.register(ProductTech)
admin.site.register(TechReview)