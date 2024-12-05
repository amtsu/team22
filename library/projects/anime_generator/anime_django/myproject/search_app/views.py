import time
from typing import List, Optional

from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .consts.const_sets import my_anime_set
from .consts.forbidden_words import FORBIDDEN_WORDS
from .forms import SearchForm
from .models import Anime
from .utils import vector_search, vector_similar  # Импортируем функцию векторного поиска
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_view(request: HttpRequest) -> HttpResponse:
    form = SearchForm()
    results: List[Anime] = []
    query_submitted: bool = False
    show_scenario_and_poster: bool = True
    translate_to_russian: bool = True
    safe_search: bool = False
    start_time: float = time.time()
    len_results = 0

    if request.GET.get('query') is not None:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            vector = form.cleaned_data['vector']
            with_scenario = form.cleaned_data['with_scenario']
            with_poster = form.cleaned_data['with_poster']
            show_scenario_and_poster = form.cleaned_data['show_scenario_and_poster']
            translate_to_russian = form.cleaned_data['translate_to_russian']
            safe_search = form.cleaned_data['safe_search']
            genre = form.cleaned_data['genre']
            titles_per_page: int = int(form.cleaned_data.get('titles_per_page', '25'))  # Значение по умолчанию — 25
            sets: int = int(form.cleaned_data.get('sets', '0'))

            results, len_results = get_results(query, vector, with_scenario, with_poster, safe_search, titles_per_page, sets, genre, request)
            query_submitted = True

    for idx, result in enumerate(results, start=1):
        result.title = result.title.replace('__', ': ').replace('_', ' ')
        result.idx = idx

    took_time: float = time.time() - start_time

    context = {
        'form': form,
        'took_time': f"{took_time:.2f}",
        'results': results,
        'query_submitted': query_submitted,
        'show_scenario_and_poster': show_scenario_and_poster,
        'translate_to_russian': translate_to_russian,
        'safe_search': safe_search,
        'len_results': len_results
    }
    return render(request, 'search_app/search.html', context)


def get_results(
        query: Optional[str],
        vector: Optional[List[float]],
        with_scenario: bool,
        with_poster: bool,
        safe_search: bool,
        titles_per_page: int,
        sets: int,
        genre: Optional[str],
        request: HttpRequest
):
    try:
        maybe_anime_id = int(query)
        if maybe_anime_id:
            result1 = Anime.objects.filter(anime_id=query)
            if len(result1) > 0:
                anime_id = result1[0].anime_id
                results = list(
                    [result1[0]] + [v for v in vector_similar(anime_id, titles_per_page) if v.anime_id != anime_id])

                if safe_search:
                    results = filter_forbidden_words(results)
                    results = [result for result in results if
                               not result.image_is_adult and
                               ('Hentai' not in result.genres if result.genres is not None else True) and
                               ('Hentai' not in result.predicted_genres if result.predicted_genres is not None else True)]

                return results, len(results)

    except ValueError:
        pass

    results = []
    len_results = 0

    if vector:
        results = vector_search(query, with_scenario, with_poster, titles_per_page)

        if with_scenario:
            results = [item for item in results if item.poster is not None]
        if genre:
            results = [item for item in results if item.genres is not None and genre in item.genres]
        if with_poster:
            results = [item for item in results if item.image1 is not None]
        if safe_search:
            results = filter_forbidden_words(results)
            results = [result for result in results if
                       not result.image_is_adult and
                       ('Hentai' not in result.genres if result.genres is not None else True) and
                       ('Hentai' not in result.predicted_genres if result.predicted_genres is not None else True)

                       ]

        len_results = len(results)

    if len(results) == 0:
        results = Anime.objects.filter(rating__isnull=False)

        if sets == 1:
            set1: List[int] = my_anime_set
            results = results.filter(anime_id__in=set1)

        if query:
            results = results.filter(
                Q(description__icontains=query) | Q(title__icontains=query)
            )

        if genre:
            results = results.filter(genres__icontains=genre)

        if with_scenario:
            results = results.filter(poster__isnull=False)

        if with_poster:
            image_fields: List[str] = ['image0', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6']
            image_query = Q()
            for field in image_fields:
                image_query |= Q(**{f"{field}__isnull": False})
            results = results.filter(image_query)

        if safe_search:
            for forbidden_word in FORBIDDEN_WORDS:
                results = results.exclude(description__icontains=forbidden_word)
            results = results.filter(adult_score__lte=0.999)
            results = results.filter(image_is_adult=False)
            results = results.exclude(genres__icontains='Hentai')
            results = results.exclude(predicted_genres__icontains='Hentai')

        results = results.order_by('-rating')
        # Настройка пагинации
        page = request.GET.get('page', 1)  # Текущая страница, по умолчанию 1
        paginator = Paginator(results, titles_per_page)  # titles_per_page записей на страницу

        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        len_results = paginator.count

    return results, len_results


def filter_forbidden_words(anime_list: List[Anime]) -> List[Anime]:
    return [
        item for item in anime_list
        if not any(word in item.description.lower() for word in FORBIDDEN_WORDS)
    ]
