from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateField(auto_now=True)

    def __str__(self):  #without this the model is create just with the name "object" in DB. We need pass a string with an attribute
        return '{}'.format(self.search) 

    class Neta:
        verbose_name_plural = 'Searches'  #this is needed because sometimes its automaticaly created as plural in the DB
