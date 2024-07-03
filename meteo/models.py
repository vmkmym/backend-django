from django.db import models


class Worldcities(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)  
    lng = models.TextField(blank=True, null=True) 
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worldcities'
