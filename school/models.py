from django.db import models


class Teacher(models.Model):    # Главная/первичная сущность/модель/таблица - "один".
    # id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')
    #
    objects = models.Manager()

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):    # Зависимая/вторичная сущность/модель/таблица - "многие".
    # id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30, verbose_name='Имя')
    # related_name обеспечивает обращение из главной сущности к зависимой (из Teacher к Student).
    teacher = models.ManyToManyField(Teacher, related_name='students')
    group = models.CharField(max_length=10, verbose_name='Класс')
    #
    objects = models.Manager()

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
