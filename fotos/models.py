from django.db import models

# Create your models here.


class Foto(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fotos/')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['-created_at']