from django.db import models

class Person(models.Model):
    firstname       = models.CharField(max_length=50)
    lastname        = models.CharField(max_length=20)
    dob             = models.DateField()
    place_of_birth  = models.CharField(max_length=30)
    hobby           = models.TextField(null=True)
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def testaja():
    pass

