from function import double_string1
def test1_double_string1():
    assert double_string1("abc")=="abc abc"

                          
def test2_double_string1():
    assert not double_string1("abc")=="abcabc"
                          