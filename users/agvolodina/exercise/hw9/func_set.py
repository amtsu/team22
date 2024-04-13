def set_union(set1,set2):
    return set1.union(set2)

def set_difference(set1,set2):
     return set1.difference(set2)

def is_subset(set1,set2):
    subset_m = set1.issubset(set2)
    return subset_m

def set_delete(set1, el):
    set1.discard(el)
    return set1

def set_all (set1,set2):
    return set1==set2

def set_intersection (set1,set2,set3):
    return set1&set2&set3

def all_union(set1,set2,set3):
    return set1|set2|set3

def set_isdisjoint (set1,set2):
     return set1.isdisjoint(set2)

def s_difference(set1,set2):
     return set1-set2

def set_symmetric_difference(set1,set2):
    difference_m = set1^set2
    return difference_m

def create_set (elements):
    return set(elements)