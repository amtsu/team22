# search_app/forms.py

from django import forms
from search_app.consts.genre_list import GENRE_LIST


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=255, required=False)
    vector = forms.BooleanField(label='Векторный поиск', required=False, initial=True)
    with_scenario = forms.BooleanField(label='Со сценарием', required=False)
    with_poster = forms.BooleanField(label='Со постером', required=False)
    show_scenario_and_poster = forms.BooleanField(label='Показывать сценарий и описание постера', required=False,
                                                  initial=True)
    translate_to_russian = forms.BooleanField(label='Перевести на русский', required=False, initial=True)

    TITLES_PER_PAGE_CHOICES = [
        ('25', '25'),
        ('50', '50'),
        ('100', '100'),
        ('250', '250'),
        ('500', '500'),
        ('1000', '1000'),
        ('2500', '2500'),
        ('5000', '5000'),
        ('10000', '10000'),
    ]

    titles_per_page = forms.ChoiceField(
        choices=TITLES_PER_PAGE_CHOICES,
        label='Количество заголовков на странице',
        initial='25',
        required=False
    )

    SETS = [
        ('0', '0'),
        ('1', '1'),
    ]

    sets = forms.ChoiceField(
        choices=SETS,
        label='Сеты',
        initial='0',
        required=False
    )

    genre = forms.ChoiceField(
        choices=[(None, None), *zip(GENRE_LIST, GENRE_LIST)],
        label='Фильтр по жанру',
        initial=None,
        required=False
    )

    safe_search = forms.BooleanField(label='Безопасный поиск', required=False, initial=True)
