import pymysql
from tkinter import *
from tkinter.ttk import *
import textwrap

def main_statistics():
    def com16():
        list1.delete(0,END)
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()

        cur.execute("""SELECT `Όνομα`, YEAR(`Ημερομηνία_Έκδοσης`), COUNT(`Τίτλος`) 
                        FROM `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` JOIN `ΠΕΡΙΟΔΙΚΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Περιοδικού`=`ΠΕΡΙΟΔΙΚΟ`.`Κωδικός_Περιοδικού` 
                        JOIN `ΑΡΘΡΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`=`ΑΡΘΡΟ`.`Κωδικός_Τεύχους` 
                        WHERE `impact_factor` >= 1.5 
                        GROUP BY `Όνομα`, YEAR(`Ημερομηνία_Έκδοσης`)""")
        r = cur.fetchall()
        
        for row in r:
            list1.insert(END, row)
        cur.close()
        con.close()
        return

    def com17():
        list1.delete(0,END)
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        cur.execute("""SELECT `Συντάσσει`.`Κωδικός_Συντάκτη`, `Όνομα`, `Επώνυμο`, COUNT(`Συντάσσει`.`Κωδικός_Άρθρου`) AS `Αριθμός_Άρθρων` 
                        FROM `ΣΥΝΤΑΚΤΗΣ` JOIN `Συντάσσει` ON `ΣΥΝΤΑΚΤΗΣ`.`Κωδικός_Συντάκτη`=`Συντάσσει`.`Κωδικός_Συντάκτη` 
                        JOIN `ΑΡΘΡΟ` ON `Συντάσσει`.`Κωδικός_Άρθρου`=`ΑΡΘΡΟ`.`Κωδικός_Άρθρου` 
                        JOIN `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` ON `ΑΡΘΡΟ`.`Κωδικός_Τεύχους`=`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους` 
                        WHERE DATEDIFF(`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`,CURDATE()) 
                        GROUP BY `Συντάσσει`.`Κωδικός_Συντάκτη`, `Όνομα`, `Επώνυμο` 
                        HAVING `Αριθμός_Άρθρων` >= 2""")
        r = cur.fetchall()
        
        for row in r:
            list1.insert(END, row)
        cur.close()
        con.close()
        return

    def com18():
        list1.delete(0,END)
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()

        cur.execute("""SELECT `ΠΕΡΙΟΔΙΚΟ`.`Όνομα`, `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Αριθμός_Τεύχους`, ROUND(AVG(`ΑΡΘΡΟ`.`Τελική_Σελίδα`-`ΑΡΘΡΟ`.`Αρχική_Σελίδα`)) AS `Μέσος Όρος Σελίδων` 
                        FROM `ΑΡΘΡΟ` JOIN `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` ON `ΑΡΘΡΟ`.`Κωδικός_Τεύχους`=`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους` 
                        JOIN `ΠΕΡΙΟΔΙΚΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Περιοδικού`=`ΠΕΡΙΟΔΙΚΟ`.`Κωδικός_Περιοδικού` 
                        WHERE YEAR(`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`) >=2015 AND YEAR(`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`) <= 2020 
                        GROUP BY `ΠΕΡΙΟΔΙΚΟ`.`Όνομα`, `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Αριθμός_Τεύχους`""")
        r = cur.fetchall()
        
        for row in r:
            list1.insert(END, row)
        cur.close()
        con.close()
        return

    def com19():
        list1.delete(0,END)
        con = pymysql.connect(host = '150.140.186.221',port = 3306, user='db20_up1059338',passwd='up1059338', database='project_db20_up1059338')              
        cur = con.cursor()
        
        cur.execute("""SELECT `ΣΥΝΤΑΚΤΗΣ`.`Όνομα`,`Επώνυμο`, `ΙΔΡΥΜΑ`.`Όνομα` AS `Ίδρυμα` 
                        FROM `Συντάσσει` JOIN `ΣΥΝΤΑΚΤΗΣ` ON `Συντάσσει`.`Κωδικός_Συντάκτη`=`ΣΥΝΤΑΚΤΗΣ`.`Κωδικός_Συντάκτη` 
                        JOIN `ΙΔΡΥΜΑ` ON `Συντάσσει`.`Κωδικός_Ιδρύματος`=`ΙΔΡΥΜΑ`.`Κωδικός_Ιδρύματος` 
                        JOIN `ΑΡΘΡΟ` ON `Συντάσσει`.`Κωδικός_Άρθρου`=`ΑΡΘΡΟ`.`Κωδικός_Άρθρου` 
                        JOIN `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` ON `ΑΡΘΡΟ`.`Κωδικός_Τεύχους`=`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`
                        WHERE `ΣΥΝΤΑΚΤΗΣ`.`Κωδικός_Συντάκτη` <> 2 
                        AND `Συντάσσει`.`Κωδικός_Ιδρύματος` NOT IN (SELECT `Συντάσσει`.`Κωδικός_Ιδρύματος` 
                                                                    FROM `Συντάσσει` JOIN `ΑΡΘΡΟ` ON `Συντάσσει`.`Κωδικός_Άρθρου`=`ΑΡΘΡΟ`.`Κωδικός_Άρθρου`
                                                                    JOIN `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` ON `ΑΡΘΡΟ`.`Κωδικός_Τεύχους`=`ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`
                                                                    WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`= 2 AND `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`=ANY (SELECT MAX(`Ημερομηνία_Έκδοσης`) 
                                                                                                                                                            FROM `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` JOIN `ΑΡΘΡΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`=`ΑΡΘΡΟ`.`Κωδικός_Τεύχους` 
                                                                                                                                                            JOIN `Συντάσσει` ON `ΑΡΘΡΟ`.`Κωδικός_Άρθρου`=`Συντάσσει`.`Κωδικός_Άρθρου` 
                                                                                                                                                            WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`=2))
                        AND `Συντάσσει`.`Κωδικός_Άρθρου` IN (SELECT `Συντάσσει`.`Κωδικός_Άρθρου`FROM `Συντάσσει` WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`=2) 
                        AND `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης` >= ANY (SELECT MIN(`Ημερομηνία_Έκδοσης`) 
                                                                            FROM `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` JOIN `ΑΡΘΡΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`=`ΑΡΘΡΟ`.`Κωδικός_Τεύχους` 
                                                                            JOIN `Συντάσσει` ON `ΑΡΘΡΟ`.`Κωδικός_Άρθρου`=`Συντάσσει`.`Κωδικός_Άρθρου` 
                                                                            WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`=2 AND `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Ημερομηνία_Έκδοσης`= ANY (SELECT MAX(`Ημερομηνία_Έκδοσης`) 
                                                                                                                                                                    FROM `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ` JOIN `ΑΡΘΡΟ` ON `ΤΕΥΧΟΣ_ΠΕΡΙΟΔΙΚΟΥ`.`Κωδικός_Τεύχους`=`ΑΡΘΡΟ`.`Κωδικός_Τεύχους` 
                                                                                                                                                                    JOIN `Συντάσσει` ON `ΑΡΘΡΟ`.`Κωδικός_Άρθρου`=`Συντάσσει`.`Κωδικός_Άρθρου` 
                                                                                                                                                                    WHERE `Συντάσσει`.`Κωδικός_Συντάκτη`=2))""")
        r = cur.fetchall()
        
        for row in r:
            list1.insert(END, row)
        cur.close()
        con.close()
        return

    root = Tk()
    root.title('Statistics')
    root.geometry("730x450")
    wrapper = textwrap.TextWrapper(width=50)

    list1 = Listbox(root, height=25, width=65) #creating the list space to display all the rows of the table
    list1.grid(row=0, column=0, rowspan=18, columnspan=2) #determining the size
    sb1 = Scrollbar(root) #creating a scrollbar for the window to scroll through the list entries
    sb1.grid(row=2, column=2, rowspan=6)
    list1.configure(yscrollcommand=sb1.set) #configuring the scroll function for the scrollbar object sb1
    sb1.configure(command=list1.yview)
    #list1.bind('<<ListboxSelect>>', get_selected_row)

    b1 = Button(root, text="Search", width=10,command= com16) #creating buttons for the various operations. Giving it a name and assigning a particular command to it. 
    b1.grid(row=1, column=3) #size of the button
    b2 = Button(root, text="Search", width=10, command= com17)
    b2.grid(row=3, column=3)
    b3 = Button(root, text="Search", width=10, command= com18)
    b3.grid(row=5, column=3)
    b4 = Button(root, text="Search", width=10, command= com19)
    b4.grid(row=7, column=3)
    b5 = Button(root, text="Close", width=10, command=root.destroy)
    b5.grid(row=11, column=3)

    wr1 = wrapper.fill(text="Μέσος όρος άρθρων ανά έτος, από περιοδικά με impact factor μεγαλύτερο του 1.5")
    label1 = Label(root, text=wr1, width=50)
    label1.grid(row=0, column=3)
    wr2 = wrapper.fill(text="Εμφάνισε τους συντάκτες οι οποίοι έχουν εκδώσει πάνω από 2 άρθρα με διαφορετικά ιδρύματα, τα τελευταία 5 χρόνια")
    label2 = Label(root, text=wr2, width=50)
    label2.grid(row=2, column=3)
    wr3 = wrapper.fill(text="Εμφάνισε τον μέσο όρο σελίδων των άρθρων, για κάθε τεύχος που εκδόθηκε στο διάστημα 2015-2019")
    label3 = Label(root, text=wr3, width=50)
    label3.grid(row=4, column=3)
    wr4 = wrapper.fill(text="Με ποιους συντάκτες από διαφορετικά ιδρύματα έχει συνεργαστεί ο συντάκτης 2 όσο καιρό είναι στο ίδρυμα που βρίσκεται τώρα")
    label4 = Label(root, text=wr4, width=50)
    label4.grid(row=6, column=3)

    root.mainloop() #carry the functioning of the GUI window on a loop until it is closed using the destructor