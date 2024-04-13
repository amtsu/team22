import pytest
from circle import Circle

circle = Circle(3, 'yellow')

def test_circle_radius():
    assert circle.radius == 3


def test_circle_color():
    assert circle.color == 'yellow'


def test_area():
    assert circle.area() == 28.26 
    

def test_perimeter():
    assert circle.perimeter() == 18.84

#########################################
circle_2 = Circle(0, 'red')  #негативный. функцию надо дорабатывать, чтобы r>0

def test_circle2_radius():
    assert circle_2.radius == 0


def test_circle2_color():
    assert circle_2.color == 'red'


def test_area2():
    assert circle_2.area() == 0 
    

def test_perimeter2():
    assert circle_2.perimeter() == 0


#########################################

circle_3 = Circle(-1, 'blue')  #негативный. функцию надо дорабатывать, чтобы r>0

def test_circle3_radius():
    assert circle_3.radius == -1


def test_circle3_color():
    assert circle_3.color == 'blue'


def test_area3():
    assert circle_3.area() == 3.14
    

def test_perimeter3():
    assert circle_3.perimeter() == -6.28
