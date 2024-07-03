from django.db import models


class Worldcities(models.Model):
    id = models.AutoField(primary_key=True)  # primary_key=True를 추가
    city = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    lng = models.TextField(blank=True, null=True)  # This field type is a guess.
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worldcities'
