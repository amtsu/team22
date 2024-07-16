import pytest
import sys
sys.path.append("..") 
from student import *

def test_student():
    student = Student("Petr", "Ivanov", 21, "Khimki, Melnikova 3")
    assert student.full_name == "Petr Ivanov"
    assert student.address == "Khimki, Melnikova 3"
    assert student.age == 21

    student.mark_add("history", 5)
    student.mark_add("maths", 4)
    student.mark_add("philosophy", 3, datetime.date(2014, 4, 12))

    assert len(student) == 3

    with pytest.raises(ValueError):
        student.mark_add("m", 4)

    with pytest.raises(ValueError):
       student.mark_add("math", 6)


def test_student_extended():
    student = Student("Ibragim", "Sultanov", 19, "Moscow, Ostozhenka 3, 33")

    student.mark_add("history", 5)
    student.mark_add("maths", 4)
    student.mark_add("philosophy", 3)
    student.mark_add("history", 3)
    student.mark_add("maths", 5)
    student.mark_add("philosophy", 5)

    assert student.averange_mark == 4.17
