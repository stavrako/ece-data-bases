import pymysql
from tkinter import *
from tkinter.ttk import *
import textwrap

def main_statistics():
    root = Tk()
    root.title('Statistics')
    root.geometry("730x450")
    wrapper = textwrap.TextWrapper(width=50)

    con = pymysql.connect(host = '150.140.186.221',
                                            port = 3306, 
                                            user='db20_up1059338',
                                            passwd='up1059338', 
                                            database='project_db20_up1059338')              
    cur = con.cursor()

    def com16():
        list1.delete(0,END)
        if e1.get().isdigit()!=0:
            cur.execute("""SELECT `Όνομα`, YEAR(`Ημερομηνία_Έκδοσης`), COUNT(`Τίτλος`) 
                            FROM `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` JOIN `ΠΕΡΙΟΔΙΚΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Περιοδικού`=`ΠΕΡΙΟΔΙΚΟ`.`Κωδικός_Περιοδικού` 
                            JOIN `ΑΡΘΡΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`=`ΑΡΘΡΟ`.`Κωδικός_Τεύχους` 
                            WHERE `impact_factor` >= %s
                            GROUP BY YEAR(`Ημερομηνία_Έκδοσης`), `Όνομα` """, e1.get())

            r = cur.fetchall()
            for row in r:
                list1.insert(END, row)
            return
        
    def com17():
        list1.delete(0,END)
        if (e2_1.get().isdigit()!=0 and e2_2.get().isdigit()!=0):
            cur.execute("""SELECT `Συντάσσει`.`Κωδικός_Συντάκτη`, `Όνομα`, `Επώνυμο`, COUNT(`Συντάσσει`.`Κωδικός_Άρθρου`) AS `Αριθμός_Άρθρων` 
                            FROM `ΣΥΝΤΑΚΤΗΣ` JOIN `Συντάσσει` ON `ΣΥΝΤΑΚΤΗΣ`.`Κωδικός_Συντάκτη`=`Συντάσσει`.`Κωδικός_Συντάκτη` 
                            JOIN `ΑΡΘΡΟ` ON `Συντάσσει`.`Κωδικός_Άρθρου`=`ΑΡΘΡΟ`.`Κωδικός_Άρθρου` 
                            JOIN `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` ON `ΑΡΘΡΟ`.`Κωδικός_Τεύχους`=`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους` 
                            WHERE  (YEAR(CURDATE()) - YEAR(`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`)) <= %s
                            GROUP BY `Συντάσσει`.`Κωδικός_Συντάκτη`, `Όνομα`, `Επώνυμο` 
                            HAVING `Αριθμός_Άρθρων` >= %s""",(e2_2.get(),e2_1.get()))

            r = cur.fetchall()
        
            for row in r:
                list1.insert(END, row)
            return

    def com18():
        list1.delete(0,END)
        if (e3_1.get().isdigit()!=0 and e3_2.get().isdigit()!=0):
            cur.execute("""SELECT `ΠΕΡΙΟΔΙΚΟ`.`Όνομα`, `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Αριθμός_Τεύχους`, ROUND(AVG(`ΑΡΘΡΟ`.`Τελική_Σελίδα`-`ΑΡΘΡΟ`.`Αρχική_Σελίδα`)) AS `Μέσος Όρος Σελίδων` 
                            FROM `ΑΡΘΡΟ` JOIN `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` ON `ΑΡΘΡΟ`.`Κωδικός_Τεύχους`=`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους` 
                            JOIN `ΠΕΡΙΟΔΙΚΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Περιοδικού`=`ΠΕΡΙΟΔΙΚΟ`.`Κωδικός_Περιοδικού` 
                            WHERE YEAR(`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`) >= %s AND YEAR(`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`) <= %s
                            GROUP BY `ΠΕΡΙΟΔΙΚΟ`.`Όνομα`, `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Αριθμός_Τεύχους`""",(e3_1.get(),e3_2.get()))
            r = cur.fetchall()
        
            for row in r:
                list1.insert(END, row)
            return

    def com19():
        list1.delete(0,END)
        id = e4.get()
        if id.isdigit()!=0:
            cur.execute("""SELECT `ΣΥΝΤΑΚΤΗΣ`.`Όνομα`,`Επώνυμο`, `ΙΔΡΥΜΑ`.`Όνομα` AS `Ίδρυμα` 
                            FROM `Συντάσσει` JOIN `ΣΥΝΤΑΚΤΗΣ` ON `Συντάσσει`.`Κωδικός_Συντάκτη`=`ΣΥΝΤΑΚΤΗΣ`.`Κωδικός_Συντάκτη` 
                            JOIN `ΙΔΡΥΜΑ` ON `Συντάσσει`.`Κωδικός_Ιδρύματος`=`ΙΔΡΥΜΑ`.`Κωδικός_Ιδρύματος` 
                            JOIN `ΑΡΘΡΟ` ON `Συντάσσει`.`Κωδικός_Άρθρου`=`ΑΡΘΡΟ`.`Κωδικός_Άρθρου` 
                            JOIN `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` ON `ΑΡΘΡΟ`.`Κωδικός_Τεύχους`=`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`
                            WHERE `ΣΥΝΤΑΚΤΗΣ`.`Κωδικός_Συντάκτη` <> %s 
                            AND `Συντάσσει`.`Κωδικός_Ιδρύματος` NOT IN (SELECT `Συντάσσει`.`Κωδικός_Ιδρύματος` 
                                                                        FROM `Συντάσσει` JOIN `ΑΡΘΡΟ` ON `Συντάσσει`.`Κωδικός_Άρθρου`=`ΑΡΘΡΟ`.`Κωδικός_Άρθρου`
                                                                        JOIN `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` ON `ΑΡΘΡΟ`.`Κωδικός_Τεύχους`=`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`
                                                                        WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`=%s AND `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`=ANY (SELECT MAX(`Ημερομηνία_Έκδοσης`) 
                                                                                                                                                                FROM `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` JOIN `ΑΡΘΡΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`=`ΑΡΘΡΟ`.`Κωδικός_Τεύχους` 
                                                                                                                                                                JOIN `Συντάσσει` ON `ΑΡΘΡΟ`.`Κωδικός_Άρθρου`=`Συντάσσει`.`Κωδικός_Άρθρου` 
                                                                                                                                                                WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`=%s))
                            AND `Συντάσσει`.`Κωδικός_Άρθρου` IN (SELECT `Συντάσσει`.`Κωδικός_Άρθρου`FROM `Συντάσσει` WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`=%s) 
                            AND `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης` >= ANY (SELECT MIN(`Ημερομηνία_Έκδοσης`) 
                                                                                FROM `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` JOIN `ΑΡΘΡΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`=`ΑΡΘΡΟ`.`Κωδικός_Τεύχους` 
                                                                                JOIN `Συντάσσει` ON `ΑΡΘΡΟ`.`Κωδικός_Άρθρου`=`Συντάσσει`.`Κωδικός_Άρθρου` 
                                                                                WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`=%s)""",(id,id,id,id,id))
            r = cur.fetchall()
        
            for row in r:
                list1.insert(END, row)
            return

    #--------------------------------------------------------------------------------------------
    list1 = Listbox(root, height=25, width=65) #creating the list space to display all the rows of the table
    list1.grid(row=0, column=0, rowspan=18, columnspan=2) #determining the size

    vsb1 = Scrollbar(root, orient="vertical")
    vsb1.grid(row=0, column=2, rowspan=25, sticky="ns")

    list1.configure(yscrollcommand=vsb1.set) #configuring the scroll function for the scrollbar object sb1
    vsb1.configure(command=list1.yview)

    #--------------------------------------------------------------------------------------------
    # Create entry box
    e1 = Entry(root) 
    e1.grid(row=1, column=3, columnspan=2)
 
    e2_1 = Entry(root) 
    e2_1.grid(row=4, column=3)

    e2_2 = Entry(root)
    e2_2.grid(row=4, column=4)

    e3_1 = Entry(root) 
    e3_1.grid(row=7, column=3)

    e3_2 = Entry(root) 
    e3_2.grid(row=7, column=4)
 
    e4 = Entry(root) 
    e4.grid(row=10, column=3, columnspan=2)

    #--------------------------------------------------------------------------------------------
    # Create label and text box
    wr1 = wrapper.fill(text="Αριθμός άρθρων ανά έτος, από περιοδικά με impact factor μεγαλύτερο του (entry_box)")
    label1 = Label(root, text=wr1, width=50)
    label1.grid(row=0, column=3, columnspan=2)

    wr2 = wrapper.fill(text="Εμφάνισε τους συντάκτες οι οποίοι έχουν εκδώσει πάνω από (entry_box_left) άρθρα από διάφορα ιδρύματα, τα τελευταία (entry_box_right) χρόνια")
    label2 = Label(root, text=wr2, width=50)
    label2.grid(row=3, column=3, columnspan=2)

    wr3 = wrapper.fill(text="Εμφάνισε τον μέσο όρο σελίδων των άρθρων, για κάθε τεύχος που εκδόθηκε στο διάστημα (entry_box_left - ex. [2015]) έως (entry_box_right - ex. [2019])")
    label3 = Label(root, text=wr3, width=50)
    label3.grid(row=6, column=3, columnspan=2)

    wr4 = wrapper.fill(text="Με ποιους συντάκτες από διαφορετικά ιδρύματα έχει συνεργαστεί κάποιος (entry_box_left - ID_Συντάκτη) όσο καιρό είναι στο ίδρυμα που βρίσκεται τώρα")
    label4 = Label(root, text=wr4, width=50)
    label4.grid(row=9, column=3, columnspan=2)

    #--------------------------------------------------------------------------------------------
    # Create button
    b1 = Button(root, text="Search", width=10,command= com16) 
    b1.grid(row=2, column=3, columnspan=2)

    b2 = Button(root, text="Search", width=10, command= com17)
    b2.grid(row=5, column=3, columnspan=2)

    b3 = Button(root, text="Search", width=10, command= com18)
    b3.grid(row=8, column=3, columnspan=2)

    b4 = Button(root, text="Search", width=10, command= com19)
    b4.grid(row=11, column=3, columnspan=2)

    b5 = Button(root, text="Close", width=10, command=root.destroy)
    b5.grid(row=14, column=3, columnspan=2)

    #--------------------------------------------------------------------------------------------
    root.mainloop() 

    cur.close()
    con.close()