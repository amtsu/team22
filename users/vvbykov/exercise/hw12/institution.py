from student import *

class Institution:

    def __init__(self):
        self._students = []

    def __len__(self):
        return len(self._students)

    def __str__(self):
        result = f"There are no students"
        if len(self._students) > 0:
            result = f"ID \t Full name \t Avr. mark\n"
            result += f"="*40 + f"\n"
            for item in self._students:
                result += f"{item}\n"
        return result

    def admit(self, std: Student) -> int:
        if isinstance(std, Student):
            self._students.append(std)
            return len(self._students)
        else:
            raise TypeError("Invalid student type")
            
    def exclude(self, student_id: int) -> int:
        for item in self._students:
            if student_id == item.id:
                self._students.remove(item)
                return (len(self._students))
                
        return (len(self._students))
            
    def print0(self) -> str:
        return self._students[0].full_name
            
    
    