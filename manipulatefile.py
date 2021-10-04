import sqlite3 as sql
con=sql.connect("data.db")
cur=con.cursor()




def view():
    cur.execute(
    """select * from data"""
    )#this statement is required to fetch values
    a=cur.fetchall()
    print(a)

def delete():
    cur.execute("delete from data")
    con.commit()

view()
con.close()