# Generated by Django 4.2.1 on 2023-06-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_group_alter_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
