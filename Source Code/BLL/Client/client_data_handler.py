import sqlite3

class DataHandler:
    def __init__(self, db_file):
        self.dh = sqlite3.connect(db_file)
        self.c = self.dh.cursor()

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
