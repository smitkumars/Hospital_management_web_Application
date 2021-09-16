from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name= models.CharField("First name", max_length=255, blank = True, null = True)
    last_name= models.CharField("Last name", max_length=255, blank = True, null = True)
    email= models.EmailField()
    phone= models.CharField(max_length=20, blank = True, null = True)
    address= models.TextField(blank=True, null=True)
    description= models.TextField(blank=True,null=True)
    createdAt= models.DateTimeField("Created At",auto_now_add=True)


    def __str__(self):
        return self.first_name