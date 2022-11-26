from quadro import quadro

def test_quadro_number_2():
    if quadro(2) != 4:
        assert False
        
def test_quadro_number_5():
    if quadro(5) != 25:
        assert False
#        print('error')       

def test_quadro_number_6():
    assert quadro(6) == 36
    
    
def test_quadro_number_7():
    assert quadro(7) == 49