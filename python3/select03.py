import sqlite3

path= '/mnt/c/Users/User/databases/'
conn = sqlite3.connect(path + 'test3.db')
cur = conn.cursor()

sql = "SELECT id, name, pnumber FROM person;"
cur.execute(sql)

rows = cur.fetchall()

for row in rows:
    person_id = row[0]      # id
    name = row[1]           # name
    pnumber = row[2]        # pnumber

    print(person_id, name, pnumber)

conn.close()