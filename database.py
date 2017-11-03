#Import the sqlite package
import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text , isbn INTEGER, author text , year INTEGER ) ")
    conn.commit()
    conn.close()

def view():
        conn=sqlite3.connect("books.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows=cursor.fetchall()
        conn.commit()
        conn.close()
        return rows

def insert(title,isbn,author,year):
        conn=sqlite3.connect("books.db")
        cursor=conn.cursor()
        if title and isbn and author and year is not None:
              cursor.execute("INSERT INTO books VALUES  (NULL,?,?,?,?) ",(title,isbn,author,year))
        conn.commit()
        conn.close()

def search(title="",isbn="",author="",year=""):
        conn=sqlite3.connect("books.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title=? OR isbn=? OR author=? OR year=?",(title,isbn,author,year))
        rows=cursor.fetchall()
        conn.commit()
        conn.close()
        return rows

def delete(id):
        conn=sqlite3.connect("books.db")
        cursor=conn.cursor()
        cursor.execute("DELETE from books WHERE id=?",(id,))
        conn.commit()
        conn.close()

def update(id,title,isbn,author,year):
        conn=sqlite3.connect("books.db")
        cursor=conn.cursor()
        cursor.execute("UPDATE books SET title=?,isbn=?,author=?,year=? WHERE id=? ",(title,isbn,author,year,id))
        conn.commit()
        conn.close()



connect()
#insert(" ",5 ,"Rashmi Bansal", 2014)
#update(1,"Ignited Minds",45321,"APJ Abdul Kalam",2011)
#delete(1)
#print(view())
#print(search(author="APJ Abdul Kalam"))
