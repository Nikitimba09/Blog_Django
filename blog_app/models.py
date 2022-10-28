from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)  #Это поле является CharField, которое преобразуется в столбец VARCHAR в базе данных SQL.
    slug = models.SlugField(max_length=250, unique_for_date='published') #slug: это поле, предназначенное для использования в URL-адресах.
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE) #author: это поле ForeignKey. В
    # этом поле
    # определяется отношение «многие к одному». Мы сообщаем о том, что каждая запись написана пользователем, и пользователь можетсоздать сколько угодно постов(posts).
    body = models.TextField() #Это поле является полем TextField, которое преобразуется в текстовый столбец базы данных SQL
    publish = models.DateTimeField(default=timezone.now()) #publish : этот параметр DateTime указывает, когда была опубликована запись.
    created = models.DateTimeField(auto_now_add=True) #created : этот DateTime параметр указывает, когда был создан пост. Поскольку мы используем auto_now_add здесь, дата будет автоматически добавлена при создании объекта.
    updated = models.DateTimeField(auto_now=True) #updated : этот DateTime параметр указывает на последний момент обновления этой записи.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') #status : это поле для отображения статуса записи(опубликован\неопубликован).


class Meta:
    ordering = ('-publish')


def __str__(self):
    return self.title
# Create your models here.
