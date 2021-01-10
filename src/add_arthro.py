import pymysql
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
import shutil
import add_periodiko
import add_teuxos
import add_sintakti
import add_idrima


def main_add_arthro():
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
            int(start_page.get())
            int(end_page.get())
            numerror1.config(text='')
            numerror2.config(text='')
            submit()
        except ValueError:
            numerror1.config(text='please enter integer')
            numerror2.config(text='please enter integer')

    #--------------------------------------------------------------------------------------------
    # Create combobox selected functions
    def periodiko_selected(event):
        vol_teuxous.config(state="readonly")
        addteuxos_btn.config(state="normal")
        vol_teuxous['values']= [x[1] for x in get_teuxos(periodiko.get().split()[0])]

    def teuxos_selected(event):
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT Κωδικός_Τεύχους FROM ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ WHERE Αριθμός_Τεύχους = %s AND Κωδικός_Περιοδικού = %s", (vol_teuxous.get(), periodiko.get().split()[0],))
        global id_teuxos
        r = cur.fetchone()[0]
        id_teuxos = int(r)
        cur.close()
        con.close()

    def sintaktis_selected(event, x):
        global id_sintakti
        id_sintakti.append(sintaktis[x].get().split()[0])

    def idrima_selected(event, x):
        global id_idrima
        id_idrima.append(idrima[x].get().split()[0])

    def anafora_selected(event, x):
        global id_anafora
        id_anafora.append(anafora[x].get().split()[0])

    #--------------------------------------------------------------------------------------------
    # Individual useful queries
    def get_periodika():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT Κωδικός_Περιοδικού, Όνομα FROM ΠΕΡΙΟΔΙΚΟ")
        r = cur.fetchall()
        cur.close()
        con.close()
        return r

    def get_teuxos(id):
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT Κωδικός_Τεύχους, Αριθμός_Τεύχους FROM ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ WHERE Κωδικός_Περιοδικού = %s", id)
        r = cur.fetchall()
        cur.close()
        con.close()
        return r

    def get_arthra():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT Κωδικός_Άρθρου, Τίτλος FROM ΑΡΘΡΟ")
        r = cur.fetchall()
        cur.close()
        con.close()
        return r

    def get_sintakti():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT Κωδικός_Συντάκτη, Όνομα, Επώνυμο FROM ΣΥΝΤΑΚΤΗΣ")
        r = cur.fetchall()
        cur.close()
        con.close()
        return r

    def get_idrima():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT Κωδικός_Ιδρύματος, Όνομα FROM ΙΔΡΥΜΑ")
        r = cur.fetchall()
        cur.close()
        con.close()
        return r

    def getid():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("SELECT Κωδικός_Άρθρου FROM ΑΡΘΡΟ WHERE Τίτλος='%s' AND Κωδικός_Τεύχους='%s'" % (title.get(), id_teuxos,))
        r = cur.fetchone()[0]
        cur.close()
        con.close()
        return r

    #--------------------------------------------------------------------------------------------
    # Run other files
    def add_p():
        add_periodiko.main_add_periodiko()
    def add_t():
        add_teuxos.main_add_teuxos()
    def add_s():
        add_sintakti.main_add_sintakti()
    def add_i():
        add_idrima.main_add_idrima()

    def selectfile():
        global filedir
        filedir = fd.askopenfilename(filetypes = (("PDF files","*.pdf"),("all files","*.*")), title='Select file')
        arxeio.config(text = filedir)
        
    #--------------------------------------------------------------------------------------------
    # Create submit, clear and refresh function
    def submit():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        con.commit()
        sql_command = "INSERT INTO ΑΡΘΡΟ (Τίτλος, Αρχική_Σελίδα, Τελική_Σελίδα, Κωδικός_Τεύχους) VALUES (%s,%s,%s,%s)"
        values = (title.get(),int(start_page.get()),int(end_page.get()), id_teuxos)
        cur.close()
        con.close()
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        shutil.copy(filedir, 'C:\\articles\\' + str(getid()) + '.pdf')
        for index in range(len(sintaktis)):
            sql_command = "INSERT INTO Συντάσσει (Κωδικός_Συντάκτη, Κωδικός_Άρθρου,	Κωδικός_Ιδρύματος) VALUES (%s,%s,%s)"
            values = (id_sintakti[index], getid(), id_idrima[index])
            cur.execute(sql_command,values)
        con.commit()
        for id_a in id_anafora:
            sql_command = "INSERT INTO Αναφέρει (Κωδικός_Άρθρου, Κωδικός_Άρθρου_Αναφοράς) VALUES (%s,%s)"
            values = (getid(), id_a)
            cur.execute(sql_command,values)
            con.commit()
        cur.close()
        con.close()
        answer.config(text='record added')
        clear()

    # Clear all inputs
    def clear():
        title.delete(0,END)
        start_page.delete(0,END)
        end_page.delete(0,END)
        periodiko.set("")
        vol_teuxous.set("")

        for p in range(1,len(anafora)):
            anafora[p].grid_remove()
        for p in range(1,len(anafora)):
            anafora.pop()
        for p in range(1,len(sintaktis)):
            sintaktis[p].grid_remove()
            idrima[p].grid_remove()
        for p in range(1,len(sintaktis)):
            sintaktis.pop()
            idrima.pop()
        anafora[0].set("")
        sintaktis[0].set("")
        idrima[0].set("")
        global i,j,id_anafora,id_sintakti,id_idrima
        j=0
        i=0
        id_anafora =[]
        id_sintakti = []
        id_idrima = []
        addsintakti_btn.grid(row=7,column=3, pady=10, padx=10)
        addidrima_btn.grid(row=8,column=3, pady=10, padx=10)

        vol_teuxous.config(state="disable")
        addteuxos_btn.config(state="disable")
        arxeio.config(text = 'Επίλεξε το αρχείο σου')

    # Refresh in order to appear new adds
    def refresh():
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        periodiko['values']= get_periodika()
        vol_teuxous['values']= [x[1] for x in get_teuxos(periodiko.get())]
        for sin in sintaktis:
            sin['values'] = get_sintakti()
        for idr in idrima:
            idr['values'] = get_idrima()
        cur.close()
        con.close()

    # to add one more anafora
    def multiple_anafora():
        global j
        j += 1
        anafora.append(Combobox(root, width=20, state="readonly"))
        anafora[j]['values'] =  get_arthra()
        anafora[j].grid(row=6, column=2+j,pady=10, padx =20)
        anafora[j].bind("<<ComboboxSelected>>",lambda event, x=j :anafora_selected(event,x))
        
        root.geometry(str(500 + j*160)+"x550")

    # to add one more sintakti-idrima
    def multiple_sintakti():
        global i
        i += 1
        sintaktis.append(Combobox(root, width=20, state="readonly"))
        sintaktis[i]['values'] = get_sintakti()
        sintaktis[i].grid(row=7, column=2+i,pady=10, padx =20)
        sintaktis[i].bind("<<ComboboxSelected>>",lambda event, x=i :sintaktis_selected(event,x))

        idrima.append(Combobox(root, width=20, state="readonly"))
        idrima[i]['values'] =  get_idrima()
        idrima[i].grid(row=8, column=2+i,pady=10, padx =20)
        idrima[i].bind("<<ComboboxSelected>>",lambda event, x=i :idrima_selected(event,x))
        
        root.geometry(str(500 + i*180)+"x550")
        addsintakti_btn.grid(row=7,column=3+i, pady=10, padx=10)
        addidrima_btn.grid(row=8,column=3+i, pady=10, padx=10)

    #--------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------

    root = Tk()
    root.title('Προσθήκη Άρθρου στη Βάση')
    root.geometry("550x500")

    global id_teuxos, id_sintakti, id_idrima, id_anafora, filedir
    id_teuxos = 0
    id_sintakti = []
    id_idrima = []
    id_anafora = []
    filedir = ''
    global i,j
    i = 0
    j = 0

    #--------------------------------------------------------------------------------------------
    # Create entry box
    arxeio = Label(root, text = 'Επίλεξε το αρχείο σου', width=40)
    arxeio.grid(row=0, column=2, columnspan=2, pady=10, padx =5)

    title = Entry(root, width=20)
    title.grid(row=1, column=2, pady=10, padx =5)

    start_page = Entry(root, width=20)
    start_page.grid(row=2, column=2, pady=10, padx =5)

    end_page = Entry(root, width=20)
    end_page.grid(row=3, column=2, pady=10, padx =5)

    periodiko = Combobox(root, width=20, state="readonly")
    periodiko['values']= get_periodika()

    periodiko.bind("<<ComboboxSelected>>",periodiko_selected)
    periodiko.grid(row=4, column=2, pady=10, padx =5)

    vol_teuxous = Combobox(root, width=20, state="disabled")
    vol_teuxous.grid(row=5, column=2, pady=10, padx =5)
    vol_teuxous.bind("<<ComboboxSelected>>",teuxos_selected)

    anafora = [Combobox(root, width=20, state="readonly")]
    anafora[0]['values'] =  get_arthra()
    anafora[0].grid(row=6, column=2,pady=10, padx =5)
    anafora[0].bind("<<ComboboxSelected>>", lambda event, x=0 :anafora_selected(event,x))

    sintaktis = [Combobox(root, width=20, state="readonly")]
    sintaktis[0]['values'] = get_sintakti()
    sintaktis[0].grid(row=7, column=2,pady=10, padx =5)
    sintaktis[0].bind("<<ComboboxSelected>>", lambda event, x=0 :sintaktis_selected(event,x))

    idrima = [Combobox(root, width=20, state="readonly")]
    idrima[0]['values'] =  get_idrima()
    idrima[0].grid(row=8, column=2,pady=10, padx =5)
    idrima[0].bind("<<ComboboxSelected>>", lambda event, x=0 :idrima_selected(event,x))

    #--------------------------------------------------------------------------------------------
    # Create text box label
    arxeio_label = Label(root, text="Αρχείο")
    arxeio_label.grid(row=0, column=0, columnspan=2)

    title_label = Label(root, text="Title")
    title_label.grid(row=1, column=0, columnspan=2)

    start_page_label = Label(root, text="Start page")
    start_page_label.grid(row=2, column=0, columnspan=2)

    end_page_label = Label(root, text="End page")
    end_page_label.grid(row=3, column=0, columnspan=2)

    periodiko_label = Label(root, text="Περιοδικό")
    periodiko_label.grid(row=4, column=0, columnspan=2)

    vol_teuxous_label = Label(root, text="Τεύχος")
    vol_teuxous_label.grid(row=5, column=0, columnspan=2)

    anafora_label = Label(root, text="Αναφορά σε άρθρο")
    anafora_label.grid(row=6, column=0)

    sintaktis_label = Label(root, text="Συντάκτης")
    sintaktis_label.grid(row=7, column=0)

    idrima_label = Label(root, text="Ίδρυμα")
    idrima_label.grid(row=8, column=0, columnspan=2)

    #--------------------------------------------------------------------------------------------
    # Create Button
    submit_btn = Button(root, text="Add record to database", command=validate_number)
    submit_btn.grid(row=12, column=0, pady=10, padx=10)

    clear_btn = Button(root, text="Clear fields", command=clear)
    clear_btn.grid(row=12, column=2, pady=10, padx=10)

    selfile_btn = Button(root, text="Select file", command=selectfile)
    selfile_btn.grid(row=0, column=4, pady=10, padx=10)

    refresh_btn = Button(root, text="Refresh", command=refresh)
    refresh_btn.grid(row=13, column=0, pady=10, padx=10)

    newsin_btn = Button(root, text="+", width=2, command=multiple_sintakti)
    newsin_btn.grid(row=7, column=1, pady=10, padx=10)

    newanaf_btn = Button(root, text="+", width=2, command=multiple_anafora)
    newanaf_btn.grid(row=6, column=1, pady=10, padx=10)

    addper_btn = Button(root, text="add Περιοδικό", command=add_p)
    addper_btn.grid(row=4, column=3, pady=10, padx=10)

    addteuxos_btn = Button(root, text="add Τεύχος", command=add_t, state= "disable")
    addteuxos_btn.grid(row=5, column=3, pady=10, padx=10)

    addsintakti_btn = Button(root, text="add Συντάκτη", command=add_s)
    addsintakti_btn.grid(row=7, column=3, pady=10, padx=10)

    addidrima_btn = Button(root, text="add Ίδρυμα", command=add_i)
    addidrima_btn.grid(row=8, column=3, pady=10, padx=10)

    #--------------------------------------------------------------------------------------------
    # Create Comments on window 
    answer = Label(root, text='')
    answer.grid(row=12, column=3, columnspan = 2)

    numerror1 = Label(root, text='')
    numerror1.grid(row=2, column=3)

    numerror2 = Label(root, text='')
    numerror2.grid(row=3, column=3)
    
    #--------------------------------------------------------------------------------------------
    root.mainloop()