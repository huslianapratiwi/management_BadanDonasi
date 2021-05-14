from tkinter import *
from tkinter import ttk
from Badan_amal import *
import matplotlib.pyplot as plt
from pandas import DataFrame
from conector import DatabaseDiagram as dbDiagram
import datetime
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
  
class Dashboard:
    def __init__(self,window,id_comp):
        self.window = window
        self.window.geometry("1920x1080+0+0")
        self.window.title("Kartika Bisa")
        self.window.resizable (False,False)
        self.id_comp = id_comp
        self.tampilan()
        

    def tampilan(self):
        title=Label(self.window,text = "Donasi Kartika",font=("times new roman",40,"bold"),bg = "#010c48",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)
        btn_logout=Button(self.window,text="Logout",command=self.exit,font = ("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1700,y = 20,height = 30, width = 150)
        
        ##frame left
        LeftMenu = Frame(self.window,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=70,width=200,height=1080)

        lbl_Menu = Label(LeftMenu,text="MENU",font=("times new roman",20,"bold"),bd =3,bg="green").pack(side=TOP,fill=X)
        btn_Pegawai = Button(LeftMenu,text="Pegawai",command=self.employee,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_kotakAmal = Button(LeftMenu,text="Kotak Amal",command=self.Kotak_amal,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_Donasi = Button(LeftMenu,text="Donasi",command=self.Donasi_btn,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_Donatur = Button(LeftMenu,text="Donatur",command=self.Donatur_btn,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)
        btn_penerima = Button(LeftMenu,text="Penerima",command=self.Penerima_btn,font=("times new roman",20,"bold"),bd =3,bg="white",cursor="hand2").pack(side=TOP,fill=X)

        self.Menu_Utama = Frame(self.window,bd=2,relief=RIDGE, bg="white").place(x=200,y=70,width=1710,height=1080)
        btn_update=Button(LeftMenu,text="Update Diagram",command=self.diagram,font = ("times new roman",15,"bold"),bg="blue",cursor="hand2",fg="white").pack(side=TOP,fill=X)
        self.diagram()
        

    def employee(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Pegawai(self.new_win,self.id_comp)

    def Kotak_amal(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Kotak_amal(self.new_win,self.id_comp)

    def Donasi_btn(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Donasi(self.new_win,self.id_comp)
    
    def Donatur_btn(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Donatur(self.new_win,self.id_comp)
    
    def Penerima_btn(self):
        self.new_win = Toplevel(self.window)
        self.new_obj = Penerima(self.new_win,self.id_comp)

    def exit(self):
        self.window.destroy()
    
    def diagram(self):
        a = datetime.date.today()
        numdays = 10
        dateList = []
        datecount = []

        for x in range (0, numdays):
            dateList.append(a - datetime.timedelta(days = x))


        for i in dateList : 
            datecount.append(dbDiagram.gettanggal_donasi(self.id_comp,i))

        data1 = {'Tanggal': dateList,
            'Jumlah Donasi': datecount
        }
        df1 = DataFrame(data1,columns=['Tanggal','Jumlah Donasi'])

        figure1 = plt.Figure(figsize=(4,6), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, self.Menu_Utama)
        line1.get_tk_widget().place(x=200,y=70,width=1700,height=400)
        df1 = df1[['Tanggal','Jumlah Donasi']].groupby('Tanggal').sum()
        df1.plot(kind='line', legend=True, ax=ax1, color='b',marker='o', fontsize=10)
        ax1.set_title('Kegiatan donasi 10 hari terakhir')

        list_experience = []
        list_jumlahexp = []
        for i in range (16):
            list_experience.append(i)
        for i in range (16):
            temp_exp = dbDiagram.getexperience(self.id_comp,i)
            if (temp_exp == None):
                temp_exp = 0
            list_jumlahexp.append(temp_exp)

        data2 = {'Experience': list_experience,'Banyak Pegawai': list_jumlahexp}
        df2 = DataFrame(data2,columns=['Experience','Banyak Pegawai'])

        figure2 = plt.Figure(figsize=(3,3), dpi=100)
        ax2 = figure2.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure2, self.Menu_Utama)
        bar2.get_tk_widget().place(x=320,y=500,width=600,height=400) 
        df2 = df2[['Experience','Banyak Pegawai']].groupby('Experience').sum()
        df2.plot(kind='bar', legend=True, ax=ax2)
        ax2.set_title('Jumlah Experience Pegawai')
     
        temp_jenis = []
        jumlah_jenis = []
        jenis_barang = []
        for i in ["Makanan","Kebutuhan Pokok","Baju","Buku","Other"] : 
            temp_jenis.append(dbDiagram.getjenis(self.id_comp,i))
        for i in temp_jenis:
            if i[0][0] != 0:
                jumlah_jenis.append(i[0][0])
                jenis_barang.append(i[0][1])

        figure3 = plt.Figure(figsize=(3,3), dpi=100) # create a figure object 
        ax3 = figure3.add_subplot(111) # add an Axes to the figure
        ax3.pie(jumlah_jenis, radius=1, labels=jenis_barang,autopct='%0.2f%%', shadow=True,)
        chart1 = FigureCanvasTkAgg(figure3,self.Menu_Utama)
        chart1.get_tk_widget().place(x=1000,y=500,width=600,height=400)
        ax3.set_title('Persentase Jenis Barang')




def win (id_company):
    window = Tk()
    Dashboard(window,id_company)
    window.mainloop()
  
if __name__ == '__main__':
        win(1)