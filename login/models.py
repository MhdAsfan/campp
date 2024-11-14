from django.db import models

# Create your models here.


class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, db_collation='latin1_bin')
    password = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'