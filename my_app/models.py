from django.db import models

from services.mixin import SlugMixin, DateMixin
from services.generator import Generator
from services.uploader import Uploader



class Product(SlugMixin, DateMixin):

     name = models.CharField(max_length = 255,verbose_name = 'mehsulun adi')
     count = models.FloatField(verbose_name ='mehsulun sayi')
     description_L = models.TextField(verbose_name = 'kicik movzu')
     image = models.ImageField(upload_to=Uploader.upload_photo_products,null=True,blank=True)

     def __str__(self):
        return self.name

     class Meta:
       ordering = ('-created_at',)
       verbose_name = 'mehsul'
       verbose_name_plural = 'mehsullar'


     def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Product)
        super(Product, self).save(*args, **kwargs)

    
class Country(DateMixin):
     name = models.CharField(max_length = 255, verbose_name = 'obyektin adi')

     def __str__(self):
        return self.name
     
     class Meta:
        ordering = ('-created_at',)
        verbose_name = 'obyektin adi'
        verbose_name_plural = 'obyektlerin adlari'
     