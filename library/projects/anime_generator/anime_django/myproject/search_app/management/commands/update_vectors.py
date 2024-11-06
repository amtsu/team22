# search_app/management/commands/update_vectors.py

from django.core.management.base import BaseCommand
from search_app.models import Anime
import spacy
import numpy as np
from tqdm import tqdm
import logging

# Настройка логирования
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Генерирует и сохраняет векторные представления описаний аниме.'

    def handle(self, *args, **options):
        # Загрузка модели spaCy
        try:
            nlp = spacy.load('en_core_web_md')  # Замените на русскую модель, если необходимо
            self.stdout.write(self.style.SUCCESS('Модель spaCy успешно загружена.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка загрузки модели spaCy: {e}'))
            logger.error(f'Ошибка загрузки модели spaCy: {e}')
            return

        # Получение всех записей Anime с непустым описанием
        try:
            animes = Anime.objects.filter(description__isnull=False, description_vector__isnull=True).exclude(description='')

            total = animes.count()
            self.stdout.write(f'Найдено {total} записей для обработки.')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при получении записей из базы данных: {e}'))
            logger.error(f'Ошибка при получении записей из базы данных: {e}')
            return

        # Итерация с прогресс-баром
        for anime in tqdm(animes, desc='Обработка аниме', unit='anime'):
            try:
                # Генерация вектора для описания
                doc = nlp(anime.description)
                vector = doc.vector

                # Преобразование вектора в бинарный формат
                anime.description_vector = np.array(vector, dtype=np.float32).tobytes()

                # Сохранение изменений
                anime.save(update_fields=['description_vector'])

                # Логирование успешного сохранения
                logger.info(f'Успешно обработан Anime ID: {anime.anime_id}')
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Ошибка при обработке Anime ID {anime.anime_id}: {e}'))
                logger.error(f'Ошибка при обработке Anime ID {anime.anime_id}: {e}')
                continue

        self.stdout.write(self.style.SUCCESS('Векторные представления успешно обновлены.'))
