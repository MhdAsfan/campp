from django.db import models
from paper.models import Paper
from assign.models import Assign
# Create your models here.

class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    # assign_id = models.IntegerField()
    assign=models.ForeignKey(Assign,on_delete=models.CASCADE)
    count = models.CharField(max_length=45)
    date = models.DateField()
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'work'
