from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'course'


