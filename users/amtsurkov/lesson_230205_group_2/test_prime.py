from check_prime import is_prime 

def test_1_is_prime():
    assert is_prime(5)
    
def test_2_is_prime():
    assert not is_prime(12)