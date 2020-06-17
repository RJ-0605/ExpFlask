
class Register_validator:

#  In the near future will be receiving the date of registration and time as an input from the main.py


    def __init__(self,firstname,lastname,username,email,passwd,confirm_passwd):
        self.email = email
        self.passwd = passwd
        self.confirm_passwd = confirm_passwd
        self.firstname = firstname
        self.lastname = lastname
        self.username=username



    def validator(self):
        if self.firstname and self.lastname and self.username and  self.passwd and self.confirm_passwd and self.email != "" and self.passwd == self.confirm_passwd and len(str(self.passwd)) >= 6 :
            print('Meets all requirements')
            return True
        else:
            return False



class Login_validator:

    def __init__(self,username,email,passwd):
        self.email = email
        self.passwd = passwd  
        self.username=username


    def validator(self):
        if  self.username and self.passwd and  self.email != "":
            print('Meets all requirements')
            return True
        else:
            return False

