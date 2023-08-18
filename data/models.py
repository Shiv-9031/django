from django.db import models

# Create your models here.



class Data(models.Model):
   
   _id= models.CharField(max_length=100,primary_key=True)
   end_year= models.IntegerField()
   intensity= models.IntegerField()
   relevance= models.IntegerField()
   likelihood= models.IntegerField()
   sector = models.CharField(max_length=50)
   topic =models.CharField(max_length=50)
   insight=models.CharField(max_length=50)
   url=models.CharField(max_length=100)
   region=models.CharField(max_length=50)
   published=models.CharField(max_length=50)
   country=models.CharField(max_length=50)
   pestle=models.CharField(max_length=50)
   source=models.CharField(max_length=50)
   title=models.CharField(max_length=100)


   
    