import os
import json

from django.core.management.base import BaseCommand
from school.models import Teacher, Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        """Получает имя json-файла с данными для загрузки.
           По умолчанию - 'school.json'."""
        parser.add_argument(
            'file_name',
            action='store',
            nargs='?',
            default='school.json',
            help='Название файла для считывания данных'
        )

    def handle(self, *args, **options):
        """Переносит данные из json-файла в модели (таблицы БД) Teacher и Student."""
        input_file = options['file_name']
        if not os.path.exists(input_file):
            self.stdout.write(f"Файл с данными не найден\n{input_file}")
            return
        with open(input_file, 'rt', encoding='utf-8') as json_file:
            json_data = json.load(json_file)    # ensure_ascii=False, indent=2

        self.stdout.write()
        for record in json_data:
            if record['model'] == 'school.teacher':
                self.stdout.write(f"Это учитель - {record['pk']},"
                                  f" его имя - {record['fields']['name']},"
                                  f" предмет - {record['fields']['subject']}.")
                Teacher.objects.create(id=record['pk'],
                                       name=record['fields']['name'],
                                       subject=record['fields']['subject']
                )
            elif record['model'] == 'school.student':
                self.stdout.write(f"Это ученик - {record['pk']},"
                                  f" его имя - {record['fields']['name']},"
                                  f" его учитель - {record['fields']['teacher']},"
                                  f" класс - {record['fields']['group']}.")
                Student.objects.create(id=record['pk'],
                                       name=record['fields']['name'],
                                       teacher_id=record['fields']['teacher'],
                                       group=record['fields']['group']
                )
            else:
                self.stdout.write(f"Неизвестное лицо: {record['model']}")
        self.stdout.write("Данные перенесены.")    # Для теста.
        return
