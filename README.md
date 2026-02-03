# Ex01 Django ORM Web Application
## Date: 30.1.2026

## AIM
To develop a Django Application to store and retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM)



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

from django.db import models
from django.contrib import admin
class OrdersDB(models.Model):
	Order_id=models.IntegerField(primary_key=True);
	Name=models.CharField(max_length=10);
	Restaurant=models.CharField();
	Amount=models.IntegerField();
	Items=models.CharField();
	Mobile_no=models.IntegerField();
class OrdersDBAdmin(admin.ModelAdmin):
	list_display=['Order_id','Name','Restaurant','Amount','Items','Mobile_no'];


admin.py

from django.contrib import admin
from .models import OrdersDB,OrdersDBAdmin
admin.site.register(OrdersDB,OrdersDBAdmin)

urls.py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```




## OUTPUT
![alt text](<Screenshot 2026-01-31 113723.png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
