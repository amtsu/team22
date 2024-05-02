from func_set import set_union, set_difference, is_subset, set_delete, set_all, set_intersection, all_union, set_isdisjoint, s_difference, set_symmetric_difference, create_set

def test_set_union():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4}
    assert {1,2,3,4,5} == set_union(set1, set2)  
test_set_union()
    
def test_set_difference():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4}
    assert {5} == set_difference(set1, set2)
test_set_difference()

def test_is_subset():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4}
    expected = False
    assert expected == is_subset(set1,set2)
test_is_subset()

def test_set_delete():
    set1 = {1,2,3,4,5}
    el = 5
    assert {1,2,3,4} == set_delete(set1, el)
test_set_delete()

def test_set_all ():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4}
    expected = False
    assert expected == set_all(set1, set2)
test_set_all()

def test_set_intersection ():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4}
    set3 = {1,2,3}
    assert {1,2,3} == set_intersection(set1, set2, set3)
test_set_intersection()

def test_all_union():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4}
    set3 = {1,2,3}
    assert {1,2,3,4,5} == all_union(set1, set2, set3)
test_all_union()

def test_set_isdisjoint ():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4}
    expected = False
    assert expected == set_isdisjoint(set1, set2)
test_set_isdisjoint()

def test_s_difference ():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3,4}
    assert {5} == s_difference(set1, set2)
test_s_difference()

def test_set_symmetric_difference ():
    set3 = {1,2,6,7}
    set4 = {4,5,6,7}
    assert {1,2,4,5} == set_symmetric_difference(set3, set4)
test_set_symmetric_difference()