from django.db import models

# Create your models here.
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=122)
    sub=models.CharField(max_length=2500,default='')
    desc=models.CharField(max_length=5000)
    submitter=models.CharField(max_length=122)
    def __str__(self):
        return self.title
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=126)
    phone=models.CharField(max_length=12)
    message=models.TextField()
