from function import double_string
def test1_double_string():
    assert not double_string("abc")=="abcabc55"

def test2_double_string():
    assert double_string("abc")=="abcabc"
   

