from tkinter import *
from tkinter import ttk,messagebox
from conector import Databasepegawai as dbpegawai

class Pegawai: 
    def __init__(self,window,id_comp):
        self.window = window
        self.window.geometry("1120x480+450+300")
        self.window.title("Pegawai")
        self.window.config(bg="white")

        #variabel
        self.var_idcomp = id_comp
        self.var_nama = StringVar()
        self.var_id = StringVar()
        self.var_telp = StringVar()
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

        submit_search = Button(Searchframe,command=self.show,text="Search",bg="blue",fg="white",font=("times new roman",12,"bold"))
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

        #perbutonnan

        submit = Button (inputframe,text = "Submit",bg="green",fg ="white",command =self.submit,font=("times new roman",12,"bold"))
        submit.place(x=200,y=170)

        update = Button (inputframe,text = "Update",bg="blue",fg ="white",command=self.update,font=("times new roman",12,"bold"))
        update.place(x=300,y=170)

        delete = Button (inputframe,text = "Delete",bg="red",fg ="white",command=self.delete,font=("times new roman",12,"bold"))
        delete.place(x=400,y=170)

        #tabel
        title=Label(self.window,text = "Data Pegawai",font=("times new roman",20,"bold"),bg = "white",fg = "black").place(x = 600 , y = 30,height=50)
        pgw_frame = Frame(self.window,bd=3,relief=RIDGE)
        pgw_frame.place(x=600,y=80,width=500,height=350)

        scrolly = Scrollbar(pgw_frame,orient=VERTICAL)

        self.TabelPegawai=ttk.Treeview(pgw_frame,columns=("id_pegawai","nama","telp"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        self.TabelPegawai.heading("id_pegawai",text="ID")
        self.TabelPegawai.heading("nama",text="Nama Pegawai")
        self.TabelPegawai.heading("telp",text="No Telepon")
        self.TabelPegawai["show"]="headings"
        self.TabelPegawai.pack(fill=BOTH,expand=1)
        self.TabelPegawai.bind("<ButtonRelease-1>",self.get_data)

        self.TabelPegawai.column("id_pegawai",width=5)
        self.TabelPegawai.column("nama",width=120)
        self.TabelPegawai.column("telp",width=80)
        self.show()

    def submit(self):
        if(self.var_id.get() == "" or self.var_nama.get() == "" or self.var_telp.get() == ""):
            messagebox.showwarning("Warning","Isi Semua Data!",parent=self.window)
        else :
            if dbpegawai.cekprimary(self.var_id.get()):
                messagebox.showerror("Error","ID Pegawai sudah ada")
            else :
                dbpegawai.insert(self.var_id.get(),self.var_nama.get(),self.var_telp.get(),self.var_idcomp)
                messagebox.showinfo("Info","Data berhasil dimasukkan")
                self.show()
                self.clear()
        
    def clear(self):
        self.var_id.set("")
        self.var_nama.set("")
        self.var_telp.set("")

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

    def update(self):
        if(self.var_id.get() == ""):
            messagebox.showwarning("Warning","Data Primary belum diisi !",parent=self.window)
        else :
            if not cekprimary(self.var_id.get()):
                messagebox.showerror("Error","ID Pegawai belum ada")
            else :
                dbpegawai.update(self.var_id.get(),self.var_nama.get(),self.var_telp.get())
                messagebox.showinfo("Info","Data berhasil diupdate")
                self.show()
                self.clear()

    def delete(self):
        if(not self.var_id.get() == ""):
            if cekprimary(self.var_id.get()):
                pilih = messagebox.askyesno("Delete data", "Apakah Kamu yakin untuk menghapus data dengan id "+self.var_id.get()+"?")
                if pilih:
                    dbpegawai.delete_data(self.var_id.get(),self.var_nama.get(),self.var_telp.get())
                    self.show()
                    self.clear()
                else:
                    pass
            else :
                messagebox.showerror("Error","ID Pegawai belum ada")
        else : 
            messagebox.showwarning("Warning","Data belum diisi !",parent=self.window)
        

def start ():
    window = Tk()
    objek = Pegawai(window,1)
    window.mainloop()
  
if __name__ == '__main__':
    start()