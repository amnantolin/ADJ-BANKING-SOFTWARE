import sqlite3

class DataHandler:
    def __init__(self, db_file):
        self.dh = sqlite3.connect(db_file)
        self.c = self.dh.cursor()

    def admin_log(self, user, password):
        self.c.execute("SELECT count(*) FROM adminTable WHERE AUser=? AND APass=?", (user, password))
        count, = self.c.fetchone()
        if count != 0:
            return True
        else:
            return False

    def find_acc(self, anum):
        self.c.execute("SELECT count(*) FROM accounts WHERE ANum=?", (anum,))
        count, = self.c.fetchone()
        if count != 0:
            return True
        else:
            return False

    def check_reps(self, anum, cnum):
        self.c.execute("SELECT count(*) FROM accounts WHERE ANum=? or CNum=?", (anum, cnum))
        count, = self.c.fetchone()
        if count != 0:
            return True
        else:
            return False

    def delete_acc(self, anum):
        self.c.execute("DELETE FROM accounts WHERE ANum=?", (anum,))
        self.c.execute("DELETE FROM clientInfo WHERE ANum=?", (anum,))
        self.dh.commit()

    def add_acc(self, cn, an, pin, fn, mn, ln, age, contact, email, address, bal):
        self.c.execute("INSERT INTO clientInfo VALUES(?,?,?,?,?,?,?,?,?)", (an, fn, mn, ln, age, contact, email, address, bal))
        self.c.execute("INSERT INTO accounts VALUES(?,?,?)", (cn, an, pin))
        self.dh.commit()

    def view_info(self, an):
        self.c.execute("SELECT * from clientInfo WHERE ANum=?", (an,))
        record = self.c.fetchone()
        return record

    def view_info1(self, an):
        self.c.execute("SELECT CNum from accounts WHERE ANum=?", (an,))
        record1 = self.c.fetchone()
        return record1

    def client_log(self, cnum, pnum):
        self.c.execute("SELECT count(*) FROM accounts WHERE CNum=? AND PIN=?", (cnum, pnum))
        count, = self.c.fetchone()
        if count != 0:
            return True
        else:
            return False

    def view_anum(self, cnum):
        self.c.execute("SELECT ANum FROM accounts WHERE CNum=?", (cnum,))
        record = self.c.fetchone()
        return record

    def get_bal(self, an):
        self.c.execute("SELECT Balance FROM clientInfo WHERE ANum=?", (an,))
        record = self.c.fetchone()
        return record

    def get_pin(self, an):
        self.c.execute("SELECT PIN FROM accounts WHERE ANum=?", (an,))
        record = self.c.fetchone()
        return record

    def update_bal(self, newbal, an):
        self.c.execute("UPDATE clientInfo SET Balance=? WHERE ANum=?", (newbal, an))
        self.dh.commit()

    def update_pin(self, pin, an):
        self.c.execute("UPDATE accounts SET PIN=? WHERE ANum=?", (pin, an))
        self.dh.commit()








