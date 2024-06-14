from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='blog_images/', verbose_name='изображение')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'