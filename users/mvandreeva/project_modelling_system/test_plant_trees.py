"""
Тесты к модулю plant_trees.py
"""
import pytest
from plant_trees import PlantTrees, createinstance

def test_createinstance():
    """
    Тестирует функцию createinstance
    """
    # trees = createinstance(300, 100)
    trees = createinstance()
    type_trees = type(trees)
    assert type_trees == PlantTrees

def test_name():
    """
    Тестирует метод name
    """
    # trees = createinstance(300, 100)
    trees = createinstance()
    name = trees.name()
    assert name == "plant_trees"

def test_step():
    """
    Тестирует метод step
    """
    # plant_trees = PlantTrees(50, 5)
    plant_trees = PlantTrees()
    # prepare_trees = plant_trees.prepare()
    # trees_planted = prepare_trees.step()
    # print(trees_planted)
    # plant_trees.prepare()
    trees_planted = plant_trees.step()
    print(trees_planted)
    assert trees_planted == (5,5)

def test_is_done():
    """
    Тестирует метод is_done
    """
    # plant_trees = PlantTrees(10, 5)
    plant_trees = PlantTrees()
    # prepare_trees = plant_trees.prepare()
    # trees_planted = prepare_trees.step()
    plant_trees.step()
    complete_plant = plant_trees.is_done()
    assert complete_plant is True
