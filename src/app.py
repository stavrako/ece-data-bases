from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import webbrowser
import pymysql
import add_arthro
import statistics
import update_arthro
import update_teuxos
import update_periodiko
import update_idrima
import update_sintakti

class DB:                         #creating a class DB with functions to perform various operations on the database. 
    def __init__(self):           #constructor functor for class DB.
        self.con = pymysql.connect(host = '150.140.186.221',
                                    port = 3306, 
                                    user='db20_up1059338',
                                    passwd='up1059338', 
                                    database='project_db20_up1059338')  #connects to a database called project_db20_up1059338
        self.cur = self.con.cursor()

    def __del__(self): #destructor created for the class DB
        self.con.close() #closes the connection with the database

    def update_arthro(self, id):    #to update the values of the selected row with the values passed by the user
        update_arthro.main_update_arthro(id)
        self.con.commit()
        view_command()
    
    def update_teuxos(self, id):    #to update the values of the selected row with the values passed by the user
        update_teuxos.main_update_teuxos(id)
        self.con.commit()
        view_command()

    def update_periodiko(self, id):    #to update the values of the selected row with the values passed by the user
        update_periodiko.main_update_periodiko(id)
        self.con.commit()
        view_command()
    
    def update_sintakti(self, id):    #to update the values of the selected row with the values passed by the user
        update_sintakti.main_update_sintakti(id)
        self.con.commit()
        view_command()
    
    def update_idrima(self, id):    #to update the values of the selected row with the values passed by the user
        update_idrima.main_update_idrima(id)
        self.con.commit()
        view_command()

    def delete_arthro(self, id): #to delete the row from the table given the value of the id of the selected row.
        self.qr = "DELETE FROM ΑΡΘΡΟ WHERE Κωδικός_Άρθρου = %s"
        self.cur.execute(self.qr, (id,))
        self.con.commit()
        view_command()

    def delete_teuxos(self, id): #to delete the row from the table given the value of the id of the selected row.
        self.qr = "DELETE FROM ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ WHERE Κωδικός_Τεύχους = %s"
        self.cur.execute(self.qr, (id,))	
        self.con.commit()
        view_command()
    
    def delete_periodiko(self, id): #to delete the row from the table given the value of the id of the selected row.
        self.qr = "DELETE FROM ΠΕΡΙΟΔΙΚΟ WHERE Κωδικός_Περιοδικού = %s"
        self.cur.execute(self.qr, (id,))
        self.con.commit()
        view_command()

    def delete_sintakti(self, id): #to delete the row from the table given the value of the id of the selected row.
        self.qr = "DELETE FROM ΣΥΝΤΑΚΤΗ WHERE Κωδικός_Συντάκτη = %s"
        self.cur.execute(self.qr, (id,))
        self.con.commit()
        view_command()

    def delete_idrima(self, id): #to delete the row from the table given the value of the id of the selected row.
        self.qr = "DELETE FROM ΙΔΡΥΜΑ WHERE Κωδικός_Ιδρύματος = %s"
        self.cur.execute(self.qr, (id,))
        self.con.commit()
        view_command()

    def view_arthro(self): #To view all the rows present in the table
        self.cur.execute("""SELECT a.Κωδικός_Άρθρου, a.Τίτλος, p.Κωδικός_Περιοδικού, p.Όνομα, t.Αριθμός_Τεύχους, p.Εκδότης, a.Αρχική_Σελίδα, a.Τελική_Σελίδα, 
                            GROUP_CONCAT(DISTINCT s2.Όνομα, " ", s2.Επώνυμο) AS "Συντάκτης", GROUP_CONCAT(DISTINCT i.Όνομα) AS "Ίδρυμα", GROUP_CONCAT(DISTINCT aa.Κωδικός_Άρθρου_Αναφοράς) AS "Κωδικός_Άρθρου_Αναφοράς", 
                            GROUP_CONCAT(DISTINCT l.Λέξη_κλειδί) AS "Λέξη_κλειδί" FROM ΑΡΘΡΟ a LEFT JOIN Συντάσσει s1 ON a.Κωδικός_Άρθρου = s1.Κωδικός_Άρθρου LEFT JOIN ΣΥΝΤΑΚΤΗΣ s2 ON s1.Κωδικός_Συντάκτη = s2.Κωδικός_Συντάκτη 
                            LEFT JOIN ΙΔΡΥΜΑ i ON s1.Κωδικός_Ιδρύματος = i.Κωδικός_Ιδρύματος LEFT JOIN ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ t ON a.Κωδικός_Τεύχους = t.Κωδικός_Τεύχους 
                            LEFT JOIN ΠΕΡΙΟΔΙΚΟ p ON t.Κωδικός_Περιοδικού = p.Κωδικός_Περιοδικού LEFT JOIN Αναφέρει aa ON a.Κωδικός_Άρθρου=aa.Κωδικός_Άρθρου LEFT JOIN Περιγράφεται l ON a.Κωδικός_Άρθρου = l.Κωδικός_Άρθρου
                            GROUP BY a.Κωδικός_Άρθρου ORDER BY p.Όνομα, t.Αριθμός_Τεύχους, a.Τίτλος""") #execute function is to perform the SQL operations. Here, it produces all the rows from the table.
        rows = self.cur.fetchall() #fetching all the rows one by one from the table and storing it in list rows
        return rows

    def view_teuxos(self): #To view all the rows present in the table
        self.cur.execute("""SELECT t.Κωδικός_Τεύχους, p.Κωδικός_Περιοδικού, p.Όνομα, t.Αριθμός_Τεύχους, t.Θέμα, Ημερομηνία_Έκδοσης, GROUP_CONCAT(DISTINCT l.Λέξη_κλειδί) AS "Λέξη_κλειδί" FROM ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ t JOIN ΠΕΡΙΟΔΙΚΟ p ON t.Κωδικός_Περιοδικού = p.Κωδικός_Περιοδικού LEFT JOIN Περιγράφεται l ON t.Κωδικός_Τεύχους = l.Κωδικός_Τεύχους GROUP BY t.Κωδικός_Τεύχους ORDER BY p.Όνομα, t.Αριθμός_Τεύχους""") #execute function is to perform the SQL operations. Here, it produces all the rows from the table.
        rows = self.cur.fetchall() #fetching all the rows one by one from the table and storing it in list rows
        return rows

    def view_periodiko(self): #To view all the rows present in the table
        self.cur.execute("SELECT p.Κωδικός_Περιοδικού, p.Όνομα, p.Εκδότης, p.Impact_Factor, p.Γλώσσα, p.Συχνότητα_Έκδοσης FROM ΠΕΡΙΟΔΙΚΟ p ORDER BY p.Όνομα, p.Εκδότης") #execute function is to perform the SQL operations. Here, it produces all the rows from the table.
        rows = self.cur.fetchall() #fetching all the rows one by one from the table and storing it in list rows
        return rows
    
    def view_sintakti(self): #To view all the rows present in the table
        self.cur.execute("SELECT s.Κωδικός_Συντάκτη, s.Όνομα, s.Όνομα_Πατέρα, s.Επώνυμο, s.Ιδιότητα FROM ΣΥΝΤΑΚΤΗΣ s ORDER BY s.Επώνυμο, s.Όνομα, s.Όνομα_Πατέρα") #execute function is to perform the SQL operations. Here, it produces all the rows from the table.
        rows = self.cur.fetchall() #fetching all the rows one by one from the table and storing it in list rows
        return rows
    
    def view_idrima(self): #To view all the rows present in the table
        self.cur.execute("SELECT i.Κωδικός_Ιδρύματος, i.Όνομα FROM ΙΔΡΥΜΑ i ORDER BY i.Όνομα") #execute function is to perform the SQL operations. Here, it produces all the rows from the table.
        rows = self.cur.fetchall() #fetching all the rows one by one from the table and storing it in list rows
        return rows

    def search_arthro(self, title="", author="", idruma="", issn="", periodiko="", ar="", ekdotis="", keyw=""):  #to search for a given entry in the table given either the value of the title or author name
        title_qr = ""
        author_qr = ""
        idruma_qr = ""
        issn_qr = ""
        periodiko_qr = ""
        ar_qr = ""
        ekdotis_qr = ""
        keyw_qr = ""
        values = ()
        val = []
        if title != "":
            title_qr = " AND a.Τίτλος = %s "
            val.append(title)
        if author != "":
            author_qr = " AND s2.Επώνυμο = %s "
            val.append(author)
        if idruma != "":
            idruma_qr = " AND i.Όνομα = %s "
            val.append(idruma)
        if issn != "":
            issn_qr = " AND p.Κωδικός_Περιοδικού = %s "
            val.append(issn)
        if periodiko != "":
            periodiko_qr = " AND p.Όνομα = %s "
            val.append(periodiko)
        if ar != "":
            ar_qr = " AND t.Αριθμός_Τεύχους = %s "
            val.append(ar)
        if ekdotis != "":
            ekdotis_qr = " AND p.Εκδότης = %s  "
            val.append(ekdotis)
        if keyw != "":
            keyw_qr = " AND l.Λέξη_κλειδί = %s  "
            val.append(keyw)
        values = tuple(val)
        if len(values)!= 0:
            qr =  """SELECT a.Κωδικός_Άρθρου, a.Τίτλος, p.Κωδικός_Περιοδικού, p.Όνομα, t.Αριθμός_Τεύχους, p.Εκδότης, a.Αρχική_Σελίδα, a.Τελική_Σελίδα, 
                            GROUP_CONCAT(DISTINCT s2.Όνομα, " ", s2.Επώνυμο) AS "Συντάκτης", GROUP_CONCAT(DISTINCT i.Όνομα) AS "Ίδρυμα", GROUP_CONCAT(DISTINCT aa.Κωδικός_Άρθρου_Αναφοράς) AS "Κωδικός_Άρθρου_Αναφοράς",  
                            GROUP_CONCAT(DISTINCT l.Λέξη_κλειδί) AS "Λέξη_κλειδί" FROM ΑΡΘΡΟ a LEFT JOIN Συντάσσει s1 ON a.Κωδικός_Άρθρου = s1.Κωδικός_Άρθρου LEFT JOIN ΣΥΝΤΑΚΤΗΣ s2 ON s1.Κωδικός_Συντάκτη = s2.Κωδικός_Συντάκτη 
                            LEFT JOIN ΙΔΡΥΜΑ i ON s1.Κωδικός_Ιδρύματος = i.Κωδικός_Ιδρύματος LEFT JOIN ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ t ON a.Κωδικός_Τεύχους = t.Κωδικός_Τεύχους 
                            LEFT JOIN ΠΕΡΙΟΔΙΚΟ p ON t.Κωδικός_Περιοδικού = p.Κωδικός_Περιοδικού LEFT JOIN Αναφέρει aa ON a.Κωδικός_Άρθρου=aa.Κωδικός_Άρθρου LEFT JOIN Περιγράφεται l ON a.Κωδικός_Άρθρου = l.Κωδικός_Άρθρου
                            WHERE 1""" + title_qr + author_qr + idruma_qr + issn_qr + periodiko_qr + ar_qr + ekdotis_qr + keyw_qr + "GROUP BY a.Κωδικός_Άρθρου ORDER BY p.Όνομα, t.Αριθμός_Τεύχους, a.Τίτλος"
            self.cur.execute(qr, values)
            rows = self.cur.fetchall()
            return rows
        return []

    def search_teuxos(self, issn="", periodiko="", ar="", thema="", keyw=""):  #to search for a given entry in the table given either the value of the title or author name
        issn_qr = ""
        thema_qr = ""
        periodiko_qr = ""
        ar_qr = ""
        keyw_qr = ""
        values = ()
        val = []
        if issn != "":
            issn_qr = " AND p.Κωδικός_Περιοδικού = %s"
            val.append(issn)
        if periodiko != "":
            periodiko_qr = " AND p.Όνομα = %s "
            val.append(periodiko)
        if ar != "":
            ar_qr = " AND t.Αριθμός_Τεύχους = %s "
            val.append(ar)
        if thema != "":
            thema_qr = " AND t.Θέμα = %s "
            val.append(thema)
        if keyw != "":
            keyw_qr = " AND l.Λέξη_κλειδί = %s "
            val.append(keyw)
        values = tuple(val)
        if len(values)!= 0:
            qr =  """SELECT t.Κωδικός_Τεύχους, p.Κωδικός_Περιοδικού, p.Όνομα, t.Αριθμός_Τεύχους, t.Θέμα, Ημερομηνία_Έκδοσης, GROUP_CONCAT(DISTINCT l.Λέξη_κλειδί) AS "Λέξη_κλειδί" FROM ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ t JOIN ΠΕΡΙΟΔΙΚΟ p ON t.Κωδικός_Περιοδικού = p.Κωδικός_Περιοδικού LEFT JOIN Περιγράφεται l ON t.Κωδικός_Τεύχους = l.Κωδικός_Τεύχους WHERE 1""" + issn_qr + periodiko_qr + ar_qr + thema_qr + keyw_qr + " GROUP BY t.Κωδικός_Τεύχους ORDER BY p.Όνομα, t.Αριθμός_Τεύχους"
            self.cur.execute(qr, values)
            rows = self.cur.fetchall()
            return rows

    def search_periodiko(self, issn="", periodiko="", ekdotis=""):  #to search for a given entry in the table given either the value of the title or author name
        issn_qr = ""
        periodiko_qr = ""
        ekdotis_qr = ""
        values = ()
        val = []
        if issn != "":
            issn_qr = " AND p.Κωδικός_Περιοδικού = %s"
            val.append(issn)
        if periodiko != "":
            periodiko_qr = " AND p.Όνομα = %s"
            val.append(periodiko)
        if ekdotis != "":
            ekdotis_qr = " AND p.Εκδότης = %s"
            val.append(ekdotis)
        values = tuple(val)
        if len(values)!= 0:
            qr =  """SELECT p.Κωδικός_Περιοδικού, p.Όνομα, p.Εκδότης, p.Impact_Factor, p.Γλώσσα, p.Συχνότητα_Έκδοσης FROM ΠΕΡΙΟΔΙΚΟ p WHERE 1""" + issn_qr + periodiko_qr + ekdotis_qr + "ORDER BY p.Όνομα, p.Εκδότης, p.Impact_Factor"
            self.cur.execute(qr, values)
            rows = self.cur.fetchall()
            return rows

    def search_sintakti(self, onoma="", mesaio="", eponimo="", idiotita=""):  #to search for a given entry in the table given either the value of the title or author name
        onoma_qr = ""
        mesaio_qr = ""
        eponimo_qr = ""
        idiotita_qr=""
        values = ()
        val = []
        if onoma != "":
            onoma_qr = " AND s.Κωδικός_Συντάκτη = %s"
            val.append(onoma)
        if mesaio != "":
            mesaio_qr = " AND s.Όνομα_Πατέρα = %s"
            val.append(mesaio)
        if eponimo != "":
            eponimo_qr = " AND s.Επώνυμο = %s"
            val.append(eponimo)
        if idiotita != "":
            idiotita_qr = " AND s.Ιδιότητα = %s"
            val.append(idiotita)
        values = tuple(val)
        if len(values)!= 0:
            qr =  """SELECT s.Κωδικός_Συντάκτη, s.Όνομα, s.Όνομα_Πατέρα, s.Επώνυμο, s.Ιδιότητα FROM ΣΥΝΤΑΚΤΗΣ s WHERE 1""" + onoma_qr + mesaio_qr + eponimo_qr + idiotita_qr + "ORDER BY s.Επώνυμο, s.Όνομα, s.Όνομα_Πατέρα"
            self.cur.execute(qr, values)
            rows = self.cur.fetchall()
            return rows

    def search_idrima(self, idrima=""):  #to search for a given entry in the table given either the value of the title or author name
        idrima_qr = ""
        values = ()
        val = []
        if idrima != "":
            idrima_qr = " AND i.Όνομα = %s"
            val.append(idrima)
        values = tuple(val)
        if len(values)!= 0:
            qr =  "SELECT i.Κωδικός_Ιδρύματος, i.Όνομα FROM ΙΔΡΥΜΑ i WHERE 1 " + idrima_qr + "ORDER BY i.Όνομα"
            self.cur.execute(qr, values)
            rows = self.cur.fetchall()
            return rows

    def add_keyw(self,id_arthrou):
        keyw = keyw_text.get()
        if keyw != "":
            self.qr = "INSERT INTO ΛΕΞΗ_ΚΛΕΙΔΙ (Λέξη_κλειδί) VALUES (%s)"
            self.cur.execute(self.qr, keyw,)
            self.qr1 = "SELECT t.Κωδικός_Τεύχους FROM ΑΡΘΡΟ a LEFT JOIN ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ t ON a.Κωδικός_Τεύχους = t.Κωδικός_Τεύχους WHERE a.Κωδικός_Άρθρου = %s"
            self.cur.execute(self.qr1, (id_arthrou,))
            rows1 = self.cur.fetchall()
            self.qr2 = "INSERT INTO Περιγράφεται (Κωδικός_Άρθρου, Κωδικός_Τεύχους, Λέξη_κλειδί) VALUES (%s,%s,%s)"
            values = (id_arthrou, rows1[0][0], keyw)
            self.cur.execute(self.qr2,values)
            self.con.commit()
            view_command()
    
    def get_ar(self,id,c):
        if c==1:
            self.qr = "SELECT COUNT(DISTINCT a.Κωδικός_Άρθρου) AS Αριθμός_Άρθρων FROM ΑΡΘΡΟ a LEFT JOIN Συντάσσει s ON a.Κωδικός_Άρθρου = s.Κωδικός_Άρθρου WHERE s.Κωδικός_Συντάκτη = %s GROUP BY s.Κωδικός_Συντάκτη"
        elif c==2:
            self.qr = "SELECT COUNT(DISTINCT a.Κωδικός_Άρθρου) AS Αριθμός_Άρθρων FROM ΑΡΘΡΟ a LEFT JOIN Συντάσσει s ON a.Κωδικός_Άρθρου = s.Κωδικός_Άρθρου WHERE s.Κωδικός_Ιδρύματος = %s GROUP BY s.Κωδικός_Ιδρύματος"
        elif c==3: 
            self.qr = "SELECT COUNT(DISTINCT s1.Κωδικός_Συντάκτη) AS Αριθμός_Συντακτών FROM ΙΔΡΥΜΑ i LEFT JOIN Συντάσσει s1 ON i.Κωδικός_Ιδρύματος = s1.Κωδικός_Ιδρύματος WHERE i.Κωδικός_Ιδρύματος = %s GROUP BY s1.Κωδικός_Ιδρύματος"
        elif c==4: 
            self.qr = "SELECT COUNT(DISTINCT aa.Κωδικός_Άρθρου_Αναφοράς) AS Αριθμός_Αναφορών FROM ΑΡΘΡΟ a LEFT JOIN Αναφέρει aa ON a.Κωδικός_Άρθρου = aa.Κωδικός_Άρθρου WHERE a.Κωδικός_Άρθρου = %s GROUP BY aa.Κωδικός_Άρθρου"
        self.cur.execute(self.qr, (id,))
        ar = self.cur.fetchall() 
        self.con.commit()
        return ar

db = DB()  #created an object of the class DB. Now database is connected and a new table book has been formed.

# Remove all records
def	remove_all():
    if n==0:
        for record in tree1.get_children():
            tree1.delete(record)
    elif n==1:
        for record in tree2.get_children():
            tree2.delete(record)
    elif n==2:
        for record in tree3.get_children():
            tree3.delete(record)
    elif n==3:
        for record in tree4.get_children():
            tree4.delete(record)
    elif n==4:
        for record in tree5.get_children():
            tree5.delete(record)

def view_command(): #to print all the rows of the table using view function of the class DB on to the screen
    remove_all()
    if n==0:
        count = 0
        for row in db.view_arthro():
            if count % 2 == 0:
                tree1.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], db.get_ar(row[0],4), row[11]), tags=('evenrow'))
            else:
                tree1.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], db.get_ar(row[0],4), row[11]), tags=('oddrow'))
            count += 1
    elif n==1:
        count = 0
        for row in db.view_teuxos():
            if count % 2 == 0:
                tree2.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]), tags=('evenrow'))
            else:
                tree2.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]), tags=('oddrow'))
            count += 1
    elif n==2:
        count = 0
        for row in db.view_periodiko():
            if count % 2 == 0:
                tree3.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]), tags=('evenrow'))
            else:
                tree3.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]), tags=('oddrow'))
            count += 1
    elif n==3:
        count = 0
        for row in db.view_sintakti():
            if count % 2 == 0:
                tree4.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], db.get_ar(row[0],1)), tags=('evenrow'))
            else:
                tree4.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], db.get_ar(row[0],1)), tags=('oddrow'))
            count += 1
    elif n==4:
        count = 0
        for row in db.view_idrima():
            if count % 2 == 0:
                tree5.insert(parent='', index='end', text='', values=(row[0], row[1], db.get_ar(row[0],2), db.get_ar(row[0],3)), tags=('evenrow'))
            else:
                tree5.insert(parent='', index='end', text='', values=(row[0], row[1], db.get_ar(row[0],2), db.get_ar(row[0],3)), tags=('oddrow'))
            count += 1
					
def search_command(): #to print the row we want based on title or author 
    remove_all()
    if n==0:
        count = 0
        for row in db.search_arthro(title_text.get(), author_text.get(), idruma_text.get(), issn_text.get(), periodiko_text.get(), ar_text.get(), ekdotis_text.get(), keyw_text.get()):
            if count % 2 == 0:
                tree1.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], db.get_ar(row[0],4), row[11]), tags=('evenrow'))
            else:
                tree1.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], db.get_ar(row[0],4), row[11]), tags=('oddrow'))
            count += 1
    elif n==1:
        count = 0
        for row in db.search_teuxos(issn2_text.get(), periodiko2_text.get(), ar2_text.get(), thema_text.get(), keyw2_text.get()):
            if count % 2 == 0:
                tree2.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]), tags=('evenrow'))
            else:
                tree2.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]), tags=('oddrow'))
            count += 1
    elif n==2:
        count = 0
        for row in db.search_periodiko(issn3_text.get(), periodiko3_text.get(), ekdotis3_text.get()):
            if count % 2 == 0:
                tree3.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]), tags=('evenrow'))
            else:
                tree3.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]), tags=('oddrow'))
            count += 1
    elif n==3:
        count = 0
        for row in db.search_sintakti(onomas_text.get(), onomap_text.get(), eponimo_text.get(), idiotita_text.get()):
            if count % 2 == 0:
                tree4.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], db.get_ar(row[0],1)), tags=('evenrow'))
            else:
                tree4.insert(parent='', index='end', text='', values=(row[0], row[1], row[2], row[3], row[4], db.get_ar(row[0],1)), tags=('oddrow'))
        count += 1
    elif n==4:
        count = 0
        for row in db.search_idrima(idrima5_text.get()):
            if count % 2 == 0:
                tree5.insert(parent='', index='end', text='', values=(row[0], row[1], db.get_ar(row[0],2), db.get_ar(row[0],3)), tags=('evenrow'))
            else:
                tree5.insert(parent='', index='end', text='', values=(row[0], row[1], db.get_ar(row[0],2), db.get_ar(row[0],3)), tags=('oddrow'))
        count += 1
        
def clear_search_command():  
    if n==0:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
    elif n==1:
        en1.delete(0, END)
        en2.delete(0, END)
        en3.delete(0, END)
        en4.delete(0, END)
        en5.delete(0, END)
    elif n==2:
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
    elif n==3:
        entr1.delete(0, END)
        entr2.delete(0, END)
        entr3.delete(0, END)
        entr4.delete(0, END)
    elif n==4:
        entry1.delete(0, END)

def add_command():          #to add a new row into the table
	add_arthro.main_add_arthro()
	view_command()

def delete_command(): #deleting a row 
    if n==0:
        db.delete_arthro(s_values[0]) #calls the delete function of the class DB and passes the id as the parameter and condition
        view_command()
    elif n==1:
        db.delete_teuxos(s_values[0]) #calls the delete function of the class DB and passes the id as the parameter and condition
        view_command()
    elif n==2:
        db.delete_periodiko(s_values[0]) #calls the delete function of the class DB and passes the id as the parameter and condition
        view_command()
    elif n==3:
        db.delete_sintakti(s_values[0]) #calls the delete function of the class DB and passes the id as the parameter and condition
        view_command()
    elif n==4:
        db.delete_idrima(s_values[0]) #calls the delete function of the class DB and passes the id as the parameter and condition
        view_command()

def update_command():
    if n==0:
        db.update_arthro(s_values[0]) #calls the update function of the class DB and passes the user input as parameters to update value of the row
    elif n==1:
        db.update_teuxos(s_values[0])
    elif n==2:
        db.update_periodiko(s_values[0])
    elif n==3:
        db.update_sintakti(s_values[0])
    elif n==4:
        db.update_idrima(s_values[0])

# Select Record
def select_record():
    global selected, s_values
    if n==0:
        selected = tree1.focus() # Grab record number
        s_values = tree1.item(selected, 'values') # Grab record values
    elif n==1:
        selected = tree2.focus() # Grab record number
        s_values = tree2.item(selected, 'values') # Grab record values
    elif n==2:
        selected = tree3.focus() # Grab record number
        s_values = tree3.item(selected, 'values') # Grab record values
    elif n==3:
        selected = tree4.focus() # Grab record number
        s_values = tree4.item(selected, 'values') # Grab record values
    elif n==4:
        selected = tree5.focus() # Grab record number
        s_values = tree5.item(selected, 'values') # Grab record values

def add_keyw_command():
    if n==0:
        db.add_keyw(s_values[0])

def tab_change(event):
	global n
	n = tabControl.index('current')
	return n

# Create Binding Click function
def clicker(e):
	select_record()

def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    try:
        l.sort(key=lambda t: float(t[0]), reverse=reverse)
    except ValueError:
        l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))    

def open_selected():
    if n==0:
        webbrowser.open_new(r'C:\\articles\\%s.pdf' % s_values[0])

window = Tk() #using Tkinter module, create a GUI window
window.title("App for Storing & Retrieving scientific journals and their articles using DB") #setting title of the window

window.fullScreenState = False
window.attributes("-fullscreen", window.fullScreenState)
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))

def on_closing(): #destructor for the window
	dd = db
	if messagebox.askokcancel("Quit", "Do you want to quit?"): #when ok is clicked, displays the following message
		window.destroy()
		del dd #deletes the object once window has been closed

window.protocol("WM_DELETE_WINDOW", on_closing)  # handles window closing

#tab commands
s1 = Style()
myblack = "#000000"
mywhite = "#fff"

s1.theme_create("mine", parent="clam", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": mywhite, "font": 'Helvetica 9 bold'},
            "map":       {"background": [("selected", myblack)],
                          "foreground": [("selected", mywhite)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )
s1.theme_use("clam")
tabControl = Notebook(window)
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)
tab5 = Frame(tabControl)
tabControl.add(tab1, text='Άρθρα')
tabControl.add(tab2, text='Τεύχη')
tabControl.add(tab3, text='Περιοδικά')
tabControl.add(tab4, text='Συντάκτες')
tabControl.add(tab5, text='Ιδρύματα')
tabControl.grid(column=0, row=0, columnspan=6, rowspan=32)
Label(tab1).grid(column=0, row=0, padx=30, pady=10)
Label(tab2).grid(column=0, row=0, padx=30, pady=10)
Label(tab3).grid(column=0, row=0, padx=30, pady=10)
Label(tab4).grid(column=0, row=0, padx=30, pady=10)
Label(tab5).grid(column=0, row=0, padx=30, pady=10)
tabControl.enable_traversal()

s = Style()
s.configure("Treeview.Heading", background="lightgreen", foreground='red', rowheight=25, fieldbackground="black", font=('Helvetica', 9, "bold"))
#s.configure("Treeview.Heading",background='#7d8ea3', foreground='#ffffff', font=("Century Gothic", 10, 'bold'))
s.map('Treeview', background=[('selected', 'blue')])

#treeview for tab1
hsb1 = Scrollbar(tab1, orient="horizontal")
hsb1.grid(row=3, columnspan=8, column=0, sticky="ew")
vsb1 = Scrollbar(tab1, orient="vertical")
vsb1.grid(row=4, column=8, rowspan=27, sticky="ns")

tree1 = Treeview(tab1, height=27, yscrollcommand=vsb1.set, xscrollcommand=hsb1.set, selectmode="extended")
tree1['show'] = 'headings'
tree1.grid(row=4, column=0,  rowspan=27, columnspan=8, sticky='ns') #determining the size

hsb1.config(command=tree1.xview)
vsb1.config(command=tree1.yview)

tree1["columns"] = ("ID_Άρθρου", "Τίτλος", "ISSN", "Περιοδικό", "Αρ_Τεύχους", "Εκδότης", "Αρ_Σελίδα", "Τελ_Σελίδα", "Συντάκτης", "Ίδρυμα", "ID_Άρθρου_Αναφοράς", "Αρ_Αναφορών", "Λέξεις_Κλειδιά")
tree1.column("ID_Άρθρου", width=70, minwidth=70, anchor=CENTER)
tree1.column("Τίτλος", width=100, minwidth=100, anchor=CENTER)
tree1.column("ISSN", width=70, minwidth=70, anchor=CENTER)
tree1.column("Περιοδικό", width=140, minwidth=140, anchor=CENTER)
tree1.column("Αρ_Τεύχους", width=80, minwidth=80, anchor=CENTER)
tree1.column("Εκδότης", width=80, minwidth=80, anchor=CENTER)
tree1.column("Αρ_Σελίδα", width=70, minwidth=70, anchor=CENTER)
tree1.column("Τελ_Σελίδα", width=75, minwidth=75, anchor=CENTER)
tree1.column("Συντάκτης", width=100, minwidth=100, anchor=CENTER)
tree1.column("Ίδρυμα", width=120, minwidth=100, anchor=CENTER)
tree1.column("ID_Άρθρου_Αναφοράς", width=135, minwidth=100, anchor=CENTER)
tree1.column("Αρ_Αναφορών", width=100, minwidth=80, anchor=CENTER)
tree1.column("Λέξεις_Κλειδιά", width=95, minwidth=80, anchor=CENTER)

tree1.heading("ID_Άρθρου", text="ID_Άρθρου", anchor=CENTER)
tree1.heading("Τίτλος", text="Τίτλος", anchor=CENTER)
tree1.heading("ISSN", text="ISSN", anchor=CENTER)
tree1.heading("Περιοδικό", text="Περιοδικό", anchor=CENTER)
tree1.heading("Αρ_Τεύχους", text="Αρ_Τεύχους", anchor=CENTER)
tree1.heading("Εκδότης", text="Εκδότης", anchor=CENTER)
tree1.heading("Αρ_Σελίδα", text="Αρ_Σελίδα", anchor=CENTER)
tree1.heading("Τελ_Σελίδα", text="Τελ_Σελίδα", anchor=CENTER)
tree1.heading("Συντάκτης", text="Συντάκτης", anchor=CENTER)
tree1.heading("Ίδρυμα", text="Ίδρυμα", anchor=CENTER)
tree1.heading("ID_Άρθρου_Αναφοράς", text="ID_Άρθρου_Αναφοράς", anchor=CENTER)
tree1.heading("Αρ_Αναφορών", text="ID_Άρθρου_Αναφοράς", anchor=CENTER)
tree1.heading("Λέξεις_Κλειδιά", text="Λέξεις_Κλειδιά", anchor=CENTER)

tree1.bind("<ButtonRelease-1>", clicker)

# Create striped row tags
tree1.tag_configure('oddrow', background="white")
tree1.tag_configure('evenrow', background="lightblue")

#treeview for tab2
hsb2 = Scrollbar(tab2, orient="horizontal")
hsb2.grid(row=3, columnspan=6, column=0, sticky="ew")
vsb2 = Scrollbar(tab2, orient="vertical")
vsb2.grid(row=4, column=6, rowspan=28, sticky="ns")

tree2 = Treeview(tab2, height=27, yscrollcommand=vsb2.set, xscrollcommand=hsb2.set, selectmode="extended")
tree2['show'] = 'headings'
tree2.grid(row=4, column=0, rowspan=27, columnspan=6, sticky='ns') #determining the size

hsb2.config(command=tree2.xview)
vsb2.config(command=tree2.yview)

tree2["columns"] = ("ID_Τεύχους", "ISSN", "Περιοδικό", "Αρ_Τεύχους", "Θέμα", "Ημερομηνία Έκδοσης", "Λέξεις_Κλειδιά")
tree2.column("ID_Τεύχους", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree2.column("ISSN", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree2.column("Περιοδικό", width=160, minwidth=160, stretch=True, anchor=CENTER)
tree2.column("Αρ_Τεύχους", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree2.column("Θέμα", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree2.column("Ημερομηνία Έκδοσης", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree2.column("Λέξεις_Κλειδιά", width=110, minwidth=100, anchor=CENTER)

tree2.heading("ID_Τεύχους", text="ID_Τεύχους", anchor=CENTER)
tree2.heading("ISSN", text="ISSN", anchor=CENTER)
tree2.heading("Περιοδικό", text="Περιοδικό", anchor=CENTER)
tree2.heading("Αρ_Τεύχους", text="Αρ_Τεύχους", anchor=CENTER)
tree2.heading("Θέμα", text="Θέμα", anchor=CENTER)
tree2.heading("Ημερομηνία Έκδοσης", text="Ημερομηνία Έκδοσης", anchor=CENTER)
tree2.heading("Λέξεις_Κλειδιά", text="Λέξεις_Κλειδιά", anchor=CENTER)

tree2.bind("<ButtonRelease-1>", clicker)

# Create striped row tags
tree2.tag_configure('oddrow', background="white")
tree2.tag_configure('evenrow', background="lightblue")

#treeview for tab3
hsb3 = Scrollbar(tab3, orient="horizontal")
hsb3.grid(row=2, columnspan=6, column=0, sticky="ew")
vsb3 = Scrollbar(tab3, orient="vertical")
vsb3.grid(row=3, column=7, rowspan=28, sticky="ns")

tree3 = Treeview(tab3, height=28, yscrollcommand=vsb3.set, xscrollcommand=hsb3.set, selectmode="extended")
tree3['show'] = 'headings'
tree3.grid(row=3, column=0, rowspan=28, columnspan=6, sticky='ns') #determining the size

hsb3.config(command=tree3.xview)
vsb3.config(command=tree3.yview)

tree3["columns"] = ("ISSN", "Περιοδικό", "Εκδότης", "Impact_Factor", "Γλώσσα", "Συχνότητα_Έκδοσης")
tree3.column("ISSN", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree3.column("Περιοδικό", width=160, minwidth=160, stretch=True, anchor=CENTER)
tree3.column("Εκδότης", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree3.column("Impact_Factor", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree3.column("Γλώσσα", width=150, minwidth=150, stretch=True, anchor=CENTER)
tree3.column("Συχνότητα_Έκδοσης", width=150, minwidth=150, stretch=True, anchor=CENTER)

tree3.heading("ISSN", text="ID_Περιοδικού", anchor=CENTER)
tree3.heading("Περιοδικό", text="Περιοδικό", anchor=CENTER)
tree3.heading("Εκδότης", text="Εκδότης", anchor=CENTER)
tree3.heading("Impact_Factor", text="Impact_Factor", anchor=CENTER)
tree3.heading("Γλώσσα", text="Γλώσσα", anchor=CENTER)
tree3.heading("Συχνότητα_Έκδοσης", text="Συχνότητα_Έκδοσης", anchor=CENTER)

tree3.bind("<ButtonRelease-1>", clicker)

# Create striped row tags
tree3.tag_configure('oddrow', background="white")
tree3.tag_configure('evenrow', background="lightblue")

#treeview for tab4
hsb4 = Scrollbar(tab4, orient="horizontal")
hsb4.grid(row=3, columnspan=8, column=0, sticky="ew")
vsb4 = Scrollbar(tab4, orient="vertical")
vsb4.grid(row=4, column=8, rowspan=27, sticky="ns")

tree4 = Treeview(tab4, height=27, yscrollcommand=vsb4.set, xscrollcommand=hsb4.set, selectmode="extended")
tree4['show'] = 'headings'
tree4.grid(row=4, column=0,  rowspan=27, columnspan=8, sticky='ns') #determining the size

hsb4.config(command=tree4.xview)
vsb4.config(command=tree4.yview)

tree4["columns"] = ("ID_Συντάκτη", "Όνομα", "Ον.Πατέρα", "Επώνυμο", "Ιδιότητα", "Αρ_Άρθρων")
tree4.column("ID_Συντάκτη", width=80, minwidth=80, anchor=CENTER)
tree4.column("Όνομα", width=150, minwidth=100, anchor=CENTER)
tree4.column("Ον.Πατέρα", width=150, minwidth=100, anchor=CENTER)
tree4.column("Επώνυμο", width=150, minwidth=100, anchor=CENTER)
tree4.column("Ιδιότητα", width=150, minwidth=100, anchor=CENTER)
tree4.column("Αρ_Άρθρων", width=80, minwidth=80, anchor=CENTER)

tree4.heading("ID_Συντάκτη", text="ID_Συντάκτη", anchor=CENTER)
tree4.heading("Όνομα", text="Όνομα", anchor=CENTER)
tree4.heading("Ον.Πατέρα", text="Ον.Πατέρα", anchor=CENTER)
tree4.heading("Επώνυμο", text="Επώνυμο", anchor=CENTER)
tree4.heading("Ιδιότητα", text="Ιδιότητα", anchor=CENTER)
tree4.heading("Αρ_Άρθρων", text="Αρ_Άρθρων", anchor=CENTER)

tree4.bind("<ButtonRelease-1>", clicker)

# Create striped row tags
tree4.tag_configure('oddrow', background="white")
tree4.tag_configure('evenrow', background="lightblue")

#treeview for tab5
hsb5 = Scrollbar(tab5, orient="horizontal")
hsb5.grid(row=3, columnspan=8, column=0, sticky="ew")
vsb5 = Scrollbar(tab5, orient="vertical")
vsb5.grid(row=4, column=8, rowspan=27, sticky="ns")

tree5 = Treeview(tab5, height=27, yscrollcommand=vsb5.set, xscrollcommand=hsb5.set, selectmode="extended")
tree5['show'] = 'headings'
tree5.grid(row=4, column=0,  rowspan=27, columnspan=8, sticky='ns') #determining the size

hsb5.config(command=tree5.xview)
vsb5.config(command=tree5.yview)

tree5["columns"] = ("ID_Ιδρύματος", "Όνομα", "Αρ_Άρθρων", "Αρ_Συντακτών")
tree5.column("ID_Ιδρύματος", width=150, minwidth=150, anchor=CENTER)
tree5.column("Όνομα", width=250, minwidth=250, anchor=CENTER)
tree5.column("Αρ_Άρθρων", width=150, minwidth=150, anchor=CENTER)
tree5.column("Αρ_Συντακτών", width=300, minwidth=300, anchor=CENTER)

tree5.heading("ID_Ιδρύματος", text="ID_Ιδρύματος", anchor=CENTER)
tree5.heading("Όνομα", text="Όνομα", anchor=CENTER)
tree5.heading("Αρ_Άρθρων", text="Αρ_Άρθρων", anchor=CENTER)
tree5.heading("Αρ_Συντακτών", text="Αρ_Συντακτών", anchor=CENTER)

tree5.bind("<ButtonRelease-1>", clicker)

# Create striped row tags
tree5.tag_configure('oddrow', background="white")
tree5.tag_configure('evenrow', background="lightblue")

for col in tree1["columns"]:
    tree1.heading(col, text=col ,command=lambda _col=col: treeview_sort_column(tree1, _col, True))

for col in tree2["columns"]:
    tree2.heading(col, text=col ,command=lambda _col=col: treeview_sort_column(tree2, _col, True))

for col in tree3["columns"]:
    tree3.heading(col, text=col ,command=lambda _col=col: treeview_sort_column(tree3, _col, True))

for col in tree4["columns"]:
    tree4.heading(col, text=col ,command=lambda _col=col: treeview_sort_column(tree4, _col, True))

for col in tree5["columns"]:
    tree5.heading(col, text=col ,command=lambda _col=col: treeview_sort_column(tree5, _col, True))

n=0
tabControl.bind('<ButtonRelease-1>', tab_change)

title_text = StringVar() #taking arthro tile name input
e1 = Entry(tab1, textvariable=title_text) #taking input from the user in the grid and storing it in a string variable
e1.grid(row=0, column=1)

author_text = StringVar() #taking author last name input
e2 = Entry(tab1, textvariable=author_text)
e2.grid(row=0, column=3)

idruma_text = StringVar() #taking onoma idrumatos input
e3 = Entry(tab1, textvariable=idruma_text)
e3.grid(row=0, column=5)

issn_text = StringVar() #taking issn input
e4 = Entry(tab1, textvariable=issn_text) 
e4.grid(row=1, column=1)

periodiko_text = StringVar() #taking periodiko title input
e5 = Entry(tab1, textvariable=periodiko_text)
e5.grid(row=1, column=3)

ar_text = StringVar() #taking arithmo teuxous input
e6 = Entry(tab1, textvariable=ar_text)
e6.grid(row=1, column=5)

ekdotis_text = StringVar() #taking onoma ekdoti input
e7 = Entry(tab1, textvariable=ekdotis_text)
e7.grid(row=0, column=7)

keyw_text = StringVar() #taking onoma ekdoti input
e8 = Entry(tab1, textvariable=keyw_text)
e8.grid(row=1, column=7)

l1 = Label(tab1, text="Τίτλος") #creating input labels in the window
l1.grid(row=0, column=0) #determining size of the input grid for these labels

l2 = Label(tab1, text="Επώνυμο Συντάκτη")
l2.grid(row=0, column=2)

l3 = Label(tab1, text="Ίδρυμα")
l3.grid(row=0, column=4)

l4 = Label(tab1, text="ISSN")
l4.grid(row=1, column=0)

l5 = Label(tab1, text="Περιοδικό")
l5.grid(row=1, column=2)

l6 = Label(tab1, text="Αρ_Τεύχους")
l6.grid(row=1, column=4)

l7 = Label(tab1, text="Εκδότης")
l7.grid(row=0, column=6)

l8 = Label(tab1, text="Λέξη-Κλειδί")
l8.grid(row=1, column=6)

issn2_text = StringVar() #taking arthro tile name input
en1 = Entry(tab2, textvariable=issn2_text) #taking input from the user in the grid and storing it in a string variable
en1.grid(row=0, column=1)

periodiko2_text = StringVar() #taking author last name input
en2 = Entry(tab2, textvariable=periodiko2_text)
en2.grid(row=0, column=3)

ar2_text = StringVar() #taking onoma idrumatos input
en3 = Entry(tab2, textvariable=ar2_text)
en3.grid(row=1, column=1)

thema_text = StringVar() #taking periodiko title input
en4 = Entry(tab2, textvariable=thema_text)
en4.grid(row=1, column=3)

keyw2_text = StringVar() #taking onoma ekdoti input
en5 = Entry(tab2, textvariable=keyw2_text)
en5.grid(row=0, column=5)

la1 = Label(tab2, text="ISSN") #creating input labels in the window
la1.grid(row=0, column=0) #determining size of the input grid for these labels

la2 = Label(tab2, text="Περιοδικό")
la2.grid(row=0, column=2)

la3 = Label(tab2, text="Αρ_Τεύχους")
la3.grid(row=1, column=0)

la4 = Label(tab2, text="Θέμα")
la4.grid(row=1, column=2)

la5 = Label(tab2, text="Λέξη_Κλειδί")
la5.grid(row=0, column=4)

issn3_text = StringVar() #taking arthro tile name input
ent1 = Entry(tab3, textvariable=issn3_text) #taking input from the user in the grid and storing it in a string variable
ent1.grid(row=0, column=1)

periodiko3_text = StringVar() #taking arthro tile name input
ent2 = Entry(tab3, textvariable=periodiko3_text) #taking input from the user in the grid and storing it in a string variable
ent2.grid(row=0, column=3)

ekdotis3_text = StringVar() #taking author last name input
ent3 = Entry(tab3, textvariable=ekdotis3_text)
ent3.grid(row=0, column=5)

lab1 = Label(tab3, text="ISSN") #creating input labels in the window
lab1.grid(row=0, column=0) #determining size of the input grid for these labels

lab2 = Label(tab3, text="Περιοδικό") #creating input labels in the window
lab2.grid(row=0, column=2) #determining size of the input grid for these labels

lab3 = Label(tab3, text="Εκδότης")
lab3.grid(row=0, column=4)

onomas_text = StringVar() #taking arthro tile name input
entr1 = Entry(tab4, textvariable=onomas_text) #taking input from the user in the grid and storing it in a string variable
entr1.grid(row=0, column=1)

onomap_text = StringVar() #taking arthro tile name input
entr2 = Entry(tab4, textvariable=onomap_text) #taking input fronomap_textm the user in the grid and storing it in a string variable
entr2.grid(row=0, column=3)

eponimo_text = StringVar() #taking author last name input
entr3 = Entry(tab4, textvariable=eponimo_text)
entr3.grid(row=1, column=1)

idiotita_text = StringVar() #taking arthro tile name input
entr4 = Entry(tab4, textvariable=idiotita_text) #taking input fronomap_textm the user in the grid and storing it in a string variable
entr4.grid(row=1, column=3)

labe1 = Label(tab4, text="Όνομα") #creating input labels in the window
labe1.grid(row=0, column=0) #determining size of the input grid for these labels

labe2 = Label(tab4, text="Μεσαίο") #creating input labels in the window
labe2.grid(row=0, column=2) #determining size of the input grid for these labels

labe3 = Label(tab4, text="Επώνυμο")
labe3.grid(row=1, column=0)

labe3 = Label(tab4, text="Ιδιότητα")
labe3.grid(row=1, column=2)

idrima5_text = StringVar() #taking arthro tile name input
entry1 = Entry(tab5, width=30, textvariable=idrima5_text) #taking input from the user in the grid and storing it in a string variable
entry1.grid(row=0, column=1)

label1 = Label(tab5, text="Ίδρυμα") #creating input labels in the window
label1.grid(row=0, column=0) #determining size of the input grid for these labels

l7 = Label(tab1, text="Αποτελέσματα αναζήτησης", font=('Helvetica',11,'bold','underline'))
l7.grid(row=2, column=3, columnspan=2, sticky='w')

la7 = Label(tab2, text="Αποτελέσματα αναζήτησης", font=('Helvetica',11,'bold','underline'))
la7.grid(row=2, column=2, columnspan=2, sticky='w')

lab7 = Label(tab3, text="Αποτελέσματα αναζήτησης", font=('Helvetica',11,'bold','underline'))
lab7.grid(row=1, column=2, columnspan=2, sticky='w')

labe7 = Label(tab4, text="Αποτελέσματα αναζήτησης", font=('Helvetica',11,'bold','underline'))
labe7.grid(row=2, column=1, columnspan=2, sticky='w')

label7 = Label(tab5, text="Αποτελέσματα αναζήτησης", font=('Helvetica',11,'bold','underline'))
label7.grid(row=1, column=1, columnspan=2, sticky='w')

b1_1 = Button(window, text="Search entry", width=14, command=search_command) #creating buttons for the various operations. Giving it a name and assigning a particular command to it. 
b1_1.grid(row=3, column=9) #size of the button

b1_2 = Button(window, text="Clear entry", width=14, command=clear_search_command) #creating buttons for the various operations. Giving it a name and assigning a particular command to it. 
b1_2.grid(row=2, column=9) #size of the button

b2 = Button(window, text="View all", width=14, command=view_command) 
b2.grid(row=5, column=9) 

b3 = Button(window, text="Add άρθρο", width=14, command=add_command)
b3.grid(row=6, column=9)

longtext = """Open selected
        άρθρο"""
b3 = Button(window, width=14,  text=longtext, command=open_selected)
b3.grid(row=7, rowspan=4, column=9)

b4 = Button(window, text="Update selected", width=14, command=update_command)
b4.grid(row=11, column=9)

b5 = Button(window, text="Delete selected", width=14, command=delete_command)
b5.grid(row=12, column=9)

b6 = Button(window, text="Add keyword", width=14, command=add_keyw_command)
b6.grid(row=13, column=9)

# b7 = Button(window, text="Statistics", width=14, command=statistics.main_statistics)
# b7.grid(row=14, column=9)


b9 = Button(window, text="Close", width=14, command=window.destroy)
b9.grid(row=15, column=9)

#--------------------------------------------------------------------------------------------
# Enable cut, copy, paste on entry box using shortcut keys
def make_textmenu(root):
	global the_menu
	the_menu = Menu(root, tearoff=0)
	the_menu.add_command(label="Cut")
	the_menu.add_command(label="Copy")
	the_menu.add_command(label="Paste")
	the_menu.add_separator()
	the_menu.add_command(label="Select all")

def callback_select_all(event):
	# select text after 50ms
	window.after(50, lambda:event.widget.select_range(0, 'end'))

def show_textmenu(event):
	e_widget = event.widget
	the_menu.entryconfigure("Cut",command=lambda: e_widget.event_generate("<<Cut>>"))
	the_menu.entryconfigure("Copy",command=lambda: e_widget.event_generate("<<Copy>>"))
	the_menu.entryconfigure("Paste",command=lambda: e_widget.event_generate("<<Paste>>"))
	the_menu.entryconfigure("Select all",command=lambda: e_widget.select_range(0, 'end'))
	the_menu.tk.call("tk_popup", the_menu, event.x_root, event.y_root)

make_textmenu(window)

# Bind the feature to all Entry widget
window.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_textmenu)
window.bind_class("Entry", "<Control-a>", callback_select_all)

#--------------------------------------------------------------------------------------------
window.mainloop() #carry the functioning of the GUI window on a loop until it is closed using the destructor