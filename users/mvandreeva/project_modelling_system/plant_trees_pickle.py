"""
Модуль содержит функцию для загрузки данных о посадке растений в файл в формате pickle
"""

import pickle

def pt_save_pickle(file_name: str, area: int, trees_amount: int, space_between: int):
    """
    Функция сохраняет в файл словарь данных о посадке растений в формате pickle
    """
    data = {"Площадь":area, "Количество":trees_amount, "Расстояние между": space_between}
    with open(file_name,"wb") as file_w:
        pickle.dump(data,file_w)
