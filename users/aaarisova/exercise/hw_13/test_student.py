'''2. Создав тест который загружет студента из файла, добаляет новую оценку и сохраняет в фаил.'''

import pytest
import pickle
from student_extended import Student


@pytest.fixture
def student():
    return Student('Ivan Vasilievich', 'Bunsha', 65, "Moscow", [5])

def test_new_grade(student): 
    file_name = 'file_student.pickle' 
    student.save_to_file(file_name)
    student.load_from_file(file_name) 
    student.add_grade(3) 
    student.save_to_file(file_name) 
    update_student = Student.load_from_file(file_name) 
    assert update_student.grades == [5, 3]
    