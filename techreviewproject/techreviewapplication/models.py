from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TechType(models.Model):
    techtypename = models.CharField(max_length = 255)
    techdescription = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.techtypename
    
    class Meta:
        db_table = 'techtype'
        verbose_name_plural = 'techtypes'

class ProductTech(models.Model):
    productname = models.CharField(max_length = 255)
    techtype = models.ForeignKey(TechType, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    productprice = models.DecimalField(max_digits = 10, decimal_places = 2)
    productentrydate = models.DateField()
    productURL = models.URLField(null = True, blank = True)
    productdescription = models.TextField(null = True, blank = True)
    
    def __str__ (self):
        return self.productname
    
    def memberDiscount(self):
        discount = .05
        return float(self.productprice) * discount
    
    def discountedPrice(self):
        discount = self.memberDiscount()
        return float(self.productprice) - discount
    
    class Meta:
        db_table = 'producttech'
        verbose_name_plural = 'producttechs'

class TechReview(models.Model):
    reviewtitle = models.CharField(max_length = 255)
    reviewdate = models.DateField()
    product = models.ForeignKey(ProductTech, on_delete = models.DO_NOTHING)
    user = models.ManyToManyField(User)
    rating = models.SmallIntegerField()
    reviewtext = models.TextField()
    
    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table = 'techreview'
        verbose_name_plural = 'techreviews'
        
        
class TechMeeting(models.Model):
    meetingtype = models.CharField(max_length = 255)
    meetingtitle = models.CharField(max_length = 255)
    meetingdate = models.DateField()
    posteddate = models.DateField()
    experiencelevel = models.SmallIntegerField()
    
    def __str__(self):
        return self.meetingtype
    
    class Meta:
        db_table = 'techmeeting'
        verbose_name_plural = 'techmeetings'
