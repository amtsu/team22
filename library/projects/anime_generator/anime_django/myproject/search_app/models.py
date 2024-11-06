# search_app/models.py

from django.db import models

class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    anime_id = models.IntegerField(unique=True, null=True, blank=True)
    ranked = models.IntegerField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    members = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    set = models.IntegerField(null=True, blank=True)
    scenario = models.TextField(null=True, blank=True)
    poster = models.TextField(null=True, blank=True)
    image1 = models.TextField(null=True, blank=True)
    image2 = models.TextField(null=True, blank=True)
    image3 = models.TextField(null=True, blank=True)
    image4 = models.TextField(null=True, blank=True)
    image5 = models.TextField(null=True, blank=True)
    image6 = models.TextField(null=True, blank=True)
    image0 = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    scenario_ru = models.TextField(null=True, blank=True)
    poster_ru = models.TextField(null=True, blank=True)
    title_orig = models.TextField(null=True, blank=True)
    title_en = models.TextField(null=True, blank=True)
    title_ru = models.TextField(null=True, blank=True)
    adult_score = models.FloatField(null=True, blank=True)

    # Новое поле для хранения вектора
    description_vector = models.BinaryField(null=True, blank=True)  # Хранение вектора в бинарном формате

    class Meta:
        db_table = 'anime'
        managed = False  # Это важно, чтобы Django не пытался создавать или изменять эту таблицу
