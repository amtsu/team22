def set_union(set1,set2):
    return set1|set2

def set_difference (set1,set2):
    return set1 - set2

def set_union_many (*sets):
    resultat = set () #empty set
    for i in sets :
        resultat = resultat.union(i)
    return resultat

def delete_value (set, var):
    if (var in set):
        set.remove(var)
    return set

def set_intersection_many (*sets):
    resultat = sets[0]
    for i in sets :
        resultat = resultat.intersection(i)
    return resultat

def equality_sets (set1, set2):
    return set1==set2

def disjunctive (set1,set2):
    if (set1 == set()) and (set2 == set()):
        return False
    result = set1&set2
    if (result==set()):
        return True
    else:
        return False

def create_set (*elements):
    return set(elements)

def merge_dict(dict1,dict2):
    return dict1|dict2 # произойдет перезапись 2 словарем