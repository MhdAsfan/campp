from django.db import models
from additionals.models import Additionals
from paper.models import Paper
# Create your models here.

class Assign(models.Model):
    assign_id = models.AutoField(db_column='Assign_id', primary_key=True)  # Field name made lowercase.

    # additional_id = models.IntegerField(db_column='Additional_id')  # Field name made lowercase.
    additional = models.ForeignKey(Additionals, on_delete=models.CASCADE)

    # paper_id = models.IntegerField(db_column='Paper_id')  # Field name made lowercase.
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assign'

