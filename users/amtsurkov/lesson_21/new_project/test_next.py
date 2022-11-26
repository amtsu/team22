from quadro import quadro

def test_quadro_number_10():
    if quadro(10) != 100:
        assert False
        
def test_quadro_number_20():
    if quadro(20) != 400:
        assert False