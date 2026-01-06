#sqlite3를 이용한 CRUD가 동작되는 python용 한국어 주소록/명함관리 프로그램 미니 프로젝트
#콘솔 메뉴를 만들어 입력 받아 동작이 되게 만들기
#이름 등 입력 예외 처리, 정규식을 통한 전화번호 입력 검증 - 모듈 re이용

import sqlite3

dbPath = "/mnt/c/Users/User/databases/addressbook.db"

class Person:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class AddressBook:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS contacts
                                 (id INTEGER PRIMARY KEY,
                                  name TEXT NOT NULL,
                                  phone TEXT NOT NULL,
                                  email TEXT,
                                  address TEXT)''')

    def add_contact(self, person):
        with self.conn:
            self.conn.execute('INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)',
                              (person.name, person.phone, person.email, person.address))

    def get_all_contacts(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM contacts')
        return cursor.fetchall()

    def update_contact(self, contact_id, person):
        with self.conn:
            self.conn.execute('UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?',
                              (person.name, person.phone, person.email, person.address, contact_id))

    def delete_contact(self, contact_id):
        with self.conn:
            self.conn.execute('DELETE FROM contacts WHERE id=?', (contact_id,))

    def close(self):
        self.conn.close()

def main():
    address_book = AddressBook(dbPath)

    while True:
        print("\n----- 주소록/명함관리 프로그램 -----")
        print("1. 명함 추가")
        print("2. 명함 보기")   
        print("3. 명함 수정")
        print("4. 명함 삭제")
        print("5. 종료")
        choice = input("원하는 작업을 선택하세요 (1 ~ 5): ")

        if choice == '1':
            name = input("이름: ")
            phone = input("전화번호: ")
            email = input("이메일: ")
            address = input("주소: ")
            person = Person(name, phone, email, address)
            address_book.add_contact(person)
            print("명함이 추가되었습니다.")
        elif choice == '2':
            contacts = address_book.get_all_contacts()
            for contact in contacts:
                print(contact)
        elif choice == '3':
            contact_id = int(input("수정할 명함의 ID를 입력하세요: "))
            name = input("새 이름: ")
            phone = input("새 전화번호: ")
            email = input("새 이메일: ")
            address = input("새 주소: ")
            person = Person(name, phone, email, address)
            address_book.update_contact(contact_id, person)
            print("명함이 수정되었습니다.")
        elif choice == '4':
            contact_id = int(input("삭제할 명함의 ID를 입력하세요: "))
            address_book.delete_contact(contact_id)
            print("명함이 삭제되었습니다.")
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
    address_book.close()
if __name__ == "__main__":
    main()

