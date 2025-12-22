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
    
    from django.db import models

class Review(models.Model):
    """Модель отзывов к рецептам"""
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'), 
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]
    
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, default="Аноним")
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Отзыв от {self.author_name}"
    
    def get_stars(self):
        """Возвращает звезды для отображения"""
        return '★' * self.rating + '☆' * (5 - self.rating)