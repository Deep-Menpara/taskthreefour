from django.db import models

# Create your models here.
class product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name=models.TextField()
    cost = models.IntegerField()
    quantity = models.IntegerField()

class bill(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    date=models.DateTimeField()
    empusername=models.TextField()
    soldto=models.TextField()
    profit=models.FloatField()