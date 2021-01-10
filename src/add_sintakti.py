from tkinter.font import names
import pymysql
import datetime
from tkinter import *
from tkinter.ttk import *

def main_add_sintakti():
    root = Tk()
    root.title('Προσθήκη Συντάκτη στη Βάση')
    root.geometry("450x250")

    con = pymysql.connect(host = '150.140.186.221',
                                        port = 3306, 
                                        user='db20_up1059338',
                                        passwd='up1059338', 
                                        database='project_db20_up1059338')                                 
    cur = con.cursor()

    #--------------------------------------------------------------------------------------------
    # Create submit function
    def submit():
        sql_command = "INSERT INTO ΣΥΝΤΑΚΤΗΣ (Όνομα, Όνομα_Πατέρα, Επώνυμο, Ιδιότητα) VALUES (%s,%s,%s,%s)"
        values = (on_sintaktis.get(),mid_sintaktis.get(),ep_sintaktis.get(),idiotita.get())
        cur.execute(sql_command,values)
        con.commit()
        answer.config(text='record added')
        clear()

    # Clear all inputs
    def clear():
        on_sintaktis.delete(0,END)
        mid_sintaktis.delete(0,END)
        ep_sintaktis.delete(0,END)
        idiotita.delete(0,END)

    #--------------------------------------------------------------------------------------------
    # Create entry box
    on_sintaktis = Entry(root, width=30)
    on_sintaktis.grid(row=0, column=1,pady=10, padx =20)

    mid_sintaktis = Entry(root, width=30)
    mid_sintaktis.grid(row=1, column=1,pady=10, padx =20)

    ep_sintaktis = Entry(root, width=30)
    ep_sintaktis.grid(row=2, column=1,pady=10, padx =20)

    idiotita = Combobox(root, width=30, state="readonly")
    idiotita['values'] = ["","Καθηγητής", "Μεταπτυχιακός", "Διδάκτορας"]
    idiotita.grid(row=3, column=1,pady=10, padx =20)

    #--------------------------------------------------------------------------------------------
    # Create text box label
    on_sintaktis_label = Label(root, text="Όνομα Συντάκτη")
    on_sintaktis_label.grid(row=0, column=0)

    on_sintaktis_label = Label(root, text="Μεσαίο όνομα Συντάκτη")
    on_sintaktis_label.grid(row=1, column=0)

    ep_sintaktis_label = Label(root, text="Επώνυμο Συντάκτη")
    ep_sintaktis_label.grid(row=2, column=0)
    
    idiotita_label = Label(root, text="Ιδιότητα Συντάκτη")
    idiotita_label.grid(row=3, column=0)

    #--------------------------------------------------------------------------------------------
    # Create Submit Button
    submit_btn = Button(root, text="Add record to database", command=submit)
    submit_btn.grid(row=7,column=0, pady=10, padx=10)

    clear_btn = Button(root, text="Clear fields", command=clear)
    clear_btn.grid(row=7,column=1, pady=10, padx=10)

    #--------------------------------------------------------------------------------------------
    answer = Label(root, text='')
    answer.grid(row=8, column=0, columnspan = 2)

    #--------------------------------------------------------------------------------------------
    root.mainloop()
    
    cur.close()
    con.close()