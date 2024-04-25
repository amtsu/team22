from file_methods import FileMethods


class Student(FileMethods):
    def __init__(self, name: str, surname: str, age: int, address: str, list_of_grades: list[int]):
        super().__init__()
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.list_of_grades = list_of_grades

    def __str__(self):
        info = f'{self.surname} {self.name}. Средний балл: {self.avg_rating()}'
        return info

    def add_grade(self, grade):
        self.list_of_grades.append(grade)

    def avg_rating(self) -> int | float:
        return round(sum(self.list_of_grades) / len(self.list_of_grades), 2)


if __name__ == "__main__":
    student = Student('Ivan', 'Petrov', 17, 'Moscow', [5, 4, 3, 2, 5])
    student.dump_obj()
    new_student: Student = Student.load_obj('default.pickle')
    new_student.add_grade(1)
    new_student.dump_obj()
    new_student_2: Student = Student.load_obj('default.pickle')
    assert new_student_2.list_of_grades[:-1] == student.list_of_grades
    assert new_student_2.list_of_grades == new_student.list_of_grades
