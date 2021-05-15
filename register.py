from tkinter import *
from tkinter import ttk, messagebox
from dashboard import Dashboard
from conector import dbregis as dbregis

class register_badan:
    def __init__(self,window):
        self.window = window
        self.window.geometry("540x480+300+150")
        self.window.title("Register Badan Amal")
        self.window.resizable (False,False)
        self.window.config(bg="white")

        self.var_nama = StringVar()
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_alamat = StringVar()

        #button
        title  = Label(self.window,text = "Register",font=("times new roman",40,"bold"),bg = "#010c48",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)

        inputframe=LabelFrame(self.window,bg="white")
        inputframe.place(x=70,y=100,width=400,height=350)
        
        lbl_nama = Label(inputframe,text = "Nama",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 20)
        nama_input = Entry(inputframe,width = 40,textvariable=self.var_nama).place(x=30,y=40,height=30)

        lbl_username = Label(inputframe,text = "Username",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 80)
        usenname_input = Entry(inputframe,width = 40,textvariable=self.var_username).place(x=30,y=100,height=30)

        input_password = Entry(inputframe,width = 40,textvariable=self.var_password,show="*").place(x=30,y=163,height=30)
        lbl_password = Label(inputframe,text = "Password",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 140)

        alamat_input = Entry(inputframe,width = 40,textvariable=self.var_alamat).place(x=30,y=230,height=30)
        lbl_alamat = Label(inputframe,text = "Alamat",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 205)

        btn_regis = Button(inputframe,text="Registrasi",command=self.regis).place(x=150,y=300)
    
    def regis(self):
        if(self.var_nama.get() == "" or self.var_username.get() == "" or self.var_password.get() == "" or self.var_alamat == ""):
            messagebox.showwarning("Warning","Isi Semua Data!",parent=self.window)
        else :
            if dbregis.cekada_badan("username",self.var_username.get()):
                messagebox.showwarning("Warning","Username sudah ada",parent=self.window)
            else :
                if len(self.var_username.get()) > 15: 
                    messagebox.showwarning("Warning","Username Terlalu Panjang",parent=self.window)
                elif len(self.var_password.get()) > 15: 
                    messagebox.showwarning("Warning","Password Terlalu Panjang",parent=self.window)
                elif len(self.var_nama.get()) > 15: 
                    messagebox.showwarning("Warning","Nama Terlalu Panjang",parent=self.window)
                elif len(self.var_alamat.get()) > 15: 
                    messagebox.showwarning("Warning","Alamat Terlalu Panjang",parent=self.window)
                else : 
                    dbregis.insert_badan(self.var_nama.get(),self.var_username.get(),self.var_password.get(),self.var_alamat.get())
                    temp = messagebox.showinfo("Info","Berhasil Melakukan Registrasi")
                    if (temp):
                        self.exit()

    def exit(self):
        self.window.destroy()

class register_donasi:
    def __init__(self,window):
        self.window = window
        self.window.geometry("540x600+400+50")
        self.window.title("Register Donatur")
        self.window.resizable (False,False)
        self.window.config(bg="white")

        self.var_nama = StringVar()
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_alamat = StringVar()
        self.var_notelp = StringVar()
        self.var_tipe = StringVar()


        #button
        title  = Label(self.window,text = "Register",font=("times new roman",40,"bold"),bg = "#010c48",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)

        inputframe=LabelFrame(self.window,bg="white")
        inputframe.place(x=70,y=100,width=400,height=490)
        
        lbl_nama = Label(inputframe,text = "Nama",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 20)
        nama_input = Entry(inputframe,width = 40,textvariable=self.var_nama).place(x=30,y=40,height=30)

        lbl_username = Label(inputframe,text = "Username",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 80)
        usenname_input = Entry(inputframe,width = 40,textvariable=self.var_username).place(x=30,y=100,height=30)

        input_password = Entry(inputframe,width = 40,textvariable=self.var_password,show="*").place(x=30,y=163,height=30)
        lbl_password = Label(inputframe,text = "Password",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 140)

        alamat_input = Entry(inputframe,width = 40,textvariable=self.var_alamat).place(x=30,y=230,height=30)
        lbl_alamat = Label(inputframe,text = "Alamat",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 205)

        lbl_no_telp = Label(inputframe,text = "Nomor Telepon",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 270)
        no_telp_input = Entry(inputframe,width = 40,textvariable=self.var_notelp).place(x=30,y=295,height=30)

        lbl_tipe = Label(inputframe,text = "Tipe",bg="white",font=("times new roman",12,"bold")).place(x = 30,y = 330)
        cmb_tipe =ttk.Combobox(inputframe,values=("Personal","Organisasi"),state='readonly',textvariable=self.var_tipe)
        cmb_tipe.place(x=30,y=355,width=180,height=30)
        cmb_tipe.current(0)


        btn_regis = Button(inputframe,text="Registrasi",command=self.regis).place(x=150,y=420)
    
    def regis(self):
        if(self.var_notelp.get() == "" or self.var_nama.get() == "" or self.var_username.get() == "" or self.var_password.get() == "" or self.var_alamat.get() == ""):
            messagebox.showwarning("Warning","Isi Semua Data!",parent=self.window)
        else :
            if dbregis.cekada_dntr("username",self.var_username.get()):
                messagebox.showwarning("Warning","Username sudah ada",parent=self.window)
            else :
                if len(self.var_username.get()) > 20: 
                    messagebox.showwarning("Warning","Username Terlalu Panjang",parent=self.window)
                elif len(self.var_password.get()) > 20: 
                    messagebox.showwarning("Warning","Password Terlalu Panjang",parent=self.window)
                elif len(self.var_nama.get()) > 30: 
                    messagebox.showwarning("Warning","Nama Terlalu Panjang",parent=self.window)
                elif len(self.var_alamat.get()) > 40: 
                    messagebox.showwarning("Warning","Alamat Terlalu Panjang",parent=self.window)
                else : 
                    dbregis.insert_donatur(self.var_nama.get(),self.var_username.get(),self.var_password.get(),self.var_alamat.get(),self.var_notelp.get(),self.var_tipe.get())
                    x = messagebox.showinfo("Info","Berhasil Registrasi")
                    if(x):
                        self.exit()


    def exit(self):
        self.window.destroy()


def win ():
    window = Tk()
    register_donasi(window)
    window.mainloop()
  
if __name__ == '__main__':
    win()