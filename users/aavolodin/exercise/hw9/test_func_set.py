from func_set import set_union, set_difference, is_subset, set_union1, element_del, i, kej, find_union, dis, k, symmetric, create_set

def test_set_union():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6, 7}
    assert {1, 2, 3, 4, 5, 6, 7} == set_union(set1, set2)
test_set_union()    

def test_set_difference():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6, 7}
    assert {1, 2, 3} == set_difference(set1, set2)
test_set_difference()    

def test_is_subset():
    set1 = {4, 5}
    set2 = {4, 5, 6, 7, 8}
    assert True == is_subset(set1, set2)
test_is_subset()
    
def test_set_union1():
    set1 = {4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {500, 700, 123}
    assert {4, 5, 6, 7, 8, 500, 123, 700} == set_union1(set1, set2, set3)
test_set_union1()

def test_element_del():
    set3 = {500, 700, 123}
    assert {123, 500} == element_del(set3, 700)
test_element_del()

def test_i():
    set1 = {1, 2, 3}
    set2 = {3, 2, 1}
    set3 = {1, 2, 3, 4}
    assert {1, 2, 3} == i(set1, set2, set3)
test_i()

def test_kej():
    set1 = {1, 2, 3}
    set2 = {3, 2, 1}
    set3 = {1, 2, 3, 4}
    assert True, False == kej (set1, set2)
test_kej()

def test_find_union():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {500, 700, 123}
    assert {1, 2, 3, 4, 5, 6, 7, 8, 500, 123, 700} == find_union(set1, set2, set3)
test_find_union()

def test_dis():
    set1 = {1, 2, 3, 4, 5}
    set2 = { 6, 7, 8}
    assert True == dis(set1, set2)
test_dis()

def test_k():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    assert {1, 2, 3} ==  k(set1, set2)
test_k()

def test_symmetric():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    assert {1, 2, 3, 6, 7, 8} == symmetric(set1, set2)
test_symmetric()

def test_create_set():
    assert {1, 2, 3, 4, 5, 'laa'} == create_set(1, 2, 3, 4, 5, 'laa')
test_create_set()