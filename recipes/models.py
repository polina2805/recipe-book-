from django.db import models
from django.urls import reverse

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание блюда")
    cooking_time = models.PositiveIntegerField(verbose_name="Время приготовления (минуты)")
    image = models.ImageField(
        upload_to='recipes/',
        blank=True,
        null=True,
        verbose_name="Изображение блюда"
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка на изображение",
        help_text="Можно указать ссылку на изображение вместо загрузки файла"
    )
    author_name = models.CharField(max_length=100, verbose_name="Имя автора", default="Аноним")
    author_email = models.EmailField(verbose_name="Email автора", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})
    
    def get_image(self):
        """Возвращает изображение - либо загруженное, либо по ссылке"""
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return None