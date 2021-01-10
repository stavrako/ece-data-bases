from tkinter.font import names
import pymysql
from tkinter import *
from tkinter.ttk import *

def main_update_idrima(id):
    id_idrimatos = id

    #--------------------------------------------------------------------------------------------
    root = Tk()
    root.title('Επεξεργασία Ιδρύματος στη Βάση')
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
        sql_command = "UPDATE ΙΔΡΥΜΑ SET Όνομα = %s WHERE Κωδικός_Ιδρύματος = " + id_idrimatos
        values = (idrima.get())
        cur.execute(sql_command,values)
        con.commit()
        answer.config(text='record updated')

    # Clear all inputs
    def clear():
        idrima.delete(0,END)

    #--------------------------------------------------------------------------------------------
    # Get current values
    def get_init():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT Όνομα FROM ΙΔΡΥΜΑ WHERE Κωδικός_Ιδρύματος = " + id_idrimatos)
        r = cur.fetchall()
        cur.close()
        con.close()
        return r

    # Insert current values to entries
    def init_entries_idrima():
        r = get_init()
        idrima.insert(0, str(r[0][0]))

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
    submit_btn = Button(root, text="Update record to database", command=submit)
    submit_btn.grid(row=2,column=0, pady=10, padx=10)
    
    clear_btn = Button(root, text="Clear fields", command=clear)
    clear_btn.grid(row=2,column=1, pady=10, padx=10)

    #--------------------------------------------------------------------------------------------
    answer = Label(root,text='')
    answer.grid(row=3,column=0,columnspan = 2)

    #--------------------------------------------------------------------------------------------
    init_entries_idrima()

    #--------------------------------------------------------------------------------------------
    root.mainloop()

    cur.close()
    con.close()