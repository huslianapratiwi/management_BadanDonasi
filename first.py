from tkinter import *
from dashboard import Dashboard

class Menu_awal:
    def __init__(self,window):
        self.window = window
        self.window.geometry("720x480+600+250")
        self.window.title("Menu Awal")
        self.window.resizable (False,False)
        self.window.config(bg="white")

        #button
        title  = Label(self.window,text = "Menu Awal",font=("times new roman",40,"bold"),bg = "#010c48",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)
        lbl_mn = Label(self.window,text = "Login Sebagai",font=("times new roman",15,"bold"),bg="white").place(x = 0, y = 70,relwidth = 1,height = 30)
        
        Donatur = Button(self.window,text = "Donatur",bg="white",fg ="black",font=("times new roman",12,"bold"))
        Donatur.place(x=100,y=300)

        bdn_aml = Button(self.window,text = "Badan Amal",command=self.Badan_amal,bg="white",fg ="black",font=("times new roman",12,"bold"))
        bdn_aml.place(x=500,y=300)

    def Badan_amal(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Dashboard(self.new_win)

    def exit(self):
        self.window.destroy()


def win ():
    window = Tk()
    Menu_awal(window)
    window.mainloop()
  
if __name__ == '__main__':
    win()