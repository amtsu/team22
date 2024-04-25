from student import Student
from file_methods import FileMethods


class EducationInstitution(FileMethods):
    def __init__(self):
        super().__init__()
        self.__list_of_students: list[Student] = []

    def __len__(self):
        return len(self.__list_of_students)

    def add_student(self, student: Student):
        self.__list_of_students.append(student)

    def expel_student(self, student: Student):
        name = student.name
        surname = student.surname
        for body in self.__list_of_students:
            if body.name == name and body.surname == surname:
                self.__list_of_students.remove(body)
                break
        else:
            raise ValueError('Такой студент не числиться в учебном заведении!')

    def show_students(self):
        for student in self.__list_of_students:
            print(student)


if __name__ == "__main__":
    student_1 = Student('Ivan', 'Petrov', 17, 'Moscow', [5, 4, 3, 2, 5])
    student_2 = Student('Petr', 'Ivanov', 18, 'Moscow', [5, 4, 5, 5, 5])
    msu = EducationInstitution()
    msu.add_student(student_1)
    msu.add_student(student_2)
    msu.dump_obj()
    new_msu: EducationInstitution = EducationInstitution.load_obj('default.pickle')
    new_msu.expel_student(student_2)
    new_msu.dump_obj()
    new_msu_2: EducationInstitution = EducationInstitution.load_obj('default.pickle')
    assert len(new_msu_2) == len(msu) - 1
    assert len(new_msu_2) == len(new_msu)
