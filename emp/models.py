from django.db import models

from datetime import timezone

class Employe(models.Model):
    username=models.CharField(max_length=255,null=True)
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=255,null=True)
    gender=models.CharField(max_length=255,null=True)
    age=models.DateField(null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    salary=models.IntegerField(null=True)
    exp=models.IntegerField(null=True)
    role=models.CharField(max_length=255,null=True)
    gfrom=models.CharField(max_length=255,null=True)
    gyear=models.DateField(null=True)
    bimage=models.ImageField(upload_to="image",null=True)
    certicate=models.ImageField(upload_to="certificate",null=True)
    valid=models.BooleanField(default=True)
    bcmgpa=models.IntegerField(null=True)
    bach=models.DateField(null=True)
    msc=models.DateField(null=True)
    phd=models.DateField(null=True)
    mimage=models.ImageField(upload_to="certificate",null=True)
    pimage=models.ImageField(upload_to="certificate",null=True)
    mcmgpa=models.IntegerField(null=True)
    pcmgpa=models.IntegerField(null=True)
    dt=models.DateField(auto_now=True)
    def __str__(self):
        return self.username
    
    