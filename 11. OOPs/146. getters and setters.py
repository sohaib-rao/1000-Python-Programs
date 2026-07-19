class Student:
    def __init__(self):
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
            
    def get_grade(self):
        return self.__grade

s = Student()
s.set_grade(85)
print(s.get_grade()) 