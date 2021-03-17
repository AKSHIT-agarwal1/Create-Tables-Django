from django.db import models
import eav

class Table_Manager(models.Model):
    schema = models.CharField(max_length=50)
    table = models.CharField(max_length=50)

class Table(models.Model):
    ...


eav.register(Table)