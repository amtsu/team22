from function import square_parameters
def test_1_square_parameters():
    a=(20, 25, 7.0710678118654755)
    square_parameters(5)==(20, 25, 7.0710678118654755)
    assert square_parameters(5)==a 
def test_2_square_parameters():
    square_parameters(5)==(20, 25, 7.0710678118654755)
    a=(20, 25, 7.0710678118654755)
    assert not square_parameters(5)!=a