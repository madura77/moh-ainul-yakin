from django.db import models

# Create your models here.
class Teknik(models.Model):
    title = models.CharField(max_length=99)
    comtent = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title 


        

# Create your models here.
class Computer(models.Model):
    title = models.CharField(max_length=99)
    comtent = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title 



# Create your models here.
class Elit(models.Model):
    title = models.CharField(max_length=99)
    comtent = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title 