from function import summ_sqrt
def test_1_summ_sqrt():
    assert summ_sqrt(1,2)==5
    
def test_2_summ_sqrt():
    assert not summ_sqrt(1,2)==4
