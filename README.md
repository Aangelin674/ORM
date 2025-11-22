# Ex01 Django ORM Web Application
## Date: 22.11.2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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
 
 admins.py
 from django.contrib import admin

# Register your models here.





from .models import Website,WebsiteAdmin
admin.site.register(Website,WebsiteAdmin)


```


## OUTPUT
![alt text](<Screenshot (17).png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
