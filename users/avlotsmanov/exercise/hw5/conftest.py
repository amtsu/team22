import pytest

@pytest.fixture
def fix_set():
    set1 = {0, 1, 2, 3, 4, 5, 6, 8}
    set2 = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    set3 = {14, 15, 16}
    set4 = {1, 2, 3}
    set5 = {3, 6, 9, 11, 14}
    set0 = set()
    s1 = 5
    
    return set1, set2, #set3, set4, set5, set0, s1

@pytest.fixture
def setup_teardown():
    print('test_start')
    
    yield

    print('test_finish')