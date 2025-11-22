from django.db import models

# Create your models here.



from django.contrib import admin
class Website(models.Model):
	Product_Name=models.CharField(max_length=100)
	Product_ID=models.IntegerField()
	Brand=models.CharField(max_length=10)
	Quality=models.CharField(max_length=10)
	Stoke_Quality=models.CharField()
	Rating=models.FloatField()
	Price=models.IntegerField()
class WebsiteAdmin(admin.ModelAdmin):
	list_display=["Product_Name","Product_ID","Brand","Rating","Stoke_Quality","Quality"]

