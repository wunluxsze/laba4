from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Films(models.Model):
    genre = models.ForeignKey("Category",on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date = models.DateField()
    actors = models.TextField()
    dateView = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
