import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "Donasi_kartika"
)

if db.is_connected():
  print("Berhasil terhubung ke database")


#PEGAWAI
class Databasepegawai:
  def cekprimary(id):
    cursor = db.cursor()
    sql = """select * from Pegawai where id_pegawai = (%s) """   % (id)
    cursor.execute(sql)
    row=cursor.fetchone()
    if row!=None:
      return True
    else :
      return False

  def insert(id,nama,no_telp,tgl,id_comp):
    cursor = db.cursor()
    sql = "INSERT INTO Pegawai (id_pegawai,nama,no_telepon,tgl_masuk,id_company) VALUES (%s,%s,%s,%s,%s)"
    val = (id,nama,no_telp,tgl,id_comp)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

  def getdata(id):
    cursor = db.cursor()
    sql = """select id_pegawai,nama,no_telepon,tgl_masuk, FLOOR(DATEDIFF(CURRENT_DATE(),tgl_masuk)/365) from Pegawai where id_company = '%s' """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return(results)

  def update(id,nama,no_telp):
    cursor = db.cursor()
    sql = "update Pegawai set nama =%s, no_telepon =%s where id_pegawai =%s" 
    val = (nama,no_telp,id)
    cursor.execute(sql,val)
    db.commit()
    print("data diupdate")

  def delete_data(id):
    cursor = db.cursor()
    sql = "DELETE FROM Pegawai WHERE id_pegawai =%s" % id
    cursor.execute(sql)
    db.commit()
    print("Data berhasil dibapus")

class dbregis:
  def insert_donatur(nama,user,pwd,alamat,no_telp,tipe):
    id_dntr = 1
    while dbregis.cekada_dntr("id_donatur",id_dntr):
      id_dntr += 1

    cursor = db.cursor()
    sql = "INSERT INTO Donatur (id_donatur,username,password,nama,alamat,no_telepon,tipe) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (id_dntr,user,pwd,alamat,nama,no_telp,tipe)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

  def insert_badan(nama,user,pwd,alamat):
    id_comp = 1
    while dbregis.cekada_badan("id_company",id_comp):
      id_comp += 1

    cursor = db.cursor()
    sql = "INSERT INTO Badan_amal (id_company,username,password,alamat,nama) VALUES (%s,%s,%s,%s,%s)"
    val = (id_comp,user,pwd,alamat,nama)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

  def cekada_badan(jenis,id):
    cursor = db.cursor()
    sql = """select (%s) from Badan_amal where (%s)= '%s' """ % (jenis,jenis,id)
    cursor.execute(sql)
    row=cursor.fetchone()
    if row!=None:
      return True
    else :
      return False

  def cekada_dntr(jenis,id):
    cursor = db.cursor()
    sql = """select (%s) from Donatur where (%s)= '%s' """ % (jenis,jenis,id)
    cursor.execute(sql)
    row=cursor.fetchone()
    if row!=None:
      return True
    else :
      return False

class dblogin:
  def getdata(pilih,isi):
    cursor = db.cursor()
    sql = """select (%s) from Badan_amal where username = '%s' """ % (pilih,isi)
    cursor.execute(sql)
    data = cursor.fetchone()
    return data

  def getdata_donatur(pilih,isi):
    cursor = db.cursor()
    sql = """select (%s) from Donatur where username = '%s' """ % (pilih,isi)
    cursor.execute(sql)
    data = cursor.fetchone()
    return data

class donasi_uang:
  def getBadanAmal():
    cursor = db.cursor()
    sql = """select nama from Badan_amal"""
    cursor.execute(sql)
    data = cursor.fetchall()
    list_nama = []
    for i in range(len(data)):
      list_nama.append(data[i][0])
    return list_nama

class Databasekotakamal:
  def cekprimary(id):
    cursor = db.cursor()
    sql = """select * from Kotak_amal where id_kotak = (%s) """   % (id)
    cursor.execute(sql)
    row=cursor.fetchone()
    if row!=None:
      return True
    else :
      return False

  def insert(id_kotak,id_comp,id_pgw,alamat,jumlah,tgl):
    cursor = db.cursor()
    sql = """INSERT INTO Kotak_amal (id_kotak,id_company,id_pegawai,alamat,jumlah_uang,tgl_penarikan) VALUES (%s,%s,%s,%s,%s,%s)""" 
    val = (id_kotak,id_comp,id_pgw,alamat,jumlah,tgl)
    cursor.execute(sql,val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

  def getdata(id):
    cursor = db.cursor()
    sql = """select id_kotak,id_pegawai,nama,alamat,jumlah_uang,tgl_penarikan from Kotak_amal natural join Pegawai where id_company = '%s' """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return(results)

  def update(alamat,jumlah,id_pegawai):
    cursor = db.cursor()
    sql = "update Kotak_amal set alamat =%s, jumlah_uang =%s where id_pegawai =%s" 
    val = (alamat,jumlah_uang,id_pegawai)
    cursor.execute(sql,val)
    db.commit()
    print("data diupdate")

  def delete_data(id):
    cursor = db.cursor()
    sql = "DELETE FROM Kotak_amal WHERE id_kotak =%s" % id
    cursor.execute(sql)
    db.commit()
    print("Data berhasil dibapus")

class dbregis:
  def insert_donatur(nama,user,pwd,alamat,no_telp,tipe):
    id_dntr = 1
    while dbregis.cekada_dntr("id_donatur",id_dntr):
      id_dntr += 1

    cursor = db.cursor()
    sql = "INSERT INTO Donatur (id_donatur,username,password,nama,alamat,no_telepon,tipe) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (id_dntr,user,pwd,alamat,nama,no_telp,tipe)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

  def insert_badan(nama,user,pwd,alamat):
    id_comp = 1
    while dbregis.cekada_badan("id_company",id_comp):
      id_comp += 1

    cursor = db.cursor()
    sql = "INSERT INTO Badan_amal (id_company,username,password,alamat,nama) VALUES (%s,%s,%s,%s,%s)"
    val = (id_comp,user,pwd,alamat,nama)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

  def cekada_badan(jenis,id):
    cursor = db.cursor()
    sql = """select (%s) from Badan_amal where (%s)= '%s' """ % (jenis,jenis,id)
    cursor.execute(sql)
    row=cursor.fetchone()
    if row!=None:
      return True
    else :
      return False

  def cekada_dntr(jenis,id):
    cursor = db.cursor()
    sql = """select (%s) from Donatur where (%s)= '%s' """ % (jenis,jenis,id)
    cursor.execute(sql)
    row=cursor.fetchone()
    if row!=None:
      return True
    else :
      return False

