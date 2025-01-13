from django.db import models

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)

class Group(models.Model):
    
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    image = models.ImageField(upload_to='images/groups/', verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Album(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="albums", verbose_name="Группа")
    release_date = models.DateField(verbose_name="Дата выпуска")
    cover_image = models.ImageField(upload_to='images/albums/', verbose_name="Обложка альбома", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Song(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True, related_name="songs", verbose_name="Альбом")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name="songs", verbose_name="Группа")
    duration = models.DurationField(verbose_name="Длительность")  
    audio_file = models.FileField(upload_to="songs", verbose_name="Файл с аудио", blank=True, null=True)
    lyrics = models.TextField(verbose_name="Текст песни", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


class GroupMember(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    biography = models.TextField(verbose_name="Биография", default="Биография пока не указана")
    photo = models.ImageField(upload_to="group_members", verbose_name="Фотография")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members", verbose_name="Группа")
    instrument = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Участник группы"
        verbose_name_plural = "Участники группы"
