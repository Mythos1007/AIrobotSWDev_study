import sqlite3

path= '/mnt/c/Users/User/databases/'
conn = sqlite3.connect(path + 'test3.db')
cur = conn.cursor()

sql = '''
CREATE TABLE "Person" (
	"ID"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"Pnumber"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
'''
cur.execute(sql)
conn.commit()
conn.close()

print('모시갱이가 생성되었습니다')