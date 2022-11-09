from django.db import models
from django.utils.safestring import mark_safe


class Contact(models.Model):
    first_name = models.CharField('Имя', max_length=300)
    last_name = models.CharField('Фамилия', max_length=300)
    phone = models.CharField('Телефон', max_length=300)
    message = models.TextField('Сообщение', max_length=2000)
    ip = models.CharField('IP адрес', max_length=300)
    create_time = models.TimeField('Время', auto_now=True)
    create_date = models.DateField('Дата', auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Общение с клиентами'
        verbose_name_plural = 'Общение с клиентами'


class Projects(models.Model):
    title = models.TextField(max_length=300)
    site_link = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='projects/images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наши проекты'
        verbose_name_plural = 'Наши проекты'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))


class SiteLogo(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='site_logo/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Логотип сайта'
        verbose_name_plural = 'Логотип сайта'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))
