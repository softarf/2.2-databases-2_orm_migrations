from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)  # Регистрирует класс Student в административной панеле.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group', ]


@admin.register(Teacher)  # Регистрирует класс Teacher в административной панеле.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', ]
