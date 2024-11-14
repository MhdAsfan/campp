from django.db import models
from course.models import Course
from paper.models import Paper
# Create your models here.
class Additionals(models.Model):
    additional_id = models.AutoField(db_column='Additional_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='User_name', max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_id', max_length=45)  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_no', max_length=45)  # Field name made lowercase.
    uid = models.IntegerField()
    # course_id = models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    sem = models.CharField(max_length=45)
    priority_1 = models.CharField(max_length=45)
    priority_2 = models.CharField(max_length=45)
    priority_3 = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    username=models.CharField(max_length=45)
    totelpapers = models.IntegerField()
    collegename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'additionals'
