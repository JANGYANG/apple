from django.db import models

# Create your models here.

class Apple(models.Model):
    appleId = models.AutoField(db_column='appleId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=100,unique=True)  # Field name made lowercase.
    phone = models.CharField(max_length=100,unique=True)
    manittoId = models.ForeignKey('Apple',on_delete= models.CASCADE, db_column='manittoId', blank=True, null=True, db_constraint=False,related_name='+')  # Field name made lowercase..s