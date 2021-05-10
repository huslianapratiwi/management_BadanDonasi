from tkinter import *
from donasi import *
from conector import dbdonatur 

class donatur:
    def __init__(self,window,id_dntr):
        self.window = window
        self.window.geometry("1920x1080+0+0")
        self.window.title("Donatur")
        self.window.resizable (False,False)
        self.window.config(bg="white")
        self.id_dntr = id_dntr
        temp = dbdonatur.getnama(id_dntr)
        self.nama = temp[0][0].split(" ")

        title=Label(self.window,text = "Selamat Datang " + self.nama[0],font=("times new roman",40,"bold"),bg = "green",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)

        LeftMenu = Frame(self.window,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=70,width=200,height=900)

        lbl_Menu = Label(LeftMenu,text="MENU",font=("times new roman",20,"bold"),bd =3,bg="yellow",fg="black").pack(side=TOP,fill=X)
        btn_Uang = Button(LeftMenu,text="Uang",command=self.uang,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_Barang = Button(LeftMenu,text="Barang",command=self.barang,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_riwayat = Button(LeftMenu,text="Riwayat Donasi",command=self.riwayat,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
    
    def uang(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = donasi(self.new_win,self.id_dntr)

    def barang(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = donasi_barang(self.new_win,self.id_dntr)

    def riwayat(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Riwayat(self.new_win,self.id_dntr)
    

def win (id_comp):
    window = Tk()
    donatur(window,id_comp)
    window.mainloop()
  
if __name__ == '__main__':
    win(1)