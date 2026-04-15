from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        # verbose_name = 'Categoria'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name    

class Contact(models.Model):
    # class Meta:
    #     verbose_name = 'Contato'
    #     verbose_name_plural = 'Contatos'    
      
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) 
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)  
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True, null=True)   
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        blank=True,
        null=True,
        related_name='contacts'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

