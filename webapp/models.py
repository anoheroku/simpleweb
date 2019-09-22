from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.TextField(verbose_name='Имя')
    title = models.TextField(verbose_name='Должность')
    number = models.TextField(verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.title, self.number)


class Equipment(models.Model):
    name = models.TextField(verbose_name='Наименование')
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name


class Operation(models.Model):
    number = models.IntegerField()
    title = models.TextField(verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.number, self.title)
