from django.db import models
from tinymce import models as tiny_model

# Create your models here.
class PromoBlock(models.Model):
    name = models.CharField(verbose_name='Block name', max_length=50)
    heading = models.CharField(verbose_name='Block heading', max_length=100)
    text = tiny_model.HTMLField(verbose_name='Text', max_length=7000)
    img = models.ImageField(verbose_name='Banner picture', upload_to='promo/', null=True, max_length=255)
    position = models.IntegerField(verbose_name='Queue position', default=1)
    url = models.URLField(verbose_name='Link from block', max_length=255, null=True)
    active_from = models.DateField(verbose_name='Turn on')
    active_to = models.DateField(verbose_name='Turn off')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'promoblock'  # название таблицы в БД
        verbose_name = 'Пробомоблок'
        verbose_name_plural = 'Промоблоки'
        ordering = ('name', 'position',)



