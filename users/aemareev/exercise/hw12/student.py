class Student:
    def __init__(self, name: str, surname: str, age: int, address: str, list_of_grades: list[int]):
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
    assert student.name == 'Ivan'
    assert student.surname == 'Petrov'
    assert student.age == 17
    assert student.address == 'Moscow'
    assert student.list_of_grades == [5, 4, 3, 2, 5]
    student.add_grade(1)
    assert len(student.list_of_grades) == 6
    assert student.avg_rating() == 3.33
