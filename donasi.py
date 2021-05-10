from tkinter import *
from tkinter import ttk, messagebox
from conector import donasi_uang
from conector import donasi_barang as dbdonasi_barang

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

        title  = Label(self.window,text = "Riwayat Donasi",font=("times new roman",30,"bold"),bg = "green",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 50)

        Searchframe=LabelFrame(self.window,text="Search Donasi",bg="white")
        Searchframe.place(x=180,y=70,width=520,height=70)

        cmb_search=ttk.Combobox(Searchframe,values=("Select","Nama","Id","Tanggal Masuk"),state='readonly')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        search_data = Entry(Searchframe)
        search_data.place(x=200,y=10,width=180,height=30)

        submit_search = Button(Searchframe,text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
        submit_search.place(x=400,y=10,width=90,height = 30)

        dns_frame = Frame(self.window,bd=3,relief=RIDGE)
        dns_frame.place(x=0,y=140,width=700,height=420)

        scrolly = Scrollbar(dns_frame,orient=VERTICAL)
        
        self.TabelDonasi=ttk.Treeview(dns_frame,columns=("id_donasi","nama","jenis","jumlah","Tanggal","Badan"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command = self.TabelPegawai.yview)
        self.TabelDonasi.heading("id_donasi",text="ID")
        self.TabelDonasi.heading("nama",text="Nama Donatur")
        self.TabelDonasi.heading("jenis",text="Jenis Donasi")
        self.TabelDonasi.heading("jumlah",text="Jumlah Donasi")
        self.TabelDonasi.heading("Tanggal",text="Tanggal donasi")
        self.TabelDonasi.heading("Badan",text="Badan donasi")
        self.TabelDonasi["show"]="headings"
        self.TabelDonasi.pack(fill=BOTH,expand=1)

        self.TabelDonasi.column("id_donasi",width=30)
        self.TabelDonasi.column("nama",width=120)
        self.TabelDonasi.column("jenis",width=90)
        self.TabelDonasi.column("jumlah",width=100)
        self.TabelDonasi.column("Tanggal",width=120)
        self.TabelDonasi.column("Badan",width=90)
        self.show()

    def show():



def win (id_comp):
    window = Tk()
    donasi_barang(window,id_comp)
    window.mainloop()
  
if __name__ == '__main__':
    win(1)