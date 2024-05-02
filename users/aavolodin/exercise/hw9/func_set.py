def set_union(set1, set2):
     new_set = set1|set2
     return new_set

def set_difference(set1, set2):
    new_set = set1 - set2
    return new_set

def is_subset(one_subset, two_subset):
    result = one_subset.issubset(two_subset)
    return result

def set_union1(set1, set2, set3):
     new_set2 = set1|set2|set3
     return new_set2

def element_del(set3, a):
    set3.discard(a)
    return set3

def i(set1, set2, set3):
    result = (set1&set2&set3)
    return result

def kej(set1, set2):
    return set1 == set2

def find_union(set1, set2, set3):
    return set1.union(set2, set3)

def dis(set1, set2):
    return set1.isdisjoint(set2)

def k(set1, set2):
    return set1 - set2

def symmetric(set1, set2):
    return set1.symmetric_difference(set2)

def create_set(*args):
    return set(args)