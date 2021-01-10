from tkinter.font import names
import pymysql
from tkinter import *
from tkinter.ttk import *

def main_add_idrima():
    root = Tk()
    root.title('Προσθήκη Ιδρύματος στη Βάση')
    root.geometry("450x150")

    con = pymysql.connect(host = '150.140.186.221',
                                        port = 3306, 
                                        user='db20_up1059338',
                                        passwd='up1059338', 
                                        database='project_db20_up1059338')                         
    cur = con.cursor()
    
    #--------------------------------------------------------------------------------------------
    # Create submit function
    def submit():
        sql_command = "INSERT INTO ΙΔΡΥΜΑ (Όνομα) VALUES (%s)"
        values = (idrima.get())
        cur.execute(sql_command,values)
        con.commit()
        answer.config(text='record added')
        clear()

    # Clear all inputs
    def clear():
        idrima.delete(0,END)

    #--------------------------------------------------------------------------------------------
    # Create entry box
    idrima = Entry(root, width=30)
    idrima.grid(row=1, column=1,pady=10, padx =20)

    #--------------------------------------------------------------------------------------------
    # Create text box label
    idrima_label = Label(root, text="Ίδρυμα")
    idrima_label.grid(row=1, column=0)

    #--------------------------------------------------------------------------------------------
    # Create Submit Button
    submit_btn = Button(root, text="Add record to database", command=submit)
    submit_btn.grid(row=2,column=0, pady=10, padx=10)

    clear_btn = Button(root, text="Clear fields", command=clear)
    clear_btn.grid(row=2,column=1, pady=10, padx=10)

    answer = Label(root,text='')
    answer.grid(row=3,column=0,columnspan = 2)

    root.mainloop()

    cur.close()
    con.close()