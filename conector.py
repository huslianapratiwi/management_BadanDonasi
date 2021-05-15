import mysql.connector
import time

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

  def getsearch(id_comp,conteks,hasil):
    cursor = db.cursor()
    like = ("%" + str(hasil) + "%")
    sql = """select id_pegawai,nama,no_telepon,tgl_masuk, FLOOR(DATEDIFF(CURRENT_DATE(),tgl_masuk)/365) from Pegawai where id_company = '%s' and %s like '%s' ;""" % (id_comp,conteks,like)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return results

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
    val = (id_dntr,user,pwd,nama,alamat,no_telp,tipe)
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

  def insert (id_dntr,jumlah,nama_comp):
    
    temp = time.strftime('%Y%m%d')
    year = temp[0:4]
    mount = temp[4:6]
    day = temp[6:8]
    date = str(year) + "-" + str(mount) + "-" +str(day)

    id_donasi = 1
    while donasi_uang.cekada_donasi("id_donasi",id_donasi):
      id_donasi += 1

    cursor = db.cursor()
    sql = """INSERT INTO Donasi (id_donatur,id_donasi,tgl_donasi,id_company) VALUES (%s,%s,%s,(SELECT Badan_amal.id_company from Badan_amal where Badan_amal.nama = %s))"""
    val = (id_dntr,id_donasi,date,nama_comp)
    cursor.execute(sql, val)
    db.commit()

    sql = "INSERT INTO Uang (id_donasi,jumlah_total) VALUES (%s,%s)"
    val = (id_donasi,jumlah)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

  def cekada_donasi(jenis,id):
    cursor = db.cursor()
    sql = """select (%s) from Donasi where (%s)= '%s' """ % (jenis,jenis,id)
    cursor.execute(sql)
    row=cursor.fetchone()
    if row!=None :
      return True
    else :
      return False

class donasi_barang:
  def insert(id_dntr,jumlah,jenis,nama_comp):
    temp = time.strftime('%Y%m%d')
    year = temp[0:4]
    mount = temp[4:6]
    day = temp[6:8]
    date = str(year) + "-" + str(mount) + "-" +str(day)

    id_donasi = 1
    while donasi_uang.cekada_donasi("id_donasi",id_donasi):
      id_donasi += 1

    cursor = db.cursor()
    sql = """INSERT INTO Donasi (id_donatur,id_donasi,tgl_donasi,id_company) VALUES (%s,%s,%s,(SELECT Badan_amal.id_company from Badan_amal where Badan_amal.nama = %s))"""
    val = (id_dntr,id_donasi,date,nama_comp)
    cursor.execute(sql, val)
    db.commit()

    sql = "INSERT INTO Barang (id_donasi,jumlah,jenis) VALUES (%s,%s,%s)"
    val = (id_donasi,jumlah,jenis)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

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
    sql = """select id_kotak,id_pegawai,nama,alamat,jumlah_uang,tgl_penarikan from Kotak_amal natural join Pegawai where id_company = '%s' ORDER BY id_kotak ASC """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return(results)

  def update(id_kotak,pegawai,alamat,jumlah):
    cursor = db.cursor()
    sql = "update Kotak_amal set id_pegawai=%s,alamat =%s, jumlah_uang =%s where id_kotak =%s" 
    val = (pegawai,alamat,jumlah,id_kotak)
    cursor.execute(sql,val)
    db.commit()
    print("data diupdate")

  def delete_data(id):
    cursor = db.cursor()
    sql = "DELETE FROM Kotak_amal WHERE id_kotak =%s" % id
    cursor.execute(sql)
    db.commit()
    print("Data berhasil dibapus")
  
  def getsearch(id_comp,conteks,hasil):
    cursor = db.cursor()
    kunci = "%" + str(hasil) + "%"
    sql = """select id_kotak,id_pegawai,nama,alamat,jumlah_uang,tgl_penarikan from Kotak_amal natural join Pegawai where id_company = '%s' and %s like '%s' """ % (id_comp,conteks,kunci)
    cursor.execute(sql)
    results = cursor.fetchall()
    return(results)

class dbdonatur: 
  def getnama(id):
    cursor = db.cursor()
    sql = """select nama from Donatur where id_donatur = %s """ % (id)
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

class DatabasePenerima:


  def insert(id_pegawai,id_comp,nama,alamat,telp1,telp2):
    id_penerima = 1
    while (DatabasePenerima.cekprimary(id_penerima)):
      id_penerima += 1 
    cursor = db.cursor()
    sql = """insert into Penerima (id_pegawai,id_company,id_penerima,nama,alamat) values  (%s,%s,%s,%s, %s ) """
    var = (id_pegawai,id_comp,id_penerima,nama,alamat)
    cursor.execute(sql, var)
    db.commit()
    DatabasePenerima.insert_phone(id_penerima,telp1)
    if(telp2 != "") :
      DatabasePenerima.insert_phone(id_penerima,telp2)
    print("berhasil")
  
  def insert_phone(id,telp):
    id_ponsel = 1
    while (DatabasePenerima.cekprimary_hp(id_ponsel)):
      id_ponsel +=1
    cursor = db.cursor()
    sql = "insert into Ponsel_penerima (id_penerima,id_nomor_hp,nomor_hp) values (%s,%s,'%s')" % (id,id_ponsel,telp)
    cursor.execute(sql)
    db.commit()

  def cekprimary(id):
    cursor = db.cursor()
    sql = "select * from Penerima where id_penerima = %s" % (id)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data != None : 
      return True
    else :
      return False

  def cekprimary_hp(id):
    cursor = db.cursor()
    sql = "select * from Ponsel_penerima where id_nomor_hp = %s" % (id)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data != None : 
      return True
    else :
      return False

  def getdata(id):
    cursor = db.cursor()
    sql = """select Penerima.id_penerima,Pegawai.nama,Penerima.nama,Penerima.alamat,GROUP_CONCAT(Ponsel_penerima.nomor_hp) as no_hp from Penerima join Pegawai join Ponsel_penerima where Penerima.id_pegawai = Pegawai.id_pegawai and Ponsel_penerima.id_penerima = Penerima.id_penerima and Penerima.id_company = %s GROUP BY Penerima.id_penerima """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    hasil = []
    if results != None :
      for i in range (len(results)):
        phone = results[i][4].split(',')
        list = []
        for j in range (len(results[i])-1) :
          list.append(results[i][j])
        list.append(str(phone[0]))
        if len(phone) > 1 :
          list.append( str(phone[1]))
        hasil.append(list)
        
      return hasil

  def search_nama(nama,id_comp):
    cursor = db.cursor(buffered = True)
    sql = """Select Penerima.id_pegawai from Penerima join Pegawai WHERE Penerima.id_pegawai = Pegawai.id_pegawai and Pegawai.nama = (%s) and Penerima.id_company = (%s) """ 
    var = (nama,id_comp)
    cursor.execute(sql, var)
    data = cursor.fetchone()
    return data[0] 

  def getprimary(nama):
    cursor = db.cursor()
    sql = """SELECT id_penerima from Penerima where nama ='%s' """ % (nama)
    cursor.execute(sql)
    data = cursor.fetchone()
    return data
 
  def delete(id):
    cursor = db.cursor()
    sql = "Delete from Ponsel_penerima where id_penerima =%s" % (id)
    cursor.execute(sql)
    db.commit()
    sql1 = "Delete from Penerima where id_penerima =%s" % (id)
    cursor.execute(sql1)
    db.commit()

  def update(id,pegawai,comp,nama,alamat,telp1,telp2):
    cursor = db.cursor()
    sql = """UPDATE Penerima set id_pegawai = %s, nama = %s,alamat = %s where id_penerima = %s and id_company = %s""" 
    var = (pegawai,nama,alamat,id,comp)
    cursor.execute(sql, var)
    db.commit()

    list_phone = DatabasePenerima.getphoneid(id)
    DatabasePenerima.update_ponsel(list_phone[0][0],telp1)
    if (len(list_phone) > 1):
      DatabasePenerima.update_ponsel(list_phone[1][0],telp2)

  def getphoneid(id):
      cursor = db.cursor()
      sql = "select id_nomor_hp from Ponsel_penerima where id_penerima = %s " % id
      cursor.execute(sql)
      data = cursor.fetchall()
      return data 

  def update_ponsel(id,telp):
    cursor = db.cursor()
    sql = "update Ponsel_penerima set nomor_hp = '%s' where id_nomor_hp = %s " % (telp,id)
    cursor.execute(sql)
    db.commit()
  
  def getsearch(id,conteks,hasil):
    cursor = db.cursor()
    kunci = "%" + str(hasil) + "%"
    sql = """select Penerima.id_penerima,Pegawai.nama,Penerima.nama,Penerima.alamat,GROUP_CONCAT(Ponsel_penerima.nomor_hp) as no_hp from Penerima join Pegawai join Ponsel_penerima where Penerima.id_pegawai = Pegawai.id_pegawai and Ponsel_penerima.id_penerima = Penerima.id_penerima and Penerima.id_company = %s and %s like '%s' GROUP BY Penerima.id_penerima """ % (id,conteks,kunci)
    cursor.execute(sql)
    results = cursor.fetchall()
    hasil = []
    if results != None :
      for i in range (len(results)):
        phone = results[i][4].split(',')
        list = []
        for j in range (len(results[i])-1) :
          list.append(results[i][j])
        list.append(str(phone[0]))
        if len(phone) > 1 :
          list.append( str(phone[1]))
        hasil.append(list)
        
      return hasil

class DatabaseRiwayat:
  def getdata(id):
    cursor = db.cursor()
    sql = """select Donasi.id_donasi,Donatur.nama,jumlah_total,tgl_donasi,Badan_amal.nama from Donasi join Donatur join Badan_amal join Uang where Donasi.id_donasi = Uang.id_donasi and Donasi.id_company = Badan_amal.id_company and Donatur.id_donatur = Donasi.id_donatur and Donasi.id_donatur = %s  ORDER BY Donasi.id_donasi ASC """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results
  
  def getdatabarang(id):
    cursor = db.cursor()
    sql = """select Donasi.id_donasi,Donatur.nama,jenis,jumlah,tgl_donasi,Badan_amal.nama from Donasi join Donatur join Badan_amal join Barang where Donasi.id_donasi = Barang.id_donasi and Donasi.id_company = Badan_amal.id_company and Donatur.id_donatur = Donasi.id_donatur and Donasi.id_donatur = %s  ORDER BY Donasi.id_donasi ASC """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

  def getsearchuang(id,konteks,hasil):
    cursor = db.cursor()
    kunci = "%" + str(hasil) + "%"
    sql = """select Donasi.id_donasi,Donatur.nama,jumlah_total,tgl_donasi,Badan_amal.nama from Donasi join Donatur join Badan_amal join Uang where Donasi.id_donasi = Uang.id_donasi and Donasi.id_company = Badan_amal.id_company and Donatur.id_donatur = Donasi.id_donatur and Donasi.id_donatur = %s and %s like '%s' ORDER BY Donasi.id_donasi ASC """ % (id,konteks,kunci)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

  def getsearchbarang(id,konteks,hasil):
    cursor = db.cursor()
    kunci = "%" + str(hasil) + "%"
    sql = """select Donasi.id_donasi,Donatur.nama,jenis,jumlah,tgl_donasi,Badan_amal.nama from Donasi join Donatur join Badan_amal join Barang where Donasi.id_donasi = Barang.id_donasi and Donasi.id_company = Badan_amal.id_company and Donatur.id_donatur = Donasi.id_donatur and Donasi.id_donatur = %s and %s like '%s'  ORDER BY Donasi.id_donasi ASC """ % (id,konteks,kunci)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

class DatabaseDonasi:
  
  def getdata(id):
    cursor = db.cursor()
    sql = """select Donasi.id_donasi,Donatur.nama,jumlah_total,tgl_donasi from Donasi join Donatur join Badan_amal join Uang where Donasi.id_donasi = Uang.id_donasi and Donasi.id_company = Badan_amal.id_company and Donatur.id_donatur = Donasi.id_donatur and Donasi.id_company = %s  ORDER BY Donasi.id_donasi ASC """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results
  
  def getdatabarang(id):
    cursor = db.cursor()
    sql = """select Donasi.id_donasi,Donatur.nama,jenis,jumlah,tgl_donasi from Donasi join Donatur join Badan_amal join Barang where Donasi.id_donasi = Barang.id_donasi and Donasi.id_company = Badan_amal.id_company and Donatur.id_donatur = Donasi.id_donatur and Donasi.id_company = %s  ORDER BY Donasi.id_donasi ASC """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results
  
  def getsearchuang(id,konteks,hasil):
    cursor = db.cursor()
    kunci = "%" + str(hasil) + "%"
    sql = """select Donasi.id_donasi,Donatur.nama,jumlah_total,tgl_donasi from Donasi join Donatur join Badan_amal join Uang where Donasi.id_donasi = Uang.id_donasi and Donasi.id_company = Badan_amal.id_company and Donatur.id_donatur = Donasi.id_donatur and Donasi.id_company = %s and %s like '%s'  ORDER BY Donasi.id_donasi ASC """ % (id,konteks,kunci)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

  def getsearchbarang(id,konteks,hasil):
    cursor = db.cursor()
    kunci = "%" + str(hasil) + "%"
    sql = """select Donasi.id_donasi,Donatur.nama,jenis,jumlah,tgl_donasi from Donasi join Donatur join Badan_amal join Barang where Donasi.id_donasi = Barang.id_donasi and Donasi.id_company = Badan_amal.id_company and Donatur.id_donatur = Donasi.id_donatur and Donasi.id_company = %s and %s like '%s' ORDER BY Donasi.id_donasi ASC """ % (id,konteks,kunci)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

class DatabaseDonatur:
  
  def getdata(id):
    cursor = db.cursor()
    sql = """select Donatur.id_donatur,Donatur.nama,Donatur.username,Donatur.alamat,Donatur.no_telepon,Donatur.tipe from Donatur join Donasi join Badan_amal where Donatur.id_donatur = Donasi.id_donasi and Badan_amal.id_company = Donasi.id_company and Badan_amal.id_company = %s """ % (id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results
  
  def getsearch(id,konteks,hasil):
    cursor = db.cursor()
    kunci = "%" + str(hasil) + "%"
    sql = """select Donatur.id_donatur,Donatur.nama,Donatur.username,Donatur.alamat,Donatur.no_telepon,Donatur.tipe from Donatur join Donasi join Badan_amal where Donatur.id_donatur = Donasi.id_donasi and Badan_amal.id_company = Donasi.id_company and Badan_amal.id_company = %s and %s like '%s' """ % (id,konteks,kunci)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

class DatabaseDiagram:
  def gettanggal_donasi(id_comp,date):
    cursor = db.cursor()
    sql = """select count(tgl_donasi) from Donasi where id_company = %s and tgl_donasi = '%s'  """ % (id_comp,date)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results[0][0]
  
  def getexperience(id_comp,exp):
    cursor = db.cursor()
    sql = """select count(FLOOR(DATEDIFF(CURRENT_DATE(),tgl_masuk)/365)) from Pegawai where id_company = %s and FLOOR(DATEDIFF(CURRENT_DATE(),tgl_masuk)/365) = %s """ % (id_comp,exp)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results[0][0]

  def gettanggal_user(id_dntr,date):
    cursor = db.cursor()
    sql = """select count(tgl_donasi) from Donasi where id_donatur= %s and tgl_donasi = '%s'  """ % (id_dntr,date)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results[0][0]
  
  def getjenis(id_comp,Jenis):
    cursor = db.cursor()
    sql = """select count(jenis),jenis from Donasi natural join Barang where id_company = %s and jenis = '%s'  """ % (id_comp,Jenis)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results
  
  def getjenisuser(id_dntr,Jenis):
    cursor = db.cursor()
    sql = """select count(jenis),jenis from Donasi natural join Barang where id_donatur= %s and jenis = '%s'  """ % (id_dntr,Jenis)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

class DatabaseBadan_amal:
  def getnama(id):
    cursor = db.cursor()
    sql = "Select nama from Badan_amal where id_company = %s " % (id)
    cursor.execute(sql)
    results = cursor.fetchone()
    return results[0]