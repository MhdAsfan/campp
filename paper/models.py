from django.db import models
from course.models import Course
from  cheif.models import  Cheif
# Create your models here.
class Paper(models.Model):
    paper_id = models.AutoField(db_column='Paper_id', primary_key=True)  # Field name made lowercase.
    # course_id = models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    sem = models.CharField(max_length=45)
    paper = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'paper'


