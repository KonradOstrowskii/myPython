import sqlite3
def create_table():
    conn = sqlite3.connect("lite1.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER,item TEXT,quantity INTEGER , price REAL)")
    conn.commit()
    conn.close()
    
def insert_data(id,item,quantity,price):
    conn = sqlite3.connect("lite1.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?,?)",(id,item,quantity,price))
    conn.commit()
    conn.close()

def delete(item):
    conn = sqlite3.connect("lite1.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item =?",(quantity,price,item))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("lite1.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows
insert_data(1,"love","infinity","price_less")
print(view())
delete("love")

print(view())
