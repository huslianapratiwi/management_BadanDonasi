from tkinter import *
from donasi import *
from conector import dbdonatur 
import matplotlib.pyplot as plt
from pandas import DataFrame
from conector import DatabaseDiagram as dbDiagram
import datetime
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class donatur:
    def __init__(self,window,id_dntr):
        self.window = window
        self.window.geometry("1280x720+0+0")
        self.window.title("Donatur")
        self.window.resizable (False,False)
        self.window.config(bg="white")
        self.id_dntr = id_dntr
        temp = dbdonatur.getnama(id_dntr)
        self.nama = temp[0][0].split(" ")

        title=Label(self.window,text = "Selamat Datang " + self.nama[0],font=("times new roman",30,"bold"),bg = "green",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)

        LeftMenu = Frame(self.window,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=70,width=150,height=900)

        lbl_Menu = Label(LeftMenu,text="MENU",font=("times new roman",15,"bold"),bd =3,bg="yellow",fg="black").pack(side=TOP,fill=X)
        btn_Uang = Button(LeftMenu,text="Uang",command=self.uang,font=("times new roman",15,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_Barang = Button(LeftMenu,text="Barang",command=self.barang,font=("times new roman",15,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_riwayat = Button(LeftMenu,text="Riwayat Donasi",command=self.riwayat,font=("times new roman",15,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        
        self.Menu_Utama = Frame(self.window,bd=2,relief=RIDGE, bg="white").place(x=150,y=70,width=1710,height=1080)
        btn_update=Button(LeftMenu,text="Update Table",command=self.diagram,font = ("times new roman",15,"bold"),bg="blue",cursor="hand2",fg="white").pack(side=TOP,fill=X)
        self.diagram()
        
        
    def uang(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = donasi(self.new_win,self.id_dntr)

    def barang(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = donasi_barang(self.new_win,self.id_dntr)

    def riwayat(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Riwayat(self.new_win,self.id_dntr)

    def diagram(self):
        a = datetime.date.today()
        numdays = 10
        dateList = []
        datecount = []

        for x in range (0, numdays):
            dateList.append(a - datetime.timedelta(days = x))


        for i in dateList : 
            datecount.append(dbDiagram.gettanggal_user(self.id_dntr,i))

        data1 = {'Tanggal': dateList,
            'Jumlah Donasi': datecount
        }
        df1 = DataFrame(data1,columns=['Tanggal','Jumlah Donasi'])

        figure1 = plt.Figure(figsize=(1,1), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, self.Menu_Utama)
        line1.get_tk_widget().place(x=160,y=70,width=1200,height=350)
        df1 = df1[['Tanggal','Jumlah Donasi']].groupby('Tanggal').sum()
        df1.plot(kind='line', legend=True, ax=ax1, color='b',marker='o', fontsize=10)
        ax1.set_title('Kegiatan donasi 10 hari terakhir')

        temp_jenis = []
        jumlah_jenis = []
        jenis_barang = []
        for i in ["Makanan","Kebutuhan Pokok","Baju","Buku","Other"] : 
            temp_jenis.append(dbDiagram.getjenisuser(self.id_dntr,i))
        for i in temp_jenis:
            if i[0][0] != 0:
                jumlah_jenis.append(i[0][0])
                jenis_barang.append(i[0][1])

        figure3 = plt.Figure(figsize=(1,1), dpi=100) # create a figure object 
        ax3 = figure3.add_subplot(111) # add an Axes to the figure
        ax3.pie(jumlah_jenis, radius=1, labels=jenis_barang,autopct='%0.2f%%')
        chart1 = FigureCanvasTkAgg(figure3,self.Menu_Utama)
        chart1.get_tk_widget().place(x=300,y=450,width=300,height=200) 
        ax3.set_title('Persentase Jenis Barang')

    

def win (id_comp):
    window = Tk()
    donatur(window,id_comp)
    window.mainloop()
  
if __name__ == '__main__':
    win(1)