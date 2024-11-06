# search_app/management/commands/update_vectors_2.py

from django.core.management.base import BaseCommand
from search_app.models import Anime
import spacy
import numpy as np
from tqdm import tqdm
import logging
import ollama
import chromadb

# Настройка логирования
logger = logging.getLogger(__name__)

client = chromadb.PersistentClient("chroma.db")
collection = client.get_collection(name="docs")

class Command(BaseCommand):
    help = 'Генерирует и сохраняет векторные представления описаний аниме.'

    def handle(self, *args, **options):
        # Получение всех записей Anime с непустым описанием
        try:
            animes = Anime.objects.filter(description__isnull=False).exclude(description='')
            animes = [anime for anime in animes if len(anime.description) > 110]

            total = len(animes)
            self.stdout.write(f'Найдено {total} записей для обработки.')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при получении записей из базы данных: {e}'))
            logger.error(f'Ошибка при получении записей из базы данных: {e}')
            return

        # Итерация с прогресс-баром
        for anime in tqdm(animes, desc='Обработка аниме', unit='anime'):
            try:
                # store each document in a vector embedding database
                response = ollama.embeddings(model="mxbai-embed-large", prompt=anime.description)
                embedding = response["embedding"]
                collection.add(
                    ids=[str(anime.anime_id)],
                    embeddings=[embedding],
                    documents=[anime.description]
                )

                # Логирование успешного сохранения
                logger.info(f'Успешно обработан Anime ID: {anime.anime_id}')
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Ошибка при обработке Anime ID {anime.anime_id}: {e}'))
                logger.error(f'Ошибка при обработке Anime ID {anime.anime_id}: {e}')
                continue

        self.stdout.write(self.style.SUCCESS('Векторные представления успешно обновлены.'))
