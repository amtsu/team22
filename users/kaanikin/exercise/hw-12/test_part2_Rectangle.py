import pytest
from part2_Rectangle import Rectangle

fig1 = Rectangle(6, 6)

def test_fig1_perim():
    expected = 24
    assert fig1.Perimetr() == expected

def test_fig1_square():
    expected = 36
    assert fig1.Square() == expected




fig2 = Rectangle(3, 4)

def test_fig2_perim():
    expected = 14
    assert fig2.Perimetr() == expected

def test_fig2_square():
    expected = 12
    assert fig2.Square() == expected




