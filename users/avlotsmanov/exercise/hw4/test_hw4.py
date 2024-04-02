import pytest

from types import NoneType
from hw4 import count_in_poem, solyanka


#тесты для функции count_in_poem
@pytest.mark.parametrize(
    'input, expected_result',
    [
        (
            '''За стеклом лежал Питон,
Большой и толстый, как батон.
Вверх пополз,
Затем вернулся,
Круглым бубликом свернулся.''',
            (5, 16, 111)
        ),
    ]
)

def test_count_in_poem_positive(input, expected_result):
    assert count_in_poem(input) == expected_result

@pytest.mark.parametrize(
    'input, expected_exception',
    [
        (['1', '2', 'asd'], TypeError),
    ]
)

def test_count_in_poem_negative(input, expected_exception):
    with pytest.raises(expected_exception):
        count_in_poem(input)

#тесты для функции solyanka
@pytest.mark.parametrize(
    'input, expected_result',
    [
        (
            (
                'Hello', 1, 3.14, [1, 2, 8, 16], True, {'c', 'a', 'b'},
                ('x', 1, 'y', 2), {'Alex': 'Lots'}, range(0, 3), None
            ), 
            {
                NoneType, dict, float,int, list, bool, range, set, str, tuple
            } 
        ),
    ]
)

#непонятно почему он говорит что не находит NoneType
def test_solyanka_positive(input, expected_result):
    assert solyanka(*input) == expected_result



