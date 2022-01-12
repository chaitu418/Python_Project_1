class Student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def verify_registration(self):
        status=self.get_status()
        self.status_verified=status=="registered"

    def get_gaurdianName(self):
        self.guardian="Goodman"

    def get_status(self):

        status=querydb(self.fname,self.lname)
        return status
    