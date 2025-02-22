from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок",null = True,blank =True)
    content = models.TextField(verbose_name= "Контент",null = True,blank =True)
    preview_image = models.ImageField(null = True,blank =True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    is_published = models.BooleanField(default=False,null = True,blank =True)
    views_count = models.PositiveIntegerField(default=0,verbose_name= "Количество просмотров")

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return self.title