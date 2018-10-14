import sqlite3

class DataHandler:
    #Initialize .db File and DB Cursor
    def __init__(self, db_file):
        self.dh = sqlite3.connect(db_file)
        self.c = self.dh.cursor()

    #Checks if There's a Match for the Inputted Username and Password
    def admin_log(self, user, password):
        self.c.execute("SELECT count(*) FROM adminTable WHERE AUser=? AND APass=?", (user, password))
        count, = self.c.fetchone()
        if count != 0:
            return True
        else:
            return False

    #Find if There's an Existing Account Number
    def find_acc(self, anum):
        self.c.execute("SELECT count(*) FROM accounts WHERE ANum=?", (anum,))
        count, = self.c.fetchone()
        if count != 0:
            return True
        else:
            return False

    #Checks if There's a Repetition of Card Number and/or Account Number
    def check_reps(self, anum, cnum):
        self.c.execute("SELECT count(*) FROM accounts WHERE ANum=? or CNum=?", (anum, cnum))
        count, = self.c.fetchone()
        if count != 0:
            return True
        else:
            return False

    #Removes All the Data for the Given Account Number
    def delete_acc(self, anum):
        self.c.execute("DELETE FROM accounts WHERE ANum=?", (anum,))
        self.c.execute("DELETE FROM clientInfo WHERE ANum=?", (anum,))
        self.dh.commit()

    #Adds A Record into the Table
    def add_acc(self, cn, an, pin, fn, mn, ln, age, contact, email, address, bal):
        self.c.execute("INSERT INTO clientInfo VALUES(?,?,?,?,?,?,?,?,?)", (an, fn, mn, ln, age, contact, email, address, bal))
        self.c.execute("INSERT INTO accounts VALUES(?,?,?)", (cn, an, pin))
        self.dh.commit()

    #Fetch the Data for the Given Account Number
    def view_info(self, an):
        self.c.execute("SELECT * from clientInfo WHERE ANum=?", (an,))
        record = self.c.fetchone()
        return record

    #Also Fetch the Data for the Given Account Number, but on the other Table
    def view_info1(self, an):
        self.c.execute("SELECT CNum from accounts WHERE ANum=?", (an,))
        record1 = self.c.fetchone()
        return record1

    #Checks if There's a Match for the Inputted Card Number and PIN
    def client_log(self, cnum, pnum):
        self.c.execute("SELECT count(*) FROM accounts WHERE CNum=? AND PIN=?", (cnum, pnum))
        count, = self.c.fetchone()
        if count != 0:
            return True
        else:
            return False

    #Fetch the Account Number for the Given Card Number
    def view_anum(self, cnum):
        self.c.execute("SELECT ANum FROM accounts WHERE CNum=?", (cnum,))
        record = self.c.fetchone()
        return record

    #Get the Remaining Balance of the Client Account
    def get_bal(self, an):
        self.c.execute("SELECT Balance FROM clientInfo WHERE ANum=?", (an,))
        record = self.c.fetchone()
        return record

    #Fetch the PIN for the Given Account Number
    def get_pin(self, an):
        self.c.execute("SELECT PIN FROM accounts WHERE ANum=?", (an,))
        record = self.c.fetchone()
        return record

    #Change Balance Value in the Account
    def update_bal(self, newbal, an):
        self.c.execute("UPDATE clientInfo SET Balance=? WHERE ANum=?", (newbal, an))
        self.dh.commit()

    #Change the PIN of the Client Account
    def update_pin(self, pin, an):
        self.c.execute("UPDATE accounts SET PIN=? WHERE ANum=?", (pin, an))
        self.dh.commit()








