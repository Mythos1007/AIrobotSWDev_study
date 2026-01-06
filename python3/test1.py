class Student:
    def __init__(self, id: int, name: str, pnumber: str):
        self.__id = id
        self.__name = name
        self.__pnumber = pnumber

    def study(self):
        print('공부를 합니다.')
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_pnumber(self):
        return self.__pnumber
    
    def set_pnumber(self, pnumber):
        self.__pnumber = pnumber

chulsoo = Student(1, '철수', '010-1234-5678')
chulsoo.study()
print(chulsoo.get_name())  
chulsoo.set_name('철수책상철책상')
print('{}\t{}\t{}'.format(chulsoo.get_id(),chulsoo.get_name(),chulsoo.get_pnumber()))  

