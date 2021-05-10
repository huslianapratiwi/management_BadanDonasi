from tkinter import *
from tkinter import ttk,messagebox
from conector import Databasepegawai as dbpegawai
from conector import Databasekotakamal as dbkotak
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
        self.var_search
        self.var_cmbx_search
        getrow = dbpegawai.getsearch(self.var_idcomp)
        self.TabelPegawai.delete(*self.TabelPegawai.get_children())
        for row in getrow:
            self.TabelPegawai.inser


    def submit(self):
        self.date = str(self.tahun.get()) + '-' + str(self.bulan.get()) + '-' + str(self.tanggal.get())
        if(self.var_id.get() == "" or self.var_nama.get() == "" or self.var_telp.get() == ""):
            messagebox.showwarning("Warning","Isi Semua Data!",parent=self.window)
        else :
            if dbpegawai.cekprimary(self.var_id.get()):
                messagebox.showerror("Error","ID Pegawai sudah ada")
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
        Searchframe=LabelFrame(self.window,text="Search Peagwai",bg="white")
        Searchframe.place(x=50,y=20,width=520,height=70)

        cmb_search=ttk.Combobox(Searchframe,values=("Select","Nama","Id"),state='readonly')
        cmb_search.place(x=10,y=10,width=180,height=30)
        cmb_search.current(0)

        search_data = Entry(Searchframe)
        search_data.place(x=200,y=10,width=180,height=30)

        submit_search = Button(Searchframe,text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
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

    def get_data(self,ev):
        f=self.TabelKotakAmal.focus()
        content=(self.TabelKotakAmal.item(f))
        row = content['values']
        self.var_idkotak.set(row[0])
        self.var_id_pegawai.set(row[1])
        self.var_alamat.set(row[3])
        self.var_jumlah.set(row[4])

def start ():
    window = Tk()
    Kotak_amal(window,1)
    window.mainloop()
  
if __name__ == '__main__':
    start()