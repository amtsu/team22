import pytest

from triangles import Triangle

@pytest.mark.parametrize("triangle,  expected",[
    ([3,6,5], 14),
    ([5,5,6], 16),
    ([12,5,5], None),
    ([3,4,5], 12)
])

def test_count_perimeter(triangle,  expected):
    some_triangle = Triangle(*triangle)
    assert some_triangle.count_perimeter() == expected

@pytest.mark.parametrize("triangle,  expected",[
    ([3,6,5], ['Разносторонний треугольник']),
    ([5,5,6], ['Равнобедренный треугольник']),
    ([5,5,5], ['Равносторонний треугольник']),
    ([12,5,5], None),
    ([3,4,5], ['Прямоугольный треугольник', 'Разносторонний треугольник'])
])

def test_define_type(triangle,  expected):
    some_triangle = Triangle(*triangle)
    assert some_triangle.define_type() == expected