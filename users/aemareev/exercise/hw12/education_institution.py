from student import Student


class EducationInstitution:
    def __init__(self):
        self.__list_of_students = []

    def __len__(self):
        return len(self.__list_of_students)

    def add_student(self, student: Student):
        self.__list_of_students.append(student)

    def expel_student(self, student: Student):
        if student not in self.__list_of_students:
            raise ValueError('Такой студент не числиться в учебном заведении!')
        self.__list_of_students.remove(student)

    def show_students(self):
        for student in self.__list_of_students:
            print(student)


if __name__ == "__main__":
    student_1 = Student('Ivan', 'Petrov', 17, 'Moscow', [5, 4, 3, 2, 5])
    student_2 = Student('Petr', 'Ivanov', 18, 'Moscow', [5, 4, 5, 5, 5])
    msu = EducationInstitution()
    msu.add_student(student_1)
    msu.add_student(student_2)
    assert len(msu) == 2
    msu.show_students()
    msu.expel_student(student_1)
    assert len(msu) == 1
    msu.show_students()
