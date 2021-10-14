import sqlite3

def get_db():
    conn=sqlite3.connect('database.db')
    return conn



def close_db(): 
    conn=get_db()   
    con=conn.close()
    return con