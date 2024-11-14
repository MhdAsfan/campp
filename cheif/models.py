from django.db import models

# Create your models here.

class Cheif(models.Model):
    cheif_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    totelpapers = models.IntegerField()
    collegename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cheif'

