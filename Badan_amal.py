from tkinter import *
from tkinter import ttk,messagebox
from conector import Databasepegawai as dbpegawai
from conector import Databasekotakamal as dbkotak
from conector import DatabasePenerima as dbpenerima
from conector import DatabaseDonasi as dbdonasi
from conector import DatabaseDonatur as dbdonatur
import time

class Pegawai: 
    def __init__(self,window,id_comp):
        self.window = window
        self.window.geometry("1120x480+450+300")
        self.window.title("Pegawai")
        self.window.config(bg="white")

        #variabel
        self.var_cmbx_search = StringVar()
        self.var_search = StringVar()
        self.var_idcomp = id_comp
        self.var_nama = StringVar()
        self.var_id = StringVar()
        self.var_telp = StringVar()
        self.tanggal = StringVar()
        self.bulan = StringVar()
        self.tahun = StringVar()
        self.date = str()
        self.tampilan()
        print(self.var_idcomp)

    def tampilan(self):

        #seach  
        Searchframe=LabelFrame(self.window,text="Search Peagwai",bg="white")
        Searchframe.place(x=50,y=20,width=520,height=70)

        cmb_search=ttk.Combobox(Searchframe,textvariable=self.var_cmbx_search,values=("Select","Nama","Id","Tanggal Masuk"),state='readonly')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        search_data = Entry(Searchframe,textvariable=self.var_search)
        search_data.place(x=200,y=10,width=180,height=30)

        submit_search = Button(Searchframe,command=self.submit_search,text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
        submit_search.place(x=400,y=10,width=90,height = 30)
        

        #input
        inputframe=LabelFrame(self.window,text="Input Pegawai",bg="white")
        inputframe.place(x=50,y=100,width=520,height=350)
        
        lbl_id_pegawai = Label(inputframe,text = "ID Pegawai",bg="white").place(x = 10,y = 20)
        id_pegawai = Entry(inputframe,textvariable=self.var_id).place(x=120,y=20)

        nama = Label(inputframe,text = "Nama Pegawai",bg="white").place(x = 10,y = 60)
        nama_input = Entry(inputframe,textvariable=self.var_nama).place(x=120,y=60)

        no_telepon= Entry(inputframe,textvariable=self.var_telp).place(x=120,y=100)
        lbl_no_telepon = Label(inputframe,text = "No Telephon",bg="white").place(x = 10,y = 100)

        lbl_tgl_masuk = Label(inputframe,text = "Tanggal Masuk",bg="white").place(x = 10,y = 140)
        tanggal = Entry(inputframe,textvariable=self.tanggal,width=4).place(x=120,y=140)
        self.tanggal.set("dd")
        bulan = Entry(inputframe,textvariable=self.bulan,width=4).place(x=170,y=140)
        self.bulan.set("mm")
        bulan = Entry(inputframe,textvariable=self.tahun,width=7).place(x=220,y=140)
        self.tahun.set("yyyy")

        #perbutonnans

        submit = Button (inputframe,text = "Submit",bg="green",fg ="white",command =self.submit,font=("times new roman",12,"bold"))
        submit.place(x=200,y=200)

        update = Button (inputframe,text = "Update",bg="blue",fg ="white",command=self.update,font=("times new roman",12,"bold"))
        update.place(x=300,y=200)

        delete = Button (inputframe,text = "Delete",bg="red",fg ="white",command=self.delete,font=("times new roman",12,"bold"))
        delete.place(x=400,y=200)

        #tabel
        title=Label(self.window,text = "Data Pegawai",font=("times new roman",20,"bold"),bg = "white",fg = "black").place(x = 600 , y = 30,height=50)
        pgw_frame = Frame(self.window,bd=3,relief=RIDGE)
        pgw_frame.place(x=600,y=80,width=500,height=350)

        scrolly = Scrollbar(pgw_frame,orient=VERTICAL)

        self.TabelPegawai=ttk.Treeview(pgw_frame,columns=("id_pegawai","nama","telp","tgl_masuk","experience"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command = self.TabelPegawai.yview)
        self.TabelPegawai.heading("id_pegawai",text="ID")
        self.TabelPegawai.heading("nama",text="Nama Pegawai")
        self.TabelPegawai.heading("telp",text="No Telepon")
        self.TabelPegawai.heading("tgl_masuk",text="Tanggal Masuk")
        self.TabelPegawai.heading("experience",text="experience")
        self.TabelPegawai["show"]="headings"
        self.TabelPegawai.pack(fill=BOTH,expand=1)
        self.TabelPegawai.bind("<ButtonRelease-1>",self.get_data)

        self.TabelPegawai.column("id_pegawai",width=30)
        self.TabelPegawai.column("nama",width=120)
        self.TabelPegawai.column("telp",width=120)
        self.TabelPegawai.column("tgl_masuk",width=120)
        self.TabelPegawai.column("experience",width=80)
        self.show()

    def submit_search(self):
        if self.var_cmbx_search.get() == "Select" or self.var_search.get() == "":
            self.show()
        elif self.var_cmbx_search.get() == "Nama":
            getrow = dbpegawai.getsearch(self.var_idcomp,"nama",self.var_search.get())
            self.TabelPegawai.delete(*self.TabelPegawai.get_children())
            for row in getrow:
                self.TabelPegawai.insert('',END,values=row)

        elif self.var_cmbx_search.get() == "Id":
            
            getrow = dbpegawai.getsearch(self.var_idcomp,"id_pegawai",self.var_search.get())
            self.TabelPegawai.delete(*self.TabelPegawai.get_children())
            for row in getrow:
                self.TabelPegawai.insert('',END,values=row)
        elif self.var_cmbx_search.get() == "Tanggal Masuk":

            getrow = dbpegawai.getsearch(self.var_idcomp,"tgl_masuk",self.var_search.get())
            self.TabelPegawai.delete(*self.TabelPegawai.get_children())
            for row in getrow:
                self.TabelPegawai.insert('',END,values=row)

    def submit(self):
        self.date = str(self.tahun.get()) + '-' + str(self.bulan.get()) + '-' + str(self.tanggal.get())
        if(self.var_id.get() == "" or self.var_nama.get() == "" or self.var_telp.get() == ""):
            messagebox.showwarning("Warning","Isi Semua Data!",parent=self.window)
        else :
            if dbpegawai.cekprimary(self.var_id.get()):
                messagebox.showerror("Error","ID Pegawai sudah ada")
            else :
                if len(self.var_nama.get()) > 30:
                    messagebox.showerror("Error","nama terlalu panjang")
                elif len(self.var_telp.get()) > 13:
                    messagebox.showerror("Error","Nomor Handpone terlalu panjang")
                elif len(self.var_id.get()) > 6:
                    messagebox.showerror("Error","Id terlalu panjang")
                elif len(self.date) > 10:
                    messagebox.showerror("Error","Tanggal Invalid")
                else : 
                    dbpegawai.insert(self.var_id.get(),self.var_nama.get(),self.var_telp.get(),self.date,self.var_idcomp)
                    messagebox.showinfo("Info","Data berhasil dimasukkan")
                    self.show()
                    self.clear()
        
    def clear(self):
        self.var_id.set("")
        self.var_nama.set("")
        self.var_telp.set("")
        self.tanggal.set("dd")
        self.bulan.set("mm")
        self.tahun.set("yyyy")

    def show(self):
        getrow = dbpegawai.getdata(self.var_idcomp)
        self.TabelPegawai.delete(*self.TabelPegawai.get_children())
        for row in getrow:
            self.TabelPegawai.insert('',END,values=row)
    
    def get_data(self,ev):
        f=self.TabelPegawai.focus()
        content=(self.TabelPegawai.item(f))
        row = content['values']
        self.var_id.set(row[0])
        self.var_nama.set(row[1])
        self.var_telp.set("0" + str(row[2]))
        temp = row[3].split("-")
        self.tanggal.set(temp[2])
        self.bulan.set(temp[1])
        self.tahun.set(temp[0])

    def update(self):
        if(self.var_id.get() == ""):
            messagebox.showwarning("Warning","Data Primary belum diisi !",parent=self.window)
        else :
            if not dbpegawai.cekprimary(self.var_id.get()):
                messagebox.showerror("Error","ID Pegawai belum ada")
            else :
                dbpegawai.update(self.var_id.get(),self.var_nama.get(),self.var_telp.get())
                messagebox.showinfo("Info","Data berhasil diupdate")
                self.show()
                self.clear()

    def delete(self):
        if(not self.var_id.get() == ""):
            if dbpegawai.cekprimary(self.var_id.get()):
                pilih = messagebox.askyesno("Delete data", "Apakah Kamu yakin untuk menghapus data dengan id "+self.var_id.get()+"?")
                if pilih:
                    dbpegawai.delete_data(self.var_id.get())
                    self.show()
                    self.clear()
                else:
                    pass
            else :
                messagebox.showerror("Error","ID Pegawai belum ada")
        else : 
            messagebox.showwarning("Warning","Data belum diisi !",parent=self.window)

class Kotak_amal: 
    def __init__(self,window,id_comp):
        self.window = window
        self.window.geometry("1120x480+450+300")
        self.window.title("Kotak Amal")
        self.window.config(bg="white")

        #variabel
        self.var_idkotak= StringVar()
        self.var_id_company = id_comp
        self.var_id_pegawai = StringVar()
        self.get_search = StringVar()
        self.get_isi_search = StringVar()
        self.var_alamat = StringVar()
        self.var_jumlah = StringVar()
        date = time.strftime('%Y%m%d')
        year = date[0:4]
        mount = date[4:6]
        day = date[6:8]
        self.date = str(year) + "-" + str(mount) + "-" +str(day)
        self.tampilan()

    def tampilan(self):

        #seach  
        Searchframe=LabelFrame(self.window,text="Search Kotak Amal",bg="white")
        Searchframe.place(x=50,y=20,width=520,height=70)

        cmb_search=ttk.Combobox(Searchframe,textvariable = self.get_search,values=("Select","Nama Pegawai","Id Kotak","Tanggal","Alamat"),state='readonly')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        search_data = Entry(Searchframe,textvariable = self.get_isi_search)
        search_data.place(x=200,y=10,width=180,height=30)

        submit_search = Button(Searchframe,text="Search",command = self.getsearch,bg="blue",fg="white",font=("times new roman",12,"bold"))
        submit_search.place(x=400,y=10,width=90,height = 30)

        #input
        inputframe=LabelFrame(self.window,text="Input Kotak Amal",bg="white")
        inputframe.place(x=50,y=100,width=520,height=350)
        
        lbl_id_kotakamal = Label(inputframe,text = "ID Kotak Amal",bg="white").place(x = 10,y = 20)
        id_id_kotakamal = Entry(inputframe,textvariable=self.var_idkotak).place(x=120,y=20)

        lbl_id_pegawai = Label(inputframe,text = "Id Pegawai",bg="white").place(x = 10,y = 60)
        input_id_pegawai = Entry(inputframe,textvariable=self.var_id_pegawai).place(x=120,y=60)

        Alamat = Label(inputframe,text = "alamat",bg="white").place(x = 10,y = 100)
        alamt_input = Entry(inputframe,textvariable=self.var_alamat).place(x=120,y=100)

        Uang = Label(inputframe,text = "Jumlah Uang",bg="white").place(x = 10,y = 140)
        Jumlah_input = Entry(inputframe,textvariable=self.var_jumlah).place(x=120,y=140)


        #perbutonnan

        submit = Button (inputframe,command = self.Submit,text = "Submit",bg="green",fg ="white",font=("times new roman",12,"bold"))
        submit.place(x=200,y=200)

        update = Button (inputframe,command = self.Update,text = "Update",bg="blue",fg ="white",font=("times new roman",12,"bold"))
        update.place(x=300,y=200)

        delete = Button (inputframe,command = self.Delete,text = "Delete",bg="red",fg ="white",font=("times new roman",12,"bold"))
        delete.place(x=400,y=200)

        #tabel
        title=Label(self.window,text = "Data Kotak Amal",font=("times new roman",20,"bold"),bg = "white",fg = "black").place(x = 600 , y = 30,height=50)
        pgw_frame = Frame(self.window,bd=3,relief=RIDGE)
        pgw_frame.place(x=600,y=80,width=500,height=350)

        scrolly = Scrollbar(pgw_frame,orient=VERTICAL)
        scrollx = Scrollbar(pgw_frame,orient=HORIZONTAL)

        self.TabelKotakAmal=ttk.Treeview(pgw_frame,columns=("id_kotak","id_pegawai","nama","alamat","jumlah","tanggal"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command = self.TabelKotakAmal.xview)
        scrolly.config(command = self.TabelKotakAmal.yview)
        self.TabelKotakAmal.heading("id_kotak",text="ID")
        self.TabelKotakAmal.heading("id_pegawai",text="ID Pegawai")
        self.TabelKotakAmal.heading("nama",text="Nama Pegawai")
        self.TabelKotakAmal.heading("alamat",text="Alamat")
        self.TabelKotakAmal.heading("jumlah",text="Jumlah")
        self.TabelKotakAmal.heading("tanggal",text="Tangal")
        self.TabelKotakAmal["show"]="headings"
        self.TabelKotakAmal.pack(fill=BOTH,expand=1)
        self.TabelKotakAmal.bind("<ButtonRelease-1>",self.get_data)

        self.TabelKotakAmal.column("id_kotak",width=30)
        self.TabelKotakAmal.column("id_pegawai",width=100)
        self.TabelKotakAmal.column("nama",width=120)
        self.TabelKotakAmal.column("alamat",width=400)
        self.TabelKotakAmal.column("jumlah",width=150)
        self.TabelKotakAmal.column("tanggal",width=100)
        

        self.show()
    
    def Submit(self):   
        if(self.var_idkotak.get() == ""):
            messagebox.showwarning("Warning","Isi Semua Data!",parent=self.window)
        else :
            if dbkotak.cekprimary(self.var_idkotak.get()):
                messagebox.showerror("Error","ID Kotak sudah ada")
            elif not dbpegawai.cekprimary(self.var_id_pegawai.get()):
                messagebox.showerror("Error","ID Pegawai Tidak ada ada")
            else :
                dbkotak.insert(self.var_idkotak.get(),self.var_id_company,self.var_id_pegawai.get(),self.var_alamat.get(),self.var_jumlah.get(),self.date)
                messagebox.showinfo("Info","Data berhasil dimasukkan")
                self.show()
                self.clear()

    def clear(self):
        self.var_idkotak.set("")
        self.var_id_pegawai.set("")
        self.var_alamat.set("")
        self.var_jumlah.set("")
    
    def Update(self):
        if self.var_idkotak.get() == "":
            messagebox.showwarning("Warning","Data Primary Harus diisi !",parent=self.window)
        else :
            if not dbkotak.cekprimary(self.var_idkotak.get()):
                messagebox.showerror("Error","ID Kotak belum ada")
            else :
                dbkotak.update(self.var_idkotak.get(),self.var_id_pegawai.get(),self.var_alamat.get(),self.var_jumlah.get())
                messagebox.showinfo("Info","Data berhasil diupdate")
                self.show()
                self.clear()
                
    def Delete(self):
        if not self.var_idkotak.get() == "":
            if dbkotak.cekprimary(self.var_idkotak.get()):
                pilih = messagebox.askyesno("Delete data", "Apakah Kamu yakin untuk menghapus data dengan id "+self.var_idkotak.get()+"?")
                if pilih:
                    dbkotak.delete_data(self.var_idkotak.get())
                    self.show()
                    self.clear()
                else:
                    pass
            else :
                messagebox.showerror("Error","ID Kotak tidak ada")
        else : 
            messagebox.showwarning("Warning","Data belum diisi !",parent=self.window)

    def show(self):
        getrow = dbkotak.getdata(self.var_id_company)
        self.TabelKotakAmal.delete(*self.TabelKotakAmal.get_children())
        for row in getrow:
            self.TabelKotakAmal.insert('',END,values=row)

    def getsearch(self):
        if self.get_search.get() == "Select" or self.get_isi_search.get() == "":
            self.show()

        elif self.get_search.get() =="Nama Pegawai":
            getrow = dbkotak.getsearch(self.var_id_company,"nama",self.get_isi_search.get())
            self.hasilsearch(getrow)

        elif self.get_search.get() =="Id Kotak":
            getrow = dbkotak.getsearch(self.var_id_company,"id_pegawai",self.get_isi_search.get())
            self.hasilsearch(getrow)

        elif self.get_search.get() == "Tanggal":
            getrow = dbkotak.getsearch(self.var_id_company,"tgl_penarikan",self.get_isi_search.get())
            self.hasilsearch(getrow)
        
        elif self.get_search.get() == "Alamat":
            getrow = dbkotak.getsearch(self.var_id_company,"alamat",self.get_isi_search.get())
            self.hasilsearch(getrow)
            
    def hasilsearch(self,getrow):
        self.TabelKotakAmal.delete(*self.TabelKotakAmal.get_children())
        for row in getrow:
            self.TabelKotakAmal.insert('',END,values=row)
  
    def get_data(self,ev):
        f=self.TabelKotakAmal.focus()
        content=(self.TabelKotakAmal.item(f))
        row = content['values']
        self.var_idkotak.set(row[0])
        self.var_id_pegawai.set(row[1])
        self.var_alamat.set(row[3])
        self.var_jumlah.set(row[4])

class Penerima: 

    def __init__(self,window,id_comp):
        self.window = window
        self.window.geometry("1120x480+450+300")
        self.window.title("Penerima")
        self.window.config(bg="white")

        #variabel
        self.id_comp = id_comp
        self.id_pegawai = StringVar()
        self.id_penerima = 0
        self.nama_penerima = StringVar()
        self.var_alamat = StringVar()
        self.var_telp = StringVar()
        self.var_telp2 = StringVar()
        self.var_search = StringVar()
        self.cmbox_search = StringVar()
        self.tampilan()

    def tampilan(self):

        #seach  
        Searchframe=LabelFrame(self.window,text="Search Penerima",bg="white")
        Searchframe.place(x=50,y=20,width=520,height=70)

        cmb_search=ttk.Combobox(Searchframe,textvariable = self.cmbox_search,values=("Select","Nama Pegawai","Nama Penerima","Alamat","No Telepon","Id Penerima"),state='readonly')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        search_data = Entry(Searchframe,textvariable = self.var_search)
        search_data.place(x=200,y=10,width=180,height=30)

        submit_search = Button(Searchframe,command = self.getsearch, text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
        submit_search.place(x=400,y=10,width=90,height = 30)

        #input
        inputframe=LabelFrame(self.window,text="Input Penerima",bg="white")
        inputframe.place(x=50,y=100,width=520,height=350)
        
        lblnamapenerima = Label(inputframe,text = "ID Pegawai",bg="white").place(x = 10,y = 20)
        input_namapenerima = Entry(inputframe,textvariable=self.id_pegawai).place(x=120,y=20)

        lbl_alamat = Label(inputframe,text = "Nama",bg="white").place(x = 10,y = 60)
        input_alamat = Entry(inputframe,textvariable=self.nama_penerima).place(x=120,y=60)

        lbl_no_telepon = Label(inputframe,text = "Alamat",bg="white").place(x = 10,y = 100)
        input_no_telepon = Entry(inputframe,textvariable=self.var_alamat).place(x=120,y=100)

        lblnamapenerima = Label(inputframe,text = "No Telepon 1",bg="white").place(x = 10,y = 140)
        input_namapenerima = Entry(inputframe,textvariable=self.var_telp).place(x=120,y=140)

        lblnamapenerima = Label(inputframe,text = "No Telepon 2",bg="white").place(x = 10,y = 180)
        input_namapenerima = Entry(inputframe,textvariable=self.var_telp2).place(x=120,y=180)

        #perbutonnan

        submit = Button (inputframe,command = self.Submit,text = "Submit",bg="green",fg ="white",font=("times new roman",12,"bold"))
        submit.place(x=200,y=250)

        update = Button (inputframe,command = self.Update,text = "Update",bg="blue",fg ="white",font=("times new roman",12,"bold"))
        update.place(x=300,y=250)

        delete = Button (inputframe,command = self.Delete,text = "Delete",bg="red",fg ="white",font=("times new roman",12,"bold"))
        delete.place(x=400,y=250)

        #tabel
        title=Label(self.window,text = "Data Penerima",font=("times new roman",20,"bold"),bg = "white",fg = "black").place(x = 600 , y = 30,height=50)
        pgw_frame = Frame(self.window,bd=3,relief=RIDGE)
        pgw_frame.place(x=600,y=80,width=500,height=350)

        scrolly = Scrollbar(pgw_frame,orient=VERTICAL)
        scrollx = Scrollbar(pgw_frame,orient=HORIZONTAL)

        self.TabelPenerima=ttk.Treeview(pgw_frame,columns=("id_penerima","nama_pegawai","nama_penerima","alamat","no_telp","no_telp2"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command = self.TabelPenerima.xview)
        scrolly.config(command = self.TabelPenerima.yview)
        self.TabelPenerima.heading("id_penerima",text="ID")
        self.TabelPenerima.heading("nama_pegawai",text="Nama Pegawai")
        self.TabelPenerima.heading("nama_penerima",text="Nama Penerima")
        self.TabelPenerima.heading("alamat",text="Alamat")
        self.TabelPenerima.heading("no_telp",text="No Telepon1")
        self.TabelPenerima.heading("no_telp2",text="No Telepon2")
        self.TabelPenerima["show"]="headings"
        self.TabelPenerima.pack(fill=BOTH,expand=1)
        self.TabelPenerima.bind("<ButtonRelease-1>",self.get_data)

        self.TabelPenerima.column("id_penerima",width=30)
        self.TabelPenerima.column("nama_pegawai",width=130)
        self.TabelPenerima.column("nama_penerima",width=150)
        self.TabelPenerima.column("alamat",width=400)
        self.TabelPenerima.column("no_telp",width=150)
        self.TabelPenerima.column("no_telp2",width=150)

        self.show()

    def Submit(self):
        if self.id_pegawai.get() == "" or self.nama_penerima.get() == "" or self.var_alamat.get() == "" or self.var_telp.get() == "":
            messagebox.showwarning("warning","Isi data dengan lengkap")
        else :
            if len(self.nama_penerima.get()) > 20:
                messagebox.showerror("Error","Nama Terlalu Panjang")
            else : 
                dbpenerima.insert(self.id_pegawai.get(),self.id_comp,self.nama_penerima.get(),self.var_alamat.get(),self.var_telp.get(),self.var_telp2.get())
                self.clear()
                messagebox.showinfo("Info","Data berhasil dimasukan")
                self.show()

    def show(self):
        getrow = dbpenerima.getdata(self.id_comp)
        self.TabelPenerima.delete(*self.TabelPenerima.get_children())
        for row in getrow:
            self.TabelPenerima.insert('',END,values=row)
    
    def clear(self):
        self.id_pegawai.set("") 
        self.nama_penerima.set("") 
        self.var_alamat.set("") 
        self.var_telp.set("") 
        self.var_telp2.set("") 

    def get_data(self,ev):
        f=self.TabelPenerima.focus()
        content=(self.TabelPenerima.item(f))
        row = content['values']
        self.id_pegawai.set(dbpenerima.search_nama(row[1],self.id_comp))
        self.nama_penerima.set(row[2])
        self.var_alamat.set(row[3])
        self.var_telp.set("0"+str(row[4]))
        self.var_telp2.set("0"+str(row[5]))
    
    def Update(self):
        if(self.nama_penerima == ""):
            messagebox.showwarning("Warning","Data belum diisi !",parent=self.window)
        else :
            self.id_penerima = dbpenerima.getprimary(self.nama_penerima.get())
            if not dbpenerima.cekprimary(self.id_penerima):
                messagebox.showerror("Error","ID Penerima belum ada")
            else :
                dbpenerima.update(self.id_penerima[0],self.id_pegawai.get(),self.id_comp,self.nama_penerima.get(),self.var_alamat.get(),self.var_telp.get(),self.var_telp2.get())
                messagebox.showinfo("Info","Data berhasil diupdate")
                self.show()
                self.clear()

    def Delete(self):
        if(not self.nama_penerima.get() == ""):
            self.id_penerima = dbpenerima.getprimary(self.nama_penerima.get())
            if dbpenerima.cekprimary(self.id_penerima):
                pilih = messagebox.askyesno("Delete data", "Apakah Kamu yakin untuk menghapus data "+self.nama_penerima.get()+"?")
                if pilih:
                    dbpenerima.delete(self.id_penerima)
                    self.show()
                    self.clear()
                else:
                    pass
            else :
                messagebox.showerror("Error","ID Penerima belum ada")
        else : 
            messagebox.showwarning("Warning","Data belum diisi !",parent=self.window)

    def getsearch(self):
        if self.cmbox_search.get() == "Select" or self.var_search.get() == "":
            self.show()

        elif self.cmbox_search.get() =="Nama Pegawai":
            getrow = dbpenerima.getsearch(self.id_comp,"Pegawai.nama",self.var_search.get())
            self.hasilsearch(getrow)

        elif self.cmbox_search.get() =="Nama Penerima":
            getrow = dbpenerima.getsearch(self.id_comp,"Penerima.nama",self.var_search.get())
            self.hasilsearch(getrow)

        elif self.cmbox_search.get() == "Alamat":
            getrow = dbpenerima.getsearch(self.id_comp,"Penerima.alamat",self.var_search.get())
            self.hasilsearch(getrow)
        
        elif self.cmbox_search.get() == "No Telepon":
            getrow = dbpenerima.getsearch(self.id_comp,"nomor_hp",self.var_search.get())
            self.hasilsearch(getrow)
        
        elif self.cmbox_search.get() == "Id Penerima":
            getrow = dbpenerima.getsearch(self.id_comp,"id_penerima",self.var_search.get())
            self.hasilsearch(getrow)
            
    def hasilsearch(self,getrow):
        self.TabelPenerima.delete(*self.TabelPenerima.get_children())
        for row in getrow:
            self.TabelPenerima.insert('',END,values=row)

class Donasi:

    def __init__(self,window,id_comp):
        self.window = window
        self.window.geometry("700x600+600+350")
        self.window.title("Donasi")
        self.window.resizable (False,False)
        self.window.config(bg="white")
        self.id_comp = id_comp
        self.cmbox_search = StringVar()
        self.var_search = StringVar()

        title  = Label(self.window,text = "Laporan Donasi",font=("times new roman",30,"bold"),bg = "#010c48",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 50)

        Searchframe=LabelFrame(self.window,text="Search Donasi",bg="white")
        Searchframe.place(x=180,y=70,width=520,height=70)

        cmb_search=ttk.Combobox(Searchframe,values=("Select","Nama","Id","Jenis Donasi","Tanggal Donasi","Jumlah Donasi"),textvariable = self.cmbox_search,state='readonly')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        self.menu_cmb=ttk.Combobox(self.window,values=("UANG","BARANG"))
        self.menu_cmb.place(x=20,y=90,width=90,height=30)
        self.menu_cmb.current(0)
        self.menu_cmb.bind("<<ComboboxSelected>>", self.gettabel)

        search_data = Entry(Searchframe,textvariable = self.var_search)
        search_data.place(x=200,y=10,width=180,height=30)

        submit_search = Button(Searchframe,command=self.getsearch,text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
        submit_search.place(x=400,y=10,width=90,height = 30)

        
    def showuang(self):
        getrow = dbdonasi.getdata(self.id_comp)
        self.TabelDonasi.delete(*self.TabelDonasi.get_children())
        for row in getrow:
            self.TabelDonasi.insert('',END,values=row)
    
    def showbarang(self):
        getrow = dbdonasi.getdatabarang(self.id_comp)
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
                getrow = dbdonasi.getsearchuang(self.id_comp,"Donasi.id_donasi",self.var_search.get())
                self.hasiluang(getrow)

            elif self.cmbox_search.get() == "Nama":
                getrow = dbdonasi.getsearchuang(self.id_comp,"Donatur.nama",self.var_search.get())
                self.hasiluang(getrow)
            
            elif self.cmbox_search.get() == "Jumlah Donasi":
                getrow = dbdonasi.getsearchuang(self.id_comp,"jumlah_total",self.var_search.get())
                self.hasiluang(getrow)

            elif self.cmbox_search.get() == "Tanggal Donasi":
                getrow = dbdonasi.getsearchuang(self.id_comp,"tgl_donasi",self.var_search.get())
                self.hasiluang(getrow)
        else : 
            
            if self.cmbox_search.get() == "Select" or self.var_search.get() == "":
                self.showbarang()
            elif self.cmbox_search.get() == "Nama":
                getrow = dbdonasi.getsearchbarang(self.id_comp,"Donatur.nama",self.var_search.get())
                self.hasilbarang(getrow)
            elif self.cmbox_search.get() == "Id":
                getrow = dbdonasi.getsearchbarang(self.id_comp,"Donasi.id_donasi",self.var_search.get())
                self.hasilbarang(getrow)
        
            elif self.cmbox_search.get() == "Jenis Donasi":
                getrow = dbdonasi.getsearchbarang(self.id_comp,"Barang.jenis",self.var_search.get())
                self.hasilbarang(getrow)

            elif self.cmbox_search.get() == "Tanggal Donasi":
                getrow = dbdonasi.getsearchbarang(self.id_comp,"Donasi.tgl_donasi",self.var_search.get())
                self.hasilbarang(getrow)
        
            elif self.cmbox_search.get() == "Jumlah Donasi":
                getrow = dbdonasi.getsearchbarang(self.id_comp,"Barang.jumlah",self.var_search.get())
                self.hasilbarang(getrow)

    def gettabel(self,ev):
        if self.menu_cmb.get() == "UANG":
            dns_frame = Frame(self.window,bd=3,relief=RIDGE)
            dns_frame.place(x=0,y=140,width=700,height=420)
        
            scrolly = Scrollbar(dns_frame,orient=VERTICAL)
        
            self.TabelDonasi=ttk.Treeview(dns_frame,columns=("id_donasi","nama","jumlah","Tanggal"),yscrollcommand=scrolly.set)
            scrolly.pack(side=RIGHT,fill=Y)
            scrolly.config(command = self.TabelDonasi.yview)

            self.TabelDonasi.heading("id_donasi",text="ID")
            self.TabelDonasi.heading("nama",text="Nama Donatur")
            self.TabelDonasi.heading("jumlah",text="Jumlah Donasi")
            self.TabelDonasi.heading("Tanggal",text="Tanggal donasi")
            self.TabelDonasi["show"]="headings"
            self.TabelDonasi.pack(fill=BOTH,expand=1)

            self.TabelDonasi.column("id_donasi",width=30)
            self.TabelDonasi.column("nama",width=120)
            self.TabelDonasi.column("jumlah",width=100)
            self.TabelDonasi.column("Tanggal",width=120)
            self.showuang()
        else :
            dns_frame = Frame(self.window,bd=3,relief=RIDGE)
            dns_frame.place(x=0,y=140,width=700,height=420)
        
            scrolly = Scrollbar(dns_frame,orient=VERTICAL)
            self.TabelDonasi_barang=ttk.Treeview(dns_frame,columns=("id_donasi","nama","jenis","jumlah","Tanggal"),yscrollcommand=scrolly.set)
            scrolly.pack(side=RIGHT,fill=Y)
            scrolly.config(command = self.TabelDonasi_barang.yview)

            self.TabelDonasi_barang.heading("id_donasi",text="ID")
            self.TabelDonasi_barang.heading("nama",text="Nama Donatur")
            self.TabelDonasi_barang.heading("jenis",text="Jenis Donasi")
            self.TabelDonasi_barang.heading("jumlah",text="Jumlah Donasi")
            self.TabelDonasi_barang.heading("Tanggal",text="Tanggal donasi")
            self.TabelDonasi_barang["show"]="headings"
            self.TabelDonasi_barang.pack(fill=BOTH,expand=1)

            self.TabelDonasi_barang.column("id_donasi",width=30)
            self.TabelDonasi_barang.column("nama",width=120)
            self.TabelDonasi_barang.column("jenis",width=90)
            self.TabelDonasi_barang.column("jumlah",width=100)
            self.TabelDonasi_barang.column("Tanggal",width=120)
            self.showbarang()

class Donatur: 
    def __init__(self,window,id_comp):
        self.window = window
        self.window.geometry("700x600+600+300")
        self.window.title("Donasi")
        self.window.resizable (False,False)
        self.window.config(bg="white")
        self.var_search = StringVar()
        self.cmbox_search = StringVar()
        self.id_comp = id_comp

        title  = Label(self.window,text = "Donatur",font=("times new roman",30,"bold"),bg = "green",fg = "white").place(x = 0, y = 0,relwidth = 1,height = 50)

        Searchframe=LabelFrame(self.window,text="Search Donasi",bg="white")
        Searchframe.place(x=180,y=70,width=520,height=70)

        cmb_search=ttk.Combobox(Searchframe,textvariable = self.cmbox_search,values=("Select","Nama","Username","Alamat","No Telepon","Tipe"),state='readonly')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        search_data = Entry(Searchframe,textvariable = self.var_search)
        search_data.place(x=200,y=10,width=180,height=30)

        submit_search = Button(Searchframe,command = self.getsearch,text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
        submit_search.place(x=400,y=10,width=90,height = 30)

        dns_frame = Frame(self.window,bd=3,relief=RIDGE)
        dns_frame.place(x=0,y=140,width=700,height=420)
        
        scrolly = Scrollbar(dns_frame,orient=VERTICAL)
        scrollx = Scrollbar(dns_frame,orient=HORIZONTAL)
        
        self.TabelDonatur=ttk.Treeview(dns_frame,columns=("id_donatur","nama","username","alamat","no_telepon","tipe"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.config(command = self.TabelDonatur.yview)
        scrollx.config(command = self.TabelDonatur.xview)

        self.TabelDonatur.heading("id_donatur",text="ID")
        self.TabelDonatur.heading("nama",text="Nama")
        self.TabelDonatur.heading("username",text="username")
        self.TabelDonatur.heading("alamat",text="Alamat Donatur")
        self.TabelDonatur.heading("no_telepon",text="no_telepon")
        self.TabelDonatur.heading("tipe",text="tipe")
        self.TabelDonatur["show"]="headings"
        self.TabelDonatur.pack(fill=BOTH,expand=1)

        self.TabelDonatur.column("id_donatur",width=30)
        self.TabelDonatur.column("nama",width=120)
        self.TabelDonatur.column("username",width=120)
        self.TabelDonatur.column("alamat",width=190)
        self.TabelDonatur.column("no_telepon",width=120)
        self.TabelDonatur.column("tipe",width=90)
        self.show()

    def show(self):
        getrow = dbdonatur.getdata(self.id_comp)
        self.TabelDonatur.delete(*self.TabelDonatur.get_children())
        for row in getrow:
            self.TabelDonatur.insert('',END,values=row)

    def getsearch(self):
        if self.cmbox_search.get() == "Select" or self.var_search.get() == "":
            self.show()

        elif self.cmbox_search.get() == "Nama":
            getrow = dbdonatur.getsearch(self.id_comp,"Donatur.nama",self.var_search.get())
            self.hasilsearch(getrow)

        elif self.cmbox_search.get() == "Username":
            getrow = dbdonatur.getsearch(self.id_comp,"Donatur.username",self.var_search.get())
            self.hasilsearch(getrow)

        elif self.cmbox_search.get() == "Alamat":
            getrow = dbdonatur.getsearch(self.id_comp,"Donatur.alamat",self.var_search.get())
            self.hasilsearch(getrow)
        
        elif self.cmbox_search.get() == "No Telepon":
            getrow = dbdonatur.getsearch(self.id_comp,"Donatur.no_telepon",self.var_search.get())
            self.hasilsearch(getrow)
        
        elif self.cmbox_search.get() == "Tipe":
            getrow = dbdonatur.getsearch(self.id_comp,"Donatur.tipe",self.var_search.get())
            self.hasilsearch(getrow)

    def hasilsearch(self,getrow): 
        self.TabelDonatur.delete(*self.TabelDonatur.get_children())
        for row in getrow:
            self.TabelDonatur.insert('',END,values=row)

def start ():
    window = Tk()
    Donasi(window,1)
    window.mainloop()
  
if __name__ == '__main__':
    start()