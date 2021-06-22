import sqlite3
import hash

def create(path,name):
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS {}(
        'username' VARCHAR(50),
        'Password' VARCHAR(100),
        'url' VARCHAR(50))
        '''.format(name))
    c.execute('''CREATE TABLE IF NOT EXISTS password(
        'password' VARCHAR(48)
    );''')

def insert(path,name,user,passw,url):
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('INSERT INTO {} VALUES(?,?,?)'.format(name),(user,passw,url))
    con.commit()

def update(path,key):
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('''INSERT INTO PASSWORD VALUES (?)''',(key,))
    con.commit()
