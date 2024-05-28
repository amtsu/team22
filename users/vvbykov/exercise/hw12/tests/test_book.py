import pytest
import sys
sys.path.append("..") 
from book import *

def test_book():
    b1 = Book("A Study in Scarlet", "Arthur Conan Doyle", 162, "Ward Lock & Co")
    
    assert b1.author == "Arthur Conan Doyle"
    assert b1.pages == 162
    assert b1.publisher == "Ward Lock & Co"

    b1.author = "Vladimir Bykov"
    assert b1.author == "Vladimir Bykov"

    b1.publisher = "Varmaran"
    assert b1.publisher == "Varmaran"

    b1.pages = 99
    assert b1.pages == 99
    

    with pytest.raises(TypeError):
        b1.publisher = 99

    with pytest.raises(TypeError):
       b1.author = 99.9

    with pytest.raises(ValueError):
       b1.pages = -1
