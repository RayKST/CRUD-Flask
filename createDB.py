import sqlite3

con = sqlite3.connect('crud_produtos.db')
cur = con.cursor()

#Create tables
table1 ='''CREATE TABLE "category" (
	"ID"	INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
	"NAME"	TEXT,
	"DESCRIPTION"	TEXT
)'''

table2 ='''CREATE TABLE "products" (
	"ID"	INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
	"NAME"	TEXT,
	"PRICE"	REAL,
    "DESCRIPTION" TEXT,
    "CATEGORY_ID" INTEGER,
	FOREIGN KEY(CATEGORY_ID) REFERENCES category(ID)
)'''


cur.execute(table1)
cur.execute(table2)

#commit changes
con.commit()

#close the connection
con.close()
print("done")