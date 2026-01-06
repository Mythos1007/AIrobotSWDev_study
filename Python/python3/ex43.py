class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    
if __name__ == "__main__":
    students = [
        Student('홍길동', 100, 100, 100, 100),
        Student('이순신', 99, 99, 99, 99),
        Student('강감찬', 97, 97, 97, 97),
        Student('을지문', 95, 95, 95, 95),
        Student('연개소', 85, 85, 85, 85)
    ]

    print('이름', '총점', '평균', sep='\t')
    for person in students:
        print(person.to_string()) 