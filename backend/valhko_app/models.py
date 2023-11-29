from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import HStoreField

# To use hstore don't forget to 'create extension hstore;' in the database

class ADM(models.Model):
    #  models.AutoField(primary_key=True)
    adm_name = models.CharField(max_length=255,null = True)
    adm_type = models.CharField(max_length=255,null = True)
    background_story =  models.TextField(null = True)
    adm_geom = models.GeometryField(srid=4326,null = True)

    # The following hstores contain key/value element corresponding to year/value
    finance_all = HStoreField(null = True)
    climate_finance = HStoreField(null = True)

    def __str__(self):
        return f"{self.adm_type} : {self.adm_name}"
    
    # abstract=True, this tells Django, not to create a database table for the corresponding table.
    class Meta:
        abstract=True
        
    
class ADM0(ADM):

    class Meta:
        verbose_name_plural = "Countries"

class ADM1(ADM):
    adm0 = models.ForeignKey(ADM0, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ADM1s"

class ADM2(ADM):
    adm1 = models.ForeignKey(ADM1, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ADM2s"

class ADM3(ADM):
    adm2 = models.ForeignKey(ADM2, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ADM3s"

class ADM4(ADM):
    adm3 = models.ForeignKey(ADM3, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ADM4s"

class Document(models.Model): 

    adm0 = models.ForeignKey(ADM0, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    pub_year = models.IntegerField()
    budget = models.FloatField(null = True)
    originator = models.CharField(max_length=255,null = True) # Green Climate Fund
    document_type = models.CharField(max_length=255,null = True) #  Note/Project Review
    document_group = models.CharField(max_length=255,null = True) # Legal doc | strategic doc | .....

    document_file = models.FileField(upload_to="documents/",null = True)

    class Meta:
        ordering = ['pub_year']
     
    def __str__(self):
        return f"{self.title}"


class  Indice(models.Model):
    name_index = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name_index}"
  
class IndiceValues(models.Model):
    name_index = models.ForeignKey(Indice, on_delete=models.CASCADE)
    date_index = models.DateField()
    price = models.FloatField()
    benchmark_price = models.FloatField()

    

