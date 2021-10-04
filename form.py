import tkinter as tk
from tkinter.constants import ANCHOR, RAISED, RIDGE, S, SUNKEN
import sqlite3,datetime 
#TODO: make a gui form and save data in the file and password must be * showing.Use show attribute to do this

#window
root=tk.Tk()
root.geometry("200x200")
#textvariables
name_str=tk.StringVar()
pass_str=tk.StringVar()

#database and button function


# def insert_db(name,password):
    
def submit():
    with open(r"data.txt","a") as file:
        name=name_str.get()
        password=pass_str.get()
        file.write(f"username {name} signed at {datetime.datetime.now()}\n")
    
    """attaching database"""
    try:
        con=sqlite3.connect("data.db")
        cur=con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS data
                 (name VARCHAR(100),
                 password VARCHAR(100))
                 ''')
        cur.execute(f"""INSERT INTO data (name , password) VALUES {(name,password)}""")
        con.commit()
        print("done")
        con.close()
    except:
        raise Exception("DB error")
    name_str.set("") 
    pass_str.set("") 


#Entry widgets
name=tk.Entry(root,borderwidth=6,relief=RIDGE,textvariable=name_str)
name.grid(row=1,column=1)
password=tk.Entry(root,borderwidth=6,relief=RIDGE,show="*",textvariable=pass_str)
password.grid(row=2,column=1)

#Label
tk.Label(text="FORM").grid(row=0,column=1,pady=3)
tk.Label(text="Name").grid(row=1,column=0)
tk.Label(text="Password").grid(row=2,column=0)

#Button
btn=tk.Button(root,text="Submit",borderwidth=4,command=submit)
btn.grid(row=3,column=1,pady=4)
root.mainloop()