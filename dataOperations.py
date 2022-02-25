import sqlite3

def CatchData (database, table):
    con=sqlite3.connect(database)
    cur = con.cursor()
    cur.execute("SELECT * FROM {t};".format(t = table))
    return cur.fetchall()