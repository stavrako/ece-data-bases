from tkinter.font import names
import pymysql
import datetime
from tkinter import *
from tkinter.ttk import *

def main_update_teuxos(id):
    id_teuxous = id

    #--------------------------------------------------------------------------------------------
    periodika = []
    root = Tk()
    root.title('Επεξεργασία Τεύχους στη Βάση')
    root.geometry("670x350")

    con = pymysql.connect(host = '150.140.186.221',
                                        port = 3306, 
                                        user='db20_up1059338',
                                        passwd='up1059338', 
                                        database='project_db20_up1059338')                                
    cur = con.cursor()

    #--------------------------------------------------------------------------------------------
    # Check numbers
    def validate_number():
        try:
            int(volume.get())
            numerror.config(text='')
            validate_date()
        except ValueError:
            numerror.config(text='please enter integer')
            
    def validate_date():
        try:
            datetime.datetime.strptime(date.get(), '%Y-%m-%d')
            submit()
        except ValueError:
            dateerror.config(text = "Incorrect data format, should be YYYY-MM-DD")

    #--------------------------------------------------------------------------------------------
    # Individual useful queries
    def getperiodika():
        cur.execute("SELECT Όνομα FROM ΠΕΡΙΟΔΙΚΟ")
        return cur.fetchall()

    def getidperiodikou(name):
        cur.execute("SELECT Κωδικός_Περιοδικού FROM ΠΕΡΙΟΔΙΚΟ WHERE Όνομα = %s", name)
        return cur.fetchall()

    def getnameperiodikou(id):
        cur.execute("SELECT Όνομα FROM ΠΕΡΙΟΔΙΚΟ WHERE Κωδικός_Περιοδικού = %s", id)
        return cur.fetchall()

    #--------------------------------------------------------------------------------------------
    # Create submit function
    def submit():
        sql_command = "UPDATE ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ SET Θέμα = %s, Αριθμός_Τεύχους = %s, Ημερομηνία_Έκδοσης = %s, Κωδικός_Περιοδικού = %s WHERE Κωδικός_Τεύχους = " + id_teuxous
        values = (subject.get(), int(volume.get()), date.get(), getidperiodikou(periodiko.get()))
        cur.execute(sql_command,values)
        con.commit()
        answer.config(text='record updated')
        numerror.config(text='')
        dateerror.config(text='')

    # Clear all inputs
    def clear():
        subject.delete(0,END)
        volume.delete(0,END)
        date.delete(0,END)
        periodiko.delete(0,END)

    #--------------------------------------------------------------------------------------------
    # Get current values
    def get_init():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT * FROM ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ WHERE Κωδικός_Τεύχους = " + id_teuxous)
        r = cur.fetchall()
        cur.close()
        con.close()
        return r

    # Insert current values to entries
    def init_entries_teuxos():
        r = get_init()
        subject.insert(0, str(r[0][1]))
        volume.insert(0, str(r[0][2]))
        date.insert(0, str(r[0][3]))
        periodiko.insert(0, getnameperiodikou(r[0][4]))

    #--------------------------------------------------------------------------------------------
    # Create text box
    subject = Entry(root, width=30)
    subject.grid(row=0, column=1,pady=10, padx =20)

    volume = Entry(root, width=30)
    volume.grid(row=1, column=1,pady=10, padx =20)

    date = Entry(root, width=30)
    date.grid(row=2, column=1,pady=10, padx =20)

    periodiko = Combobox(root, width=30)
    periodiko['values']= getperiodika()
    periodiko.grid(row=3, column=1,pady=10, padx =20)

    #--------------------------------------------------------------------------------------------
    # Create text box label
    subject_label = Label(root, text="Θέμα")
    subject_label.grid(row=0, column=0)

    volume_label = Label(root, text="Αριθμός Τεύχους")
    volume_label.grid(row=1, column=0)

    date_label = Label(root, text="Ημερομηνία έκδοσης")
    date_label.grid(row=2, column=0)

    periodiko_label = Label(root, text="Περιοδικό")
    periodiko_label.grid(row=3, column=0)

    #--------------------------------------------------------------------------------------------
    # Create Submit Button
    submit_btn = Button(root, text="Update record to database", command=validate_number)
    submit_btn.grid(row=6,column=0, pady=10, padx=10)

    clear_btn = Button(root, text="Clear fields", command=clear)
    clear_btn.grid(row=6,column=1, pady=10, padx=10)

    #--------------------------------------------------------------------------------------------
    answer = Label(root,text='')
    answer.grid(row=7,column=0,columnspan = 2)

    numerror = Label(root,text='')
    numerror.grid(row=1,column=2)

    dateerror = Label(root,text='')
    dateerror.grid(row=2,column=2)

    #--------------------------------------------------------------------------------------------
    init_entries_teuxos()

    #--------------------------------------------------------------------------------------------
    root.mainloop()

    cur.close()
    con.close()