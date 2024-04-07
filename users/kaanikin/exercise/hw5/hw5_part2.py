def is_dict(some_dict):
    return isinstance(some_dict, dict)

def dict_add(input_dict, new_key, new_value):
    """
    функция добавления нового элемента в заданный словарь. 
    """
    if is_dict(input_dict) == False:
        raise TypeError #('На вход подан не словарь')
    else:
        input_dict[new_key] = new_value
        return input_dict

def dict_remove(pop_dict, pop_key):
    """
    функция удаляет элемент в заданном словаре
    """
    if is_dict(pop_dict) == False:
        raise TypeError ('На вход подан не словарь')
    else:
    
        if pop_key in pop_dict:
            del pop_dict[pop_key]
        else: 
            raise ValueError ('Заданый элмент отсутствует в словаре')
        return pop_dict

def total_fruit_cost(fruit_qty, fruit_prices):
    
    if (is_dict(fruit_qty) == False) or (is_dict(fruit_prices) == False):
        raise TypeError ('На вход подан не словарь')
    
    total_cost = 0
    
    for item in fruit_prices:
        if item not in fruit_qty:
            raise ValueError ('Заданый элемент отсутствует в словаре с ассортиментом')
        elif item not in fruit_prices:
            raise ValueError ('Заданый элемент отсутствует в словаре с ценами')
        else:
            total_cost += fruit_qty[item]*fruit_prices[item]
    
    return total_cost
    