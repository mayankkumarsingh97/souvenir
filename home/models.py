from django.db import models

class Catalog(models.Model):
    catalogue_title=models.CharField(max_length=100,blank=True,null=True)
    cat= models.FileField(upload_to='sovenir_cat', verbose_name='provide a catalogue here...', blank=True)

    def __str__(self):
        return self.catalogue_title



        