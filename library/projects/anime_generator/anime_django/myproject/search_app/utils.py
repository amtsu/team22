# search_app/utils.py
import chromadb
import numpy as np
import ollama
from search_app.models import Anime
import spacy
import time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Загрузим модель spaCy
nlp = spacy.load('en_core_web_md')

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)


def vector_search(query: str, with_scenario, with_poster, titles_per_page: int):
    """Ищет аниме по векторному сходству."""

    print("starting")
    start_time = time.time()
    # translate Russian to Chinese
    input_ids = tokenizer(query, return_tensors="pt")

    generated_tokens = model.generate(**input_ids)

    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print(result[0])

    query = result[0]

    client = chromadb.PersistentClient("chroma.db")
    collection = client.get_collection(name="docs")

    # generate an embedding for the prompt and retrieve the most relevant doc
    response = ollama.embeddings(
        prompt=query,
        model="mxbai-embed-large"
    )
    results = collection.query(
        query_embeddings=[response["embedding"]],
        n_results=titles_per_page
    )
    print(results['distances'])
    data = [x[0] for x in zip(results['ids'][0], results['distances'][0]) if x[1] <200 ]

    print(data)
    print(len(data))

    # Получаем все записи с векторами
    animes = Anime.objects.filter(anime_id__in=data)

    animes = sorted(animes, key=lambda x: x.rating if x.rating  else 0, reverse=True)

    # Возвращаем только записи, игнорируя коэффициенты схожести
    return  animes[:titles_per_page]  # Возвращаем 5 самых релевантных


def vector_search_2(query: str, with_scenario, with_poster, titles_per_page: int):
    """Ищет аниме по векторному сходству."""
    query_vector = nlp(query).vector

    # print(len(query_vector))
    # print(query_vector)

    # Получаем все записи с векторами
    animes = Anime.objects.filter(description_vector__isnull=False, rating__isnull=False)
    if with_scenario:
        animes = animes.filter(poster__isnull=False).exclude(poster="")

    if with_poster:
        animes = animes.filter(image1__isnull=False)

    animes = animes.order_by('-rating')

    results = []
    for anime in animes:
        try:
            # Преобразуем бинарные данные обратно в вектор
            description_vector = np.frombuffer(anime.description_vector, dtype=np.float32)
            similarity = cosine_similarity(query_vector, description_vector)
            results.append((anime, similarity))
        except Exception as e:
            # Если возникает ошибка, пропускаем запись и продолжаем
            print(f"Ошибка при обработке Anime ID {anime.anime_id}: {e}")
            continue

    # Сортируем результаты по косинусному сходству
    results = sorted(results, key=lambda x: x[1], reverse=True)[:titles_per_page]

    results = sorted(results, key=lambda x: x[0].rating if x[0].rating  else 0, reverse=True)

    # Возвращаем только записи, игнорируя коэффициенты схожести
    return [anime for anime, similarity in results[:titles_per_page]]  # Возвращаем 5 самых релевантных
