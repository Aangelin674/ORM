from django.contrib import admin

# Register your models here.





from .models import Website,WebsiteAdmin
admin.site.register(Website,WebsiteAdmin)