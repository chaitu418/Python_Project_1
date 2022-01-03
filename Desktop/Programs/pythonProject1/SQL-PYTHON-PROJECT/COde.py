import sqlite3,sys
from mysql import connector as mc

def CreateDB(self):

    try:
        self.connection = sqlite3.connect("test.db")
    except Exception as e:
        print(str(e))

    # Creating a table for it.
    sql_command = """CREATE TABLE employee (
    staff_number INTEGER PRIMARK KEY,
    fname VARCHAR(20),
    lname VARCHAR(20),
    gender CHAR(1),
    joining DATE,
    birth_date DATE);"""

    cursor = self.connection.cursor()
    Table=[]
    Table="""SHOW DATABASES;"""
    print(Table)
    if "employee" not in Table:
        cursor.execute(sql_command)

    """populating DB with table entries"""
    def populate(self):
        staff_data=[("William","shakepear","m","1961-10-25"),
            ("Frank","Schiller","m","1955-08-17"),
            ("Jane","wall","f","1989-03-14")]

#now we are inserting above staff sdate in to the DB

        for staff, p in enumerate(staff_data):
            print(staff, p)
            format_str = """INSERT INTO employee (staff_number,fname,lname,gender,birth_date) VALUES ('{staff_no}','{first}','{last}','{gender}','{birthdate}');"""
            sql_command = format_str.format(staff_no=staff, first=p[0], last=p[1], gender=p[2], birthdate=p[3])

            print(sql_command)
            cursor.execute(sql_command)

        """Dsiplay DB contentn in table format"""

        cursor.execute("SELECT * FROM employee")
        print("----------------THe output result is as  follows-------------")
        result = cursor.fetchall()
        for r in result:
            print(r)

def Close(self):
    self.connection.commit()
    self.cursor.close()
    self.connection.close()

if __name__=="__main__":
    Rootobj=CreateDB()
    populate()
    Close()