import sqlite3

def create(path):
    con = sqlite3.connect(path)
    c = con.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS DETAILS(
        'username' VARCHAR(50),
        'password' VARCHAR(100),
        'url' VARCHAR(50)
    );''')
    c.execute('''CREATE TABLE IF NOT EXISTS MASTER(
        'master_hash' VARCHAR(32),
        'master_salt' VARCHAR(16)
    );''')

def insert(path,user,passw,url):
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('INSERT INTO DETAILS VALUES(?,?,?)',(user,passw,url))
    con.commit()

def update(path,hash,salt):
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('''INSERT INTO MASTER VALUES (?,?)''',(hash,salt))
    con.commit()

if __name__ == '__main__':
    pass
