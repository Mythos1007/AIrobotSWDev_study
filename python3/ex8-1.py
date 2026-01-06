class Student:

    count = 0
    students = []

    @classmethod
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------- ------- -------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    
Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("박지호", 76, 96, 94, 90)
Student("김민수", 98, 92, 96, 92)
Student("이수민", 95, 98, 98, 98)
Student("김영희", 64, 88, 92, 92)
Student("박철수", 99, 96, 98, 100)
Student("최수정", 83, 86, 88, 92)
Student("장동건", 78, 82, 84, 86)
Student("강예빈", 85, 90, 92, 88)


Student.print()