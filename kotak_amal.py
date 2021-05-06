from tkinter import *

class Kotak_amal: 
    def __init__(self,window):
        self.window = window
        self.window.geometry("1080x480+450+300")
        self.window.title("Kartika Bisa")

def win ():
    window = Tk()
    objek = Kotak_amal(window)
    window.mainloop()
  
if __name__ == '__main__':
        win()