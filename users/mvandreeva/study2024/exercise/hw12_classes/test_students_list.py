from student_list import StudentList
from student import Student


def test_add_student():
    students = StudentList([Student("Fedor", "Semenov", 18, "Moscow, lubyanka 1", {'math': 5, 'rus': 4}), Student("Maria", "Semenova", 20, "Moscow, Petrovka 21", {'math': 4, 'rus': 5})])
    students.add_student("Vasya", "Ivanovskiy", 19, "Moscow, Tutuevo 27")
    assert students.show_students() == [{"name": "Fedor", "surname": "Semenov", "age": 18, "address": "Moscow, lubyanka 1", "record_book": {'math': 5, 'rus': 4}},{"name": "Maria", "surname": "Semenova", "age": 20, "address": "Moscow, Petrovka 21", "record_book": {'math': 4, 'rus': 5}},{"name": "Vasya", "surname": "Ivanovskiy", "age": 19, "address": "Moscow, Tutuevo 27", "record_book": {}}]

def test_expel():
    students = StudentList([Student("Fedor", "Semenov", 18, "Moscow, lubyanka 1", {'math': 5, 'rus': 4}), Student("Maria", "Semenova", 20, "Moscow, Petrovka 21", {'math': 4, 'rus': 5}), Student("Vasya", "Ivanovskiy", 19, "Moscow, Tutuevo 27")])
    students.expel("Vasya", "Ivanovskiy", 19, "Moscow, Tutuevo 27")
    assert students.show_students() == [{"name": "Fedor", "surname": "Semenov", "age": 18, "address": "Moscow, lubyanka 1", "record_book": {'math': 5, 'rus': 4}},{"name": "Maria", "surname": "Semenova", "age": 20, "address": "Moscow, Petrovka 21", "record_book": {'math': 4, 'rus': 5}}]