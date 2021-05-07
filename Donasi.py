from tkinter import *

class donasi:
    def __init__(self,window,id_dntr):
        self.window = window
        self.window.geometry("720x480+600+250")
        self.window.title("Donasi")
        self.window.resizable (False,False)
        self.window.config(bg="white")
        self.id_dntr = id_dntr

def win ():
    window = Tk()
    Donasi(window)
    window.mainloop()
  
if __name__ == '__main__':
    win()