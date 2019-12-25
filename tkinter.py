from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


FirstName=StringVar()
LastName=StringVar()
ID = StringVar()




def database():
   name=FirstName.get()
   lastname=LastName.get()
   Id =ID.get()

   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS BigData (FirstName TEXT,LastName TEXT,ID TEXT)')
   cursor.execute('INSERT INTO BigData (FirstName,LastName,ID) VALUES(?,?,?)',(name,lastname,Id))
   prnt = cursor.execute('SELECT * from BigData')
   conn.commit()
   print(prnt)
   
   

label_1 = Label(root, text="FirstName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=FirstName)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="LastName",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=LastName)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="ID",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root,textvar=ID)
entry_3.place(x=240,y=230)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

root.mainloop()


