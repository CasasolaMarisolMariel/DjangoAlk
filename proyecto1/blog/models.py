from django.db import models
from django.conf import settings 
from django.utils import timezone

# Create your models/objects here.
class Post(models.Model):
#models.Model indica que es un modelo django para guardar en bd
#definimos propiedades
    #ForeignKey es una relación link con otro modelo
    author= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #charField para definir un texto con un nro limitado de caracteres
    title= models.CharField(max_length=200)
    text=models.TextField()
    #DateTimeField fecha y hora
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish (self):
        self.published_date=timezone.now()
        self.save()
    def __str__ (self):
        return self.title
