from django.db import models

# Create your models here.

class Status(models.Model):
    status_id = models.AutoField(db_column='Status_id', primary_key=True)  # Field name made lowercase.
    check_id = models.CharField(db_column='Check_id', max_length=45)  # Field name made lowercase.
    count_id = models.CharField(db_column='Count_id', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_time_id = models.CharField(max_length=45, blank=True, null=True)
    paper_availability = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'
        unique_together = (('status_id', 'check_id'),)
