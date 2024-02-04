import pytest


# тест пузырьковой сортировки
def test_bubble_sort_10():
    print(bubble_sort([7, 5, 9, 4, 8, 2, 6, 1, 3, 8]))
    if bubble_sort([7, 5, 9, 4, 8, 2, 6, 1, 3, 8]) == ([1, 2, 3, 4, 5, 6, 7, 8, 8, 9]):
        print ("passed")
    else:
        assert False
        
# тест сортировки выбором
def test_select_sort_10():
    #print(select_sort([7, 5, 9, 4, 8, 2, 6, 1, 3, 8]))
    if select_sort([7, 5, 9, 4, 8, 2, 6, 1, 3, 8]) == ([1, 2, 3, 4, 5, 6, 7, 8, 8, 9]):
        print ("passed")
    else:
        assert False
        
# тест сортировки вставкой
def test_insert_sort_10():
    #print(insert_sort([7, 5, 9, 4, 8, 2, 6, 1, 3, 8]))
    if insert_sort([7, 5, 9, 4, 8, 2, 6, 1, 3, 8]) == ([1, 2, 3, 4, 5, 6, 7, 8, 8, 9]):
        print ("passed")
    else:
        assert False
        
# тест сортировки Шелла
def test_shell_sort_10():
    print(shell_sort([7, 5, 9, 4, 8, 2, 6, 1, 3, 8]))
    if shell_sort([7, 5, 9, 4, 8, 2, 6, 1, 3, 8]) == ([1, 2, 3, 4, 5, 6, 7, 8, 8, 9]):
        print ("passed")
    else:
        assert False