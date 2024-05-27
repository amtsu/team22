import pytest
import sys
sys.path.append("..") 
from matrix import *

def test_matrix():

    m1 = Matrix([[1, 2, 3], [5, 6, 7], [7, 6, 5]])
    m2 = Matrix([[4, 3, 3], [2, 1, 3], [5, 6, 8]])

    assert m1 + m2 == [[5, 5, 6], [7, 7, 10], [12, 12, 13]]
    assert m1 - m2 == [[-3, -1, 0], [3, 5, 4], [2, 0, -3]]
    assert m1*m2 == [[23, 23, 33], [67, 63, 89], [65, 57, 79]]
    assert m1.trans() == [[1, 5, 7], [2, 6, 6], [3, 7, 5]]
    assert m2.det() == -22.0
    assert m2.inv() == [[0.45, 0.27, -0.27], [0.05, -0.77, 0.27], [-0.32, 0.41, 0.09]]

    
