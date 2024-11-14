from django.db import models

# Create your models here.
class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    email_id = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    college_name = models.CharField(max_length=45)
    experience = models.CharField(db_column='Experience', max_length=45)  # Field name made lowercase.
    choice = models.CharField(max_length=45)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'form'
