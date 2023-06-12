from django.apps import AppConfig


class SchoolConfig(AppConfig):
    name = 'school'
    verbose_name = 'Школа'
    # default_auto_field = 'django.db.models.BigAutoField'
    # Назначает класс для ключей 'pk', создающихся автоматически в моделях приложения по умолчанию.
    # Можно также объявить в 'settings.py'.
