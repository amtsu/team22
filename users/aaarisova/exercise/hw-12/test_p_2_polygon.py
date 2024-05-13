import pytest
import math 
from p_2_polygon import Polygon

#polygon = Polygon() - если делаю тут, то вершину создает с координатами 0,0 - почему??

def test_add_perim_area_1():
    polygon = Polygon()
    polygon.add_vertex(0,0)
    polygon.add_vertex(0,2)
    polygon.add_vertex(2,2)
    polygon.add_vertex(2,0)
    assert polygon.vertices == [(0,0), (0,2), (2,2), (2,0)]
    assert polygon.perimeter() == 8
    assert polygon.polygon_area() == 4.0



def test_add_perim_area_2():
    polygon = Polygon()
    polygon.add_vertex(0,0)
    polygon.add_vertex(0,1)
    polygon.add_vertex(1,1)
    polygon.add_vertex(1,0)
    assert polygon.vertices == [(0,0), (0,1), (1,1), (1,0)]
    assert polygon.perimeter() == 4.0
    assert polygon.polygon_area() == 1.0


#мои расчеты 
#area= 0.5*|(0⋅2−0⋅0+0⋅2−2⋅2+2⋅0−2⋅2+2⋅0−0⋅0)|=0.5*|(-4-4)|=4
#perimeter = 
    # AB=sqrt((0-0)**2+(2-0)**2)=sqrt(4)=2
    # BC=sqrt((2-0)**2+(2-2)**2)=sqrt(4)=2
    # CD=sqrt((2-2)**2+(0-2)**2)=sqrt(4)=2
    # DA=sqrt((2-0)**2+(0-0)**2)=sqrt(4)=2
    # perimeter=2+2+2+2=8
    


