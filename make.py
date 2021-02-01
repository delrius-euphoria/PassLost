import sqlite3

def create(path,name):
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS {}(
        'username' VARCHAR(50),
        'Password' VARCHAR(100),
        'url' VARCHAR(50))
        '''.format(name))

def insert(path,name,user,passw,url):
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('INSERT INTO {} VALUES(?,?,?)'.format(name),(user,passw,url))
    con.commit()
