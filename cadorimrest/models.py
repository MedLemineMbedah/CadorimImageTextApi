from django.db import models

# Create your models here.
# class Book(models.Model):
# 	title = models.CharField(max_length=100)
# 	author = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    #tagline = models.TextField()
    author = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=60)

class Event(models.Model):
     name = models.CharField('Event Name', max_length=120)
     event_date = models.DateTimeField('Event Date')
     venue = models.CharField(max_length=120)
     manager = models.CharField(max_length=60)
     description = models.TextField(blank=True)


class Cart(models.Model):
    NNI = models.CharField(max_length=100, default='none')
    Nom = models.CharField(max_length=100, default='none')
    Prenom = models.CharField(max_length=100, default='none')
    Sex =models.CharField(max_length=100, default='none')
    date_naiss =models.CharField(max_length=100, default='none')
    lieu_de_nai =models.CharField(max_length=100, default='none') 
    dateEmission =models.CharField(max_length=100, default='none') #date
    dateValidie =models.CharField(max_length=100, default='none') #date
    Pays =models.CharField(max_length=100, default='none')
    Ville =models.CharField(max_length=100, default='none')
    Rue  =models.CharField(max_length=100, default='none')
    codePostale  =models.CharField(max_length=100, default='none')
    typeDocument =models.CharField(max_length=100, default='none')
    NumeroDocument  =models.CharField(max_length=100, default='none') #int
    Path  =models.CharField(max_length=100, default='none') 


class BackCart(models.Model):
    dateEmission =models.CharField(max_length=100, default='none') #date
    dateValidie =models.CharField(max_length=100, default='none') #date
    Path  =models.CharField(max_length=100, default='none') 

    
#     def __str__(self):
#         return self.name

class PassePort(models.Model):
    NNI = models.CharField(max_length=100, default='none')
    Nom = models.CharField(max_length=100, default='none')
    Prenom = models.CharField(max_length=100, default='none')
    Sex =models.CharField(max_length=100, default='none')
    date_naiss =models.CharField(max_length=100, default='none')
    lieu_de_nai =models.CharField(max_length=100, default='none') 
    dateEmission =models.CharField(max_length=100, default='none') #date
    dateValidie =models.CharField(max_length=100, default='none') #date
    Pays =models.CharField(max_length=100, default='none')
    Ville =models.CharField(max_length=100, default='none')
    Rue  =models.CharField(max_length=100, default='none')
    codePostale  =models.CharField(max_length=100, default='none')
    typeDocument =models.CharField(max_length=100, default='none')
    NumeroDocument  =models.CharField(max_length=100, default='none') #int
    Path  =models.CharField(max_length=100, default='none') 


class FrCart(models.Model):
    NNI = models.CharField(max_length=100, default='none')
    Nom = models.CharField(max_length=100, default='none')
    Prenom = models.CharField(max_length=100, default='none')
    Sex =models.CharField(max_length=100, default='none')
    date_naiss =models.CharField(max_length=100, default='none')
    lieu_de_nai =models.CharField(max_length=100, default='none') 
    dateEmission =models.CharField(max_length=100, default='none') #date
    dateValidie =models.CharField(max_length=100, default='none') #date
    Pays =models.CharField(max_length=100, default='none')
    Ville =models.CharField(max_length=100, default='none')
    Rue  =models.CharField(max_length=100, default='none')
    codePostale  =models.CharField(max_length=100, default='none')
    typeDocument =models.CharField(max_length=100, default='none')
    NumeroDocument  =models.CharField(max_length=100, default='none') #int
    Path  =models.CharField(max_length=100, default='none') 


class Documents(models.Model):
    type = models.CharField(max_length=100, default='none')
    nationalite = models.CharField(max_length=100, default='none')


class Data(models.Model):
    name = models.CharField(max_length=100, default='none')