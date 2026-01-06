class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
chulsoo = Student(1, '철수')
chulsoo.id = 2
chulsoo.name = "철수책상철책상"
print(chulsoo.id, ':', chulsoo.name)