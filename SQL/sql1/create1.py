import sqlite3

path = "/mnt/c/Users/User/databases/"
conn = sqlite3.connect(path + "addressbook.db")

cur = conn. cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS "Person2" (
	id INTEGER PRIMARY KEY AUTOINCR,
	name	TEXT NOT NULL,
	pnumber	TEXT NOT NULL
	PRIMARY KEY("ID" AUTOINCREMENT)
);"""