from tkinter.font import names
import pymysql
from tkinter import *

def main_add_periodiko():
    root = Tk()
    root.title('Προσθήκη Περιοδικού στη Βάση')
    root.geometry("550x350")

    con = pymysql.connect(host = '150.140.186.221',
                                        port = 3306, 
                                        user='db20_up1059338',
                                        passwd='up1059338', 
                                        database='project_db20_up1059338')                                 
    cur = con.cursor()

    #--------------------------------------------------------------------------------------------
    # Check numbers
    def number():
        try:
            int(freq.get())
            float(im_factor.get())
            submit()
        except ValueError:
            numerror1.config(text='please enter integer')
            numerror2.config(text='please enter float number')

    #--------------------------------------------------------------------------------------------
    # Create submit function
    def submit():
        sql_command = "INSERT INTO ΠΕΡΙΟΔΙΚΟ (Κωδικός_Περιοδικού,   Όνομα,	Εκδότης,	Συχνότητα_Έκδοσης,	Γλώσσα,	Impact_factor) VALUES (%s,%s,%s,%s,%s,%s    )"
        values = (id.get(), name.get(), ekdotis.get(), int(freq.get()), language.get(), float(im_factor.get()))
        cur.execute(sql_command,values)
        con.commit()
        answer.config(text='record added')
        numerror1.config(text='')
        numerror2.config(text='')
        clear()

    # Clear all inputs
    def clear():
        id.delete(0,END)
        name.delete(0,END)
        ekdotis.delete(0,END)
        freq.delete(0,END)
        language.delete(0,END)
        im_factor.delete(0,END)

    #--------------------------------------------------------------------------------------------
    # Create text box
    id = Entry(root, width=30)
    id.grid(row=0, column=1,pady=10, padx =20)

    name = Entry(root, width=30)
    name.grid(row=1, column=1,pady=10, padx =20)

    ekdotis = Entry(root, width=30)
    ekdotis.grid(row=2, column=1,pady=10, padx =20)

    freq = Entry(root, width=30)
    freq.grid(row=3, column=1,pady=10, padx =20)

    language = Entry(root, width=30)
    language.grid(row=4, column=1,pady=10, padx =20)

    im_factor = Entry(root, width=30)
    im_factor.grid(row=5, column=1,pady=10, padx =20)

    #--------------------------------------------------------------------------------------------
    #Create text box label
    id_label = Label(root, text="ISSN")
    id_label.grid(row=0, column=0)

    name_label = Label(root, text="Όνομα Περιοδικού")
    name_label.grid(row=1, column=0)

    ekdotis_label = Label(root, text="Εκδότης")
    ekdotis_label.grid(row=2, column=0)

    freq_label = Label(root, text="Συχνότητα_Έκδοσης")
    freq_label.grid(row=3, column=0)

    language_label = Label(root, text="Γλώσσα")
    language_label.grid(row=4, column=0)

    im_factor_label = Label(root, text="Impact factor")
    im_factor_label.grid(row=5, column=0)

    #--------------------------------------------------------------------------------------------
    #Create Submit Button
    submit_btn = Button(root, text="Add record to database", command=number)
    submit_btn.grid(row=7,column=0, pady=10, padx=10)

    clear_btn = Button(root, text="Clear fields", command=clear)
    clear_btn.grid(row=7,column=1, pady=10, padx=10)

    answer = Label(root,text='')
    answer.grid(row=8,column=0,columnspan = 2)

    numerror1 = Label(root,text='')
    numerror1.grid(row=3,column=2)

    numerror2 = Label(root,text='')
    numerror2.grid(row=5,column=2)

    #--------------------------------------------------------------------------------------------
    root.mainloop()

    cur.close()
    con.close()