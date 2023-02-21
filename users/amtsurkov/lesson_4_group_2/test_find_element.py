from find_elenemt import find_elenemt

def test_1():
    # первый тест на наличе Petya
    index_petya = find_elenemt('Petya', ['Vast', 'Petya', 'Misha', 'Vova'])
    if index_petya != 1:
        # исключения надо проговорить
        assert False
        
def test_2():
    # вторй тест на наличе Kolya
    index_petya = find_elenemt('Kolya11', ['Vast', 'Kolya', 'Misha', 'Vova'])
    if index_petya != 1:
        # исключения надо проговорить
        assert False

def test_3():
    # теретий тест на наличе Misha
    index_petya = find_elenemt('Misha', ['Vast', 'Kolya', 'Misha', 'Vova'])
    if index_petya != 2:
        # исключения надо проговорить
        assert False
        
def test_4():
    # 4 тест на наличе Misha
    index_petya = find_elenemt('Misha', ['Vast', 'Kolya', 'Vova'])
    if index_petya != -1:
        # исключения надо проговорить
        assert False

def ttt():
    pass


def test_e():
    pass
    
#def test_all():
#    test_1()
#    test_2()
#    test_3()
#    test_4()
#    print('all test good')
       
#test_all()