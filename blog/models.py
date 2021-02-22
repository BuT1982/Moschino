from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URl")

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")
    context = models.TextField(max_length=5000, verbose_name="Содержание", blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name="Картинка", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    category = models.ForeignKey(Category, max_length=150, on_delete=models.PROTECT, related_name='posts',
                                 verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
