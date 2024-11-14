from django.db import models

# Create your models here.
class Bill(models.Model):
    no = models.AutoField(primary_key=True)
    nameofexaminer = models.CharField(max_length=45, blank=True, null=True)
    nameofcollage = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    total_no_of_paper = models.CharField(max_length=45, blank=True, null=True)
    mandatory_deduction = models.CharField(max_length=45, blank=True, null=True)
    elligibel_no_of_papers = models.CharField(db_column='Elligibel_no_of_papers', max_length=45, blank=True, null=True)  # Field name made lowercase.
    remuneration = models.CharField(db_column='Remuneration', max_length=45, blank=True, null=True)  # Field name made lowercase.
    additional_maximum_chairman_fee = models.CharField(db_column='Additional_maximum_chairman_fee', max_length=45, blank=True, null=True)  # Field name made lowercase.
    remunerationfor_decussiom = models.CharField(db_column='Remunerationfor_decussiom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    totel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill'



