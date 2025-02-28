from django.db import models

class Item(models.Model):
    name = models.CharField("item name", max_length=200) 
    description = models.CharField("item description", max_length=200,default="Hello")
    price = models.IntegerField("item price")  
    image = models.CharField(max_length=500,default="https://static.vecteezy.com/system/resources/previews/027/277/492/non_2x/eat-healthy-icon-in-illustration-vector.jpg")

    def __str__(self):
        return self.name 
