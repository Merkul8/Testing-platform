from django.db import models
from django.urls import reverse


class Answers(models.Model):
    title = models.CharField(blank=True, max_length=250, verbose_name='Вариант ответа')
    true_or_false = models.BooleanField(default=False, verbose_name='Правильность ответа')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Вопрос')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    title = models.CharField(blank=True, max_length=250, verbose_name='Вопрос')
    test = models.ForeignKey('Tests', on_delete=models.CASCADE, verbose_name='Название теста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Tests(models.Model):
    title = models.CharField(blank=True, max_length=250, verbose_name='Название теста')
    slug = models.SlugField(blank=True, verbose_name='Url', max_length=255, unique=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('test', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
