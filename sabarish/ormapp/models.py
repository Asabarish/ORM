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


