import sqlite3
import hashlib

conn = sqlite3.connect('usernames.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS userinfo(
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT)'''       
)

def hash_psw(password):
    hash_object = hashlib.sha1(bytes(str(password), encoding='utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def insert(id, username, password):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO userinfo VALUES (?, ?, ?)", (id, username, hash_psw(password)))
        conn.commit()
        print("Data uploaded successfully!")
    except Exception as e:
        print("Error", str(e))
        
def fetch_password(username):
    try:
        cursor.execute("SELECT PASSWORD FROM userinfo WHERE username=?", (username,))
        data = cursor.fetchone()
        if data != None:
            print("Success")
        else:
            print("Password incorrect")
    except Exception as e:
        print("Error", str(e))
        
fetch_password("Chrisl23")
    
    

