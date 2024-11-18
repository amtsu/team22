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
        # an example prompt
        prompt = "anime about space travel"

        # generate an embedding for the prompt and retrieve the most relevant doc
        response = ollama.embeddings(
            prompt=prompt,
            model="mxbai-embed-large"
        )
        results = collection.query(
            query_embeddings=[response["embedding"]],
            n_results=5
        )
        data = results['ids'][0]

        print(data)
