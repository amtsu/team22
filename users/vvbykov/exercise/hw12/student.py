import datetime


class UniversityData:

    age_range = (17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28)
    marks_range = (2, 3, 4, 5)
    subjects = ("maths", "philosophy", "computer science", "pe", "history")

class StudentMark:

    def __init__(self, subject: str, mark: int, timestamp: datetime.date = None):
        if timestamp is None:
            timestamp = datetime.date.today()
        elif not isinstance(timestamp, datetime.date):
            raise ValueError("Invalid timestamp value")
        
        if not (mark in UniversityData.marks_range): 
            raise ValueError("Invalid mark value")        
        if not (subject.lower() in UniversityData.subjects):
            raise ValueError("Invalid subject value")

        self._timestamp = timestamp
        self._subject = subject
        self._mark = mark

    def __str__(self):
        return f"{self.timestamp}  {self.subject} \t {self.mark}"
    
    @property
    def timestamp(self):
        return self._timestamp

    @property
    def subject(self):
        return self._subject
    
    @property
    def mark(self):
        return self._mark


class Student:
    _cnt = 0

    def __new__(cls, *args, **kwargs):
        cls._cnt += 1
        return super().__new__(cls)    
    
    def __init__(self, first_name: str, second_name: str, age: int, address: str):
        self._marks = []
        self._first_name = first_name
        self._second_name = second_name
        self._address = address
        self._id = self._cnt
        
        if age in UniversityData.age_range:
            self._age = age
        else:
            raise ValueError("Invalid age value")

    def __len__(self):
        return len(self._marks)

    def __str__(self):
        return f"{self.id}\t{self.full_name}\t{self.averange_mark}"
    
    @property
    def id(self):
        return self._id
    
    @property
    def full_name(self):
        return f"{self._first_name} {self._second_name}"

    @property
    def age(self):
        return self._age

    @property
    def address(self):
        return self._address

    @property
    def marks(self) -> list:
        return self._marks

    @property
    def averange_mark(self) -> float:
        if len(self._marks) > 0:
            avr = 0
            for item in self._marks:
                avr += item.mark
            return round(avr/len(self._marks), 2)
        return -1
    
    def mark_add(self, subject: str, mark: int, timestamp: datetime.date = None):
        self._marks.append(StudentMark(subject, mark, timestamp))
                    
    def print_marks(self):
        for rec in self._marks:
            print(rec)


    
    
        