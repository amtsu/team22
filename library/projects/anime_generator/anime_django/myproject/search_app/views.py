from django.shortcuts import render
from .forms import SearchForm
from .models import Anime
from .utils import vector_search  # Импортируем функцию векторного поиска
from django.db.models import Q


def search_view(request):
    form = SearchForm()
    results = []
    query_submitted = False
    show_scenario_and_poster = True
    translate_to_russian = True
    safe_search = False

    if request.GET.get('query') or request.GET.get('query') == "":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            vector = form.cleaned_data['vector']
            with_scenario = form.cleaned_data['with_scenario']
            with_poster = form.cleaned_data['with_poster']
            show_scenario_and_poster = form.cleaned_data['show_scenario_and_poster']
            translate_to_russian = form.cleaned_data['translate_to_russian']
            safe_search = form.cleaned_data['safe_search']
            titles_per_page = int(form.cleaned_data.get('titles_per_page', '25'))  # Значение по умолчанию — 25
            sets = int(form.cleaned_data.get('sets', '0'))

            if vector and query:
                results = vector_search(query, with_scenario, with_poster, titles_per_page)

                if with_scenario:
                    results = [item for item in results if item.poster is not None]
                if with_poster:
                    results = [item for item in results if item.image1 is not None]
                if safe_search:
                    results = [item for item in results if
                               (item.adult_score and item.adult_score < 0.999 and item.description and " rape" not in item.description and
                                " sex" not in item.description and " humiliat" not in item.description and " erotic" not in item.description)]

            else:
                results = Anime.objects.filter(rating__isnull=False)
                set1 = [320, 306, 1292, 4970, 101, 656, 713, 47, 22147, 1797, 1798, 54, 1554, 66, 375, 374, 2220, 368,
                        357, 59, 60, 32407, 1575, 2904, 982, 1, 485, 1494, 1535, 2164, 3702, 293, 1757, 1756, 1752,
                        2166, 226, 365, 34662, 33047, 38084, 356, 227, 71, 73, 1015, 72, 121, 5114, 430, 126, 1829,
                        1056, 243, 507, 133, 881, 1016, 134, 387, 3298, 270, 777, 379, 934, 1889, 1977, 581, 256, 578,
                        431, 1956, 1230, 940, 2132, 1622, 3958, 143, 1530, 572, 757, 33, 147, 486, 2175, 1379, 3466,
                        3323, 412, 237, 28623, 433, 4472, 1088, 512, 221, 330, 1039, 164, 4879, 601, 615, 920, 921,
                        1978, 2966, 853, 1034, 564, 710, 941, 64, 45, 46, 44, 205, 2605, 24, 199, 339, 2104, 355, 2216,
                        169, 30, 32, 1633, 3588, 2452, 198, 565, 849, 182, 513, 51, 885, 2236, 1703, 523, 4224, 3457,
                        4752, 202, 1023, 497, 1195]

                if sets == 1:
                    results = results.filter(anime_id__in=set1)

                if query:
                    results = results.filter(
                        Q(description__icontains=query) | Q(title__icontains=query)
                    )
                if with_scenario:
                    results = results.filter(poster__isnull=False)
                if with_poster:
                    results = results.filter(image1__isnull=False)
                    results = results.filter(
                        Q(image0__isnull=False) | Q(image1__isnull=False) | Q(image2__isnull=False) | Q(
                            image3__isnull=False)
                        | Q(image4__isnull=False) | Q(image5__isnull=False) | Q(image6__isnull=False)
                    )
                if safe_search:
                    results = results.filter(adult_score__lte=0.999)
                    results = results.exclude(description__icontains=" rape")
                    results = results.exclude(description__icontains=" sex")
                    results = results.exclude(description__icontains=" humiliat")
                    results = results.exclude(description__icontains=" erotic")

                results = results.order_by('-rating')
                # results = results.order_by('-adult_score')
                results = results[:titles_per_page]

    idx = 1
    for result in results:
        result.title = result.title.replace('__', ': ').replace('_', ' ')
        result.idx = idx
        idx += 1

    context = {
        'form': form,
        'results': results,
        'query_submitted': query_submitted,
        'show_scenario_and_poster': show_scenario_and_poster,
        'translate_to_russian': translate_to_russian,
        'safe_search': safe_search,
        'len_results': len(results)
    }
    return render(request, 'search_app/search.html', context)
