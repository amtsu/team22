# search_app/management/commands/update_vectors.py
# python manage.py update_vectors
import logging
import time

import chromadb
from django.core.management.base import BaseCommand
from ollama import Client

# Настройка логирования
logger = logging.getLogger(__name__)

ollama1 = Client(host='http://127.0.0.1:11434')

class Command(BaseCommand):
    help = 'Генерирует и сохраняет векторные представления описаний аниме.'

    def handle(self, *args, **options):

        # Пример использования
        client = chromadb.PersistentClient("chroma.db")
        collection = client.get_collection(name="docs")

        """
          Проверяет и заполняет отсутствующие эмбеддинги для документов в коллекции.

          :param collection: Коллекция Chroma DB.
          :param ollama1: Объект для генерации эмбеддингов.
          :param model: Модель для генерации эмбеддингов.
          """
        print("Ensuring embeddings for all documents...")
        start_time = time.time()

        # Получаем документы и их метаданные
        all_docs = collection.get(include=["documents", "embeddings", "metadatas"])

        # IDs отдельно извлекаются из метаданных или через встроенный механизм
        doc_ids = all_docs["ids"] if "ids" in all_docs else []

        # Проверяем, какие документы не имеют эмбеддингов
        missing_embeddings = []
        for doc_id, document, embedding in zip(doc_ids, all_docs["documents"], all_docs["embeddings"]):
            if embedding is None:
                missing_embeddings.append((doc_id, document))

        print(f"Found {len(missing_embeddings)} documents without embeddings.")

        # Генерация эмбеддингов для документов с отсутствующими эмбеддингами
        for doc_id, document in missing_embeddings:
            try:
                # Генерация эмбеддинга с использованием ollama1
                response = ollama1.embeddings(prompt=document, model="mxbai-embed-large")
                new_embedding = response["embedding"]

                # Добавление эмбеддинга в коллекцию
                collection.update(
                    ids=[doc_id],
                    embeddings=[new_embedding]
                )
                print(f"Updated embedding for document ID: {doc_id}")
            except Exception as e:
                print(f"Failed to generate embedding for document ID: {doc_id}. Error: {e}")

        print(f"Embedding update completed in {time.time() - start_time:.2f} seconds.")

        self.stdout.write(self.style.SUCCESS('Векторные представления успешно обновлены.'))
