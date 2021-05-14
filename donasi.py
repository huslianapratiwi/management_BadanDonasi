from tkinter import *
from tkinter import ttk, messagebox
from conector import donasi_uang
from conector import donasi_barang as dbdonasi_barang
from conector import DatabaseRiwayat as dbriwayat

class donasi:
    def __init__(self,window,id_dntr):
        self.window = window
        self.window.geometry("540x400+600+350")
        self.window.title("Donasi Uang")
        self.window.resizable (False,False)
        self.window.config(bg="white")

        self.id_dntr = id_dntr
        self.nama_badan = StringVar()
        self.nominal = StringVar()

        title  = Label(self.window,text = "Donasi Uang",font=("times new roman",40,"bold"),bg = "green",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)

        inputframe=LabelFrame(self.window,bg="white")
        inputframe.place(x=70,y=100,width=400,height=250)
        
        lbl_Nominal = Label(inputframe,text = "Nominal dalam (idr)",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 20)
        Nominal_input = Entry(inputframe,textvariable = self.nominal,width = 40).place(x=30,y=40,height=30)
        
        lbl_nama_company = Label(inputframe,text = "Badan Amal yang ingin disumbangkan",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 100)
        cmb_nama_company =ttk.Combobox(inputframe,values=donasi_uang.getBadanAmal(),state='readonly',textvariable = self.nama_badan)
        cmb_nama_company.place(x=30,y=120,width=320,height=30)
        cmb_nama_company.current(0)

        btn_donasi = Button(inputframe,text="Donasikan",command=self.Donasikan,font=("times new roman",12,"bold"),bg="green",fg="white").place(x=150,y=200)

    def Donasikan(self):
        if(self.nominal.get() == ""):
            messagebox.showwarning("Warning","Isi Semua Data!",parent=self.window)
        else :
            donasi_uang.insert(self.id_dntr,self.nominal.get(),self.nama_badan.get())
            messagebox.showinfo("Info","Data berhasil dimasukkan")
            self.clear()

    def clear(self):
        self.nominal.set("")

class donasi_barang:
    def __init__(self,window,id_dntr):
        self.window = window
        self.window.geometry("540x500+600+350")
        self.window.title("Donasi Barang")
        self.window.resizable (False,False)
        self.window.config(bg="white")
        self.id_dntr = id_dntr

        self.jumlah_barang = StringVar()
        self.tipe = StringVar()
        self.nama_badan = StringVar()

        title  = Label(self.window,text = "Donasi Barang",font=("times new roman",40,"bold"),bg = "green",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 70)

        inputframe=LabelFrame(self.window,bg="white")
        inputframe.place(x=70,y=100,width=400,height=350)
        
        lbl_Nominal = Label(inputframe,text = "Jumlah Barang (pcs)",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 20)
        Nominal_input = Entry(inputframe,width = 40,textvariable=self.jumlah_barang).place(x=30,y=40,height=30)
        
        lbl_nama_company = Label(inputframe,text = "Tipe Barang Disumbangkan",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 100)
        cmb_nama_company =ttk.Combobox(inputframe,values=("Baju","Makanan","Kebutuhan Pokok","Buku","other"),state='readonly',textvariable=self.tipe)
        cmb_nama_company.place(x=30,y=125,width=320,height=30)
        cmb_nama_company.current(0)

        lbl_nama_company = Label(inputframe,text = "Badan Amal yang ingin disumbangkan",bg="white",font=("times new roman",12,"bold")).place(x = 28,y = 185)
        cmb_nama_company =ttk.Combobox(inputframe,values=donasi_uang.getBadanAmal(),state='readonly',textvariable=self.nama_badan)
        cmb_nama_company.place(x=30,y=210,width=320,height=30)
        cmb_nama_company.current(0)

        btn_donasi = Button(inputframe,command = self.donasikan,text="Donasikan",font=("times new roman",12,"bold"),bg="green",fg="white").place(x=150,y=300)

    def donasikan(self):
        """self.jumlah_barang = StringVar()
        self.tipe = StringVar()
        self.nama_badan = StringVar()"""

        if(self.jumlah_barang.get()==""):
            messagebox.showwarning("Warning","Data belum Diisi")
        else : 
            dbdonasi_barang.insert(self.id_dntr,self.jumlah_barang.get(),self.tipe.get(),self.nama_badan.get())
            messagebox.showinfo("Info","Donasi Berhasil")

class Riwayat:
    def __init__(self,window,id_dntr):
        self.window = window
        self.window.geometry("700x600+600+350")
        self.window.title("Riwayat Donasi")
        self.window.resizable (False,False)
        self.window.config(bg="white")
        self.id_dntr = id_dntr
        self.cmbox_search = StringVar()
        self.var_search = StringVar()

        title  = Label(self.window,text = "Riwayat Donasi",font=("times new roman",30,"bold"),bg = "green",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 50)

        Searchframe=LabelFrame(self.window,text="Search Donasi",bg="white")
        Searchframe.place(x=180,y=70,width=520,height=70)

        cmb_search=ttk.Combobox(Searchframe,textvariable = self.cmbox_search,values=("Select","Id","Tanggal Donasi","Jenis Donasi","Jumlah Donasi","Badan Donasi"),state='readonly')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        self.menu_cmb=ttk.Combobox(self.window,values=("UANG","BARANG"))
        self.menu_cmb.place(x=20,y=90,width=90,height=30)
        self.menu_cmb.current(0)
        self.menu_cmb.bind("<<ComboboxSelected>>", self.gettabel)

        search_data = Entry(Searchframe,textvariable = self.var_search)
        search_data.place(x=200,y=10,width=180,height=30)

        submit_search = Button(Searchframe,command = self.getsearch,text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
        submit_search.place(x=400,y=10,width=90,height = 30)

        
    def showuang(self):
        getrow = dbriwayat.getdata(self.id_dntr)
        self.TabelDonasi.delete(*self.TabelDonasi.get_children())
        for row in getrow:
            self.TabelDonasi.insert('',END,values=row)

    def showbarang(self):
        getrow = dbriwayat.getdatabarang(self.id_dntr)
        self.TabelDonasi_barang.delete(*self.TabelDonasi_barang.get_children())
        for row in getrow:
            self.TabelDonasi_barang.insert('',END,values=row)

    def hasiluang(self,getrow):
        self.TabelDonasi.delete(*self.TabelDonasi.get_children())
        for row in getrow:
            self.TabelDonasi.insert('',END,values=row)

    def hasilbarang(self,getrow):
        self.TabelDonasi_barang.delete(*self.TabelDonasi_barang.get_children())
        for row in getrow:
            self.TabelDonasi_barang.insert('',END,values=row)
    
    def getsearch(self):
        if self.menu_cmb.get() == "UANG":

            if self.cmbox_search.get() == "Select" or self.var_search.get() == "":
                self.showuang()

            elif self.cmbox_search.get() == "Id":
                getrow = dbriwayat.getsearchuang(self.id_dntr,"Donasi.id_donasi",self.var_search.get())
                self.hasiluang(getrow)

            elif self.cmbox_search.get() == "Tanggal Donasi":
                getrow = dbriwayat.getsearchuang(self.id_dntr,"Donasi.tgl_donasi",self.var_search.get())
                self.hasiluang(getrow)

            elif self.cmbox_search.get() == "Jumlah Donasi":
                getrow = dbriwayat.getsearchuang(self.id_dntr,"jumlah_total",self.var_search.get())
                self.hasiluang(getrow)

            elif self.cmbox_search.get() == "Badan Donasi":
                getrow = dbriwayat.getsearchuang(self.id_dntr,"Badan_amal.nama",self.var_search.get())
                self.hasiluang(getrow)
        else : 
            
            if self.cmbox_search.get() == "Select" or self.var_search.get() == "":
                self.showbarang()

            elif self.cmbox_search.get() == "Id":
                getrow = dbriwayat.getsearchbarang(self.id_dntr,"Donatur.id",self.var_search.get())
                self.hasilbarang(getrow)
        
            elif self.cmbox_search.get() == "Jenis Donasi":
                getrow = dbriwayat.getsearchbarang(self.id_dntr,"Barang.jenis",self.var_search.get())
                self.hasilbarang(getrow)

            elif self.cmbox_search.get() == "Tanggal Donasi":
                getrow = dbriwayat.getsearchbarang(self.id_dntr,"Donasi.tgl_donasi",self.var_search.get())
                self.hasilbarang(getrow)
        
            elif self.cmbox_search.get() == "Jumlah Donasi":
                getrow = dbriwayat.getsearchbarang(self.id_dntr,"Barang.jumlah",self.var_search.get())
                self.hasilbarang(getrow)
            
            elif self.cmbox_search.get() == "Badan Donasi":
                getrow = dbriwayat.getsearchbarang(self.id_dntr,"Badan_amal.nama",self.var_search.get())
                self.hasilbarang(getrow)

    def gettabel(self,ev):
        if self.menu_cmb.get() == "UANG":
            dns_frame = Frame(self.window,bd=3,relief=RIDGE)
            dns_frame.place(x=0,y=140,width=700,height=420)
        
            scrolly = Scrollbar(dns_frame,orient=VERTICAL)
        
            self.TabelDonasi=ttk.Treeview(dns_frame,columns=("id_donasi","nama","jumlah","Tanggal","Badan"),yscrollcommand=scrolly.set)
            scrolly.pack(side=RIGHT,fill=Y)
            scrolly.config(command = self.TabelDonasi.yview)

            self.TabelDonasi.heading("id_donasi",text="ID")
            self.TabelDonasi.heading("nama",text="Nama Donatur")
            self.TabelDonasi.heading("jumlah",text="Jumlah Donasi")
            self.TabelDonasi.heading("Tanggal",text="Tanggal donasi")
            self.TabelDonasi.heading("Badan",text="Badan donasi")
            self.TabelDonasi["show"]="headings"
            self.TabelDonasi.pack(fill=BOTH,expand=1)

            self.TabelDonasi.column("id_donasi",width=30)
            self.TabelDonasi.column("nama",width=120)
            self.TabelDonasi.column("jumlah",width=100)
            self.TabelDonasi.column("Tanggal",width=120)
            self.TabelDonasi.column("Badan",width=90)
            self.showuang()
        else :
            dns_frame = Frame(self.window,bd=3,relief=RIDGE)
            dns_frame.place(x=0,y=140,width=700,height=420)
        
            scrolly = Scrollbar(dns_frame,orient=VERTICAL)
            self.TabelDonasi_barang=ttk.Treeview(dns_frame,columns=("id_donasi","nama","jenis","jumlah","Tanggal","Badan"),yscrollcommand=scrolly.set)
            scrolly.pack(side=RIGHT,fill=Y)
            scrolly.config(command = self.TabelDonasi_barang.yview)

            self.TabelDonasi_barang.heading("id_donasi",text="ID")
            self.TabelDonasi_barang.heading("nama",text="Nama Donatur")
            self.TabelDonasi_barang.heading("jenis",text="Jenis Donasi")
            self.TabelDonasi_barang.heading("jumlah",text="Jumlah Donasi")
            self.TabelDonasi_barang.heading("Tanggal",text="Tanggal donasi")
            self.TabelDonasi_barang.heading("Badan",text="Badan donasi")
            self.TabelDonasi_barang["show"]="headings"
            self.TabelDonasi_barang.pack(fill=BOTH,expand=1)

            self.TabelDonasi_barang.column("id_donasi",width=30)
            self.TabelDonasi_barang.column("nama",width=120)
            self.TabelDonasi_barang.column("jenis",width=90)
            self.TabelDonasi_barang.column("jumlah",width=100)
            self.TabelDonasi_barang.column("Tanggal",width=120)
            self.TabelDonasi_barang.column("Badan",width=90)
            self.showbarang()


def win (id_comp):
    window = Tk()
    Riwayat(window,id_comp)
    window.mainloop()
  
if __name__ == '__main__':
    win(1)