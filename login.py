from tkinter import *
from tkinter import ttk, messagebox
from dashboard import Dashboard
from register import *
from Donasi import donasi
from conector import dblogin as dblogin

class login_amal:
    id_company = int()

    def __init__(self,window):
        top = 50
        self.window = window
        self.window.geometry("400x260+700+400")
        self.window.title("Login Badan Amal")
        self.window.resizable (False,False)
        self.window.config(bg="white")
    
        self.var_username = StringVar()
        self.var_password = StringVar()

        #button

        inputframe=LabelFrame(self.window,bg="white")
        inputframe.place(x=0,y=10,width=400,height=350-top*2)

        lbl_username = Label(inputframe,text = "Username",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 80-top)
        usenname_input = Entry(inputframe,width = 40,textvariable=self.var_username).place(x=30,y=100-top,height=30)

        input_password = Entry(inputframe,width = 40,textvariable=self.var_password,show="*").place(x=30,y=163-top,height=30)
        lbl_password = Label(inputframe,text = "Password",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 140-top)

        btn_regis = Button(inputframe,text="Registrasi",command=self.regis,bg="blue",fg="white").place(x=180,y=300-top*2)
        btn_login = Button(inputframe,text="Login",command=self.login,bg="green",fg="white").place(x=290,y=300-top*2)
    
    def regis(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = register_badan(self.new_win)
    
    def login(self):
        if(self.var_username.get() == "" or self.var_password.get() == ""):
            messagebox.showwarning("Warning","Isi dengan lengkap!",parent=self.window) 
        else : 
            real_user = dblogin.getdata("username",self.var_username.get())
            real_pass = dblogin.getdata("password",self.var_username.get())
            if self.var_username.get() == real_user[0]:
                if self.var_password.get() == real_pass[0]:
                    nilai = messagebox.showinfo("Berhasil","Login Berhasil")
                    temp = dblogin.getdata("id_company",self.var_username.get())
                    login_amal.id_company = temp[0]
                    if nilai : 
                         self.dashboard()
            else :
                messagebox.showwarning("warning","username tidak ada")

    def dashboard(self): 
        self.new_win = Toplevel(self.window)
        self.new_obj = Dashboard(self.new_win,login_amal.id_company)

class login_donatur(login_amal):
    id_donatur = int()
    def __init__(self,window):
        super().__init__(window)
        self.window.title("Login Donatur")

    def regis(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = register_donasi(self.new_win)
    
    def login(self):
        if(self.var_username.get() == "" or self.var_password.get() == ""):
            messagebox.showwarning("Warning","Isi dengan lengkap!",parent=self.window) 
        else : 
            real_user = dblogin.getdata_donatur("username",self.var_username.get())
            real_pass = dblogin.getdata_donatur("password",self.var_username.get())
            if self.var_username.get() == real_user[0]:
                if self.var_password.get() == real_pass[0]:
                    nilai = messagebox.showinfo("Berhasil","Login Berhasil")
                    temp = dblogin.getdata_donatur("id_donatur",self.var_username.get())
                    login_donatur.id_donatur = temp[0]
                    if nilai :  
                         self.Donasi()
            else :
                messagebox.showwarning("warning","username tidak ada")

    def Donasi(self): 
        self.new_win = Toplevel(self.window)
        self.new_obj = donasi(self.new_win,login_donatur.id_donatur)


def win ():
    window = Tk()
    login_donatur(window)
    window.mainloop()
  
if __name__ == '__main__':
    win()