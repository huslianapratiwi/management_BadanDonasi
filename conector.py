import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "Donasi_kartika"
)

if db.is_connected():
  print("Berhasil terhubung ke database")

def cekprimary(id):
  cursor = db.cursor()
  sql = """select * from Pegawai where id_pegawai = (%s) """   % (id)
  cursor.execute(sql)
  row=cursor.fetchone()
  if row!=None:
    return True
  else :
    return False

def insert (id,nama,no_telp):
    cursor = db.cursor()
    sql = "INSERT INTO Pegawai (id_pegawai,nama,no_telepon) VALUES (%s,%s,%s)"
    val = (id,nama,no_telp)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

def getdata():
    cursor = db.cursor()
    sql = "select * from Pegawai"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def update(id,nama,no_telp):
    cursor = db.cursor()
    sql = "update Pegawai set nama =%s, no_telepon =%s where id_pegawai =%s" 
    val = (nama,no_telp,id)
    cursor.execute(sql,val)
    db.commit()
    print("data diupdate")

def delete_data(id,nama,no_telp):
    cursor = db.cursor()
    sql = "DELETE FROM Pegawai WHERE nama =%s or no_telepon =%s or id_pegawai =%s"
    val = (nama,no_telp,id)
    cursor.execute(sql,val)
    db.commit
    print("Data berhasil dibapus")