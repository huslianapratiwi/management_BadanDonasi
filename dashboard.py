from tkinter import *
from pegawai import Pegawai
from kotak_amal import Kotak_amal
  
class Dashboard:
    def __init__(self,window,id_comp):
        self.window = window
        print(id_comp)
        self.window.geometry("1920x1080+0+0")
        self.window.title("Kartika Bisa")
        self.window.resizable (False,False)
        self.tampilan()
        self.id_comp = id_comp

    def tampilan(self):
        title=Label(self.window,text = "Donasi Kartika",font=("times new roman",40,"bold"),bg = "#010c48",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)
        btn_logout=Button(self.window,text="Logout",command=self.exit,font = ("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1700,y = 20,height = 30, width = 150)
        
        ##frame left
        LeftMenu = Frame(self.window,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=70,width=200,height=700)

        lbl_Menu = Label(LeftMenu,text="MENU",font=("times new roman",20,"bold"),bd =3,bg="green").pack(side=TOP,fill=X)
        btn_Pegawai = Button(LeftMenu,text="Pegawai",command=self.employee,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_kotakAmal = Button(LeftMenu,text="Kotak Amal",command=self.Kotak_amal,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_Donasi = Button(LeftMenu,text="Donasi",font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_Donatur = Button(LeftMenu,text="Donatur",font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_penerima = Button(LeftMenu,text="Penerima",font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)

    def employee(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Pegawai(self.new_win,self.id_comp)

    def Kotak_amal(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Kotak_amal(self.new_win)
    
    def exit(self):
        self.window.destroy()

def win ():
    window = Tk()
    Dashboard(window,1)
    window.mainloop()
  
if __name__ == '__main__':
        win()