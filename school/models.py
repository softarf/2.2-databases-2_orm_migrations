from django.db import models


class Teacher(models.Model):
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


class Student(models.Model):
    # id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30, verbose_name='Имя')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.CharField(max_length=10, verbose_name='Класс')
    #
    objects = models.Manager()

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
