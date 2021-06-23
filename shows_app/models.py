from __future__ import unicode_literals
from django.db import models
from datetime import datetime


#creo mi propio validador en base la los campos de mi tabla que voy a validar, extiende de models.Manager
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors={}   #dicc vacio par guaradr los errores

        if len(postData['title']) < 4:
            errors['title']="Title should be at least 4 characters" #guardo ene le dicc

        if postData['description'] != "":      #si trae algo, deber ser mayor a 10 caracteres
            if len(postData['description']) < 10:
                errors['description']="Description should be at least 10 characters"

        now=datetime.now() #obtengo la fecha actual        
        release=datetime.strptime(postData['release'], '%Y-%m-%d') #recibo la fecha ingresada que viene como str y la paso a formato de fecha        
        if release > now:   #comparo ambas fechas que la ingresada no sea mayor a la actual
            errors['release']="Release Date must be BEFORE today."

        existentTitles=Show.objects.all()   #traigo todos los show de la base y la recorro
        for showTitle in existentTitles:
            if postData['title']==showTitle.title:   #comparo el titulo ingresado con los existentes
                errors['tileDuplicate']="This Show title already exists. Enter another"    

        return errors

class Network(models.Model):
    name=models.CharField(max_length=255) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    
    #   shows

    def __repr__(self):
        return f"Network: {self.name}"

    def __str__(self):
        return f"{self.name}"

class Show(models.Model):
    title= models.CharField(max_length=255)
    network=models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    release_date=models.DateField(auto_now=False)
    description=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager() #vinculo mi validador a la clase

    def __repr__(self):
        return f"Show name: {self.title}"

    def __str__(self):
        return f"Show: {self.title}"




