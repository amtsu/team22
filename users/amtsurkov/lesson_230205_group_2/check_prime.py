def is_prime(x : int) -> bool:
    """
    функция принимет оди аргумент(число) и определяет простоео он или составное
    """
    chisla = range(1, x + 1)
    list_chisel_na_kotorye_delitsy_x = []
    for i in chisla:    
        if x % i == 0:
            list_chisel_na_kotorye_delitsy_x.append(i)
            
    if len(list_chisel_na_kotorye_delitsy_x) < 3:
        is_prime_number = True
    else:
        is_prime_number = False
      
    return is_prime_number 