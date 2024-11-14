from django.db import models
from cheif.models import Cheif
from paper.models import Paper
from additionals.models import Additionals

class IssuePaper(models.Model):
    work_id = models.AutoField(primary_key=True)
    # paper_id = models.IntegerField()
    # cheif_id = models.IntegerField()
    paper = models.ForeignKey(Paper,on_delete=models.CASCADE)
    cheif = models.ForeignKey(Cheif, on_delete=models.CASCADE)
    start = models.IntegerField()
    end = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'issuepaper'



class AssignPaper(models.Model):
    assign_paper_id = models.AutoField(primary_key=True)
    # issuepaper_id = models.IntegerField()
    # additional_id = models.IntegerField()
    issuepaper=models.ForeignKey(IssuePaper,on_delete=models.CASCADE)
    additional=models.ForeignKey(Additionals,on_delete=models.CASCADE)
    start = models.IntegerField()
    end = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'assign_paper'

class ChiefIssuepaperAdditional(models.Model):
    work_id = models.AutoField(primary_key=True)
    # paper_id = models.IntegerField()
    # cheif_id = models.IntegerField()
    paper = models.ForeignKey(Paper,on_delete=models.CASCADE)
    cheif = models.ForeignKey(Cheif, on_delete=models.CASCADE)
    # additional_id = models.IntegerField(db_column='Additional_id')  # Field name made lowercase.
    additional = models.ForeignKey(Additionals, on_delete=models.CASCADE)
    start = models.IntegerField()
    end = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'chief_issuepaper_additional'
