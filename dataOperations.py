import sqlite3

def CatchData (table):
    con=sqlite3.connect("crud_produtos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM {t};".format(t = table))
    return cur.fetchall()

def CreateData (table, data):
    con=sqlite3.connect("crud_produtos.db")
    cur = con.cursor()
    
    if (table == "category"):
        cur.execute("SELECT ID FROM category")
        ids = cur.fetchall()
        cur.executemany('''
INSERT INTO {t} (ID, NAME, DESCRIPTION) VALUES ({id}, ?, ?)
'''.format(t = table, id = ids[-1][-1] + 1), data) # ids[-1][-1] + 1 vai colocar o id da categoria como o ID anterior + 1

    else:
        cur.execute("SELECT ID FROM products")
        ids = cur.fetchall()
        cur.executemany('''
INSERT INTO {t} (ID, NAME, PRICE, DESCRIPTION, CATEGORY_ID) VALUES ({id}, ?, ?, ?, ?)
'''.format(t = table, id = ids[-1][-1] + 1), data) # Mesma logica

    con.commit()

def CatchDataByID (table, id):
    con=sqlite3.connect("crud_produtos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM {t} WHERE ID={id};".format(t = table, id = id))
    return cur.fetchall()

def UpdateData (table, data, id):
    con=sqlite3.connect("crud_produtos.db")
    cur = con.cursor()
    if table == 'products':
        cur.executemany("""
    UPDATE {t}
    SET NAME = ?, PRICE = ?, DESCRIPTION = ?, CATEGORY_ID = ?
    WHERE ID = {id};
    """.format(t = table, id = id), data)

    elif table == 'category':
        cur.executemany("""
    UPDATE {t}
    SET NAME = ?, DESCRIPTION = ?
    WHERE ID = {id};
    """.format(t = table, id = id), data)

    con.commit()


def DeleteData (table, id):
    con=sqlite3.connect("crud_produtos.db")
    cur = con.cursor()
    cur.execute("""
DELETE FROM {t}
WHERE id = {id};
""".format(t = table, id = id))

    con.commit()