from django.db import models
from django import forms
import base64
try:
    import cPickle as pickle
except:
    import pickle

# Create your models here.

#class ClassItem(models.Model):
#    name = models.CharField()

#class MethodItem(models.Model):
#    name = models.CharField()
#    params = models.CharField()
#    returns = models.CharField()
#    myclass = models.ForeignKey(ClassItem, unique=True, blank=True, null=True, default="")
    

#class VariableItem(models.Model):
#    name = models.CharField()
#    value = models.CharField()
#    myclass = models.ForeignKey(ClassItem, unique=True, blank=True, null=True, default="")
#    mymethod = models.ForeignKey(MethodItem, unique=True, blank=True, null=True, default="")
    

class Code(models.Model):
    rawcode = models.CharField(max_length = 99999, blank=True)
    serialcode = models.CharField(max_length = 99999, blank=True)
