from django.contrib import admin
from .models import TechType, ProductTech, TechReview, TechMeeting

# Register your models here.
admin.site.register(TechType)
admin.site.register(ProductTech)
admin.site.register(TechReview)
admin.site.register(TechMeeting)