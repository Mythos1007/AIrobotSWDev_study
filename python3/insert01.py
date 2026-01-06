import sqlite3

path= '/mnt/c/Users/User/databases/'
conn = sqlite3.connect(path + 'test3.db')
cur = conn.cursor()

sql = '''
INSERT INTO Person (Name, Pnumber)
VALUES ('강감찬', '010-2222-2222')
);
'''
cur.execute(sql)
conn.commit()
conn.close()

print('모시갱이가 생성되었습니다')