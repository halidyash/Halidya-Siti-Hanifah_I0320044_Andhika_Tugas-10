#Soal no 2
#Program Biodata Diri

print("Selamat Datang di Program Biodata")
print("=================================")

#input user
nama = input   ("Nama      : ")
nim = input    ("NIM       : ")
umur = input   ("Umur      : ")
alamat = input ("Alamat    : ")
ntelp = input  ("No. telp  : ")

#format text
text = "Nama : {}\nNIM : {}\nUmur : {}\nAlamat  : {}\nNo. telp : {}\n\n".format(nama, nim, umur, alamat, ntelp)

#membuka file untuk ditulis
file_data = open("biodata.txt", "w")

#menulis text ke dalam file
file_data.write(text)

#menutup file
file_data.close()

#Soal no 3
#Menggunakan mode "a" untuk menambahkan biodata 1 teman

print("Selamat Datang di Program Biodata")
print("=================================")

# input user
nama = input   ("Nama      : ")
nim = input    ("NIM       : ")
umur = input   ("Umur      : ")
alamat = input ("Alamat    : ")
ntelp = input  ("No. telp  : ")

#format text
text = "Nama : {}\nNIM : {}\nUmur : {}\nAlamat  : {}\nNo. telp : {}\n\n".format(nama, nim, umur, alamat, ntelp)

#membuka file untuk ditulis
file_data = open("biodata.txt", "a")

#menulis text ke dalam file
file_data.write(text)

#menutup file
file_data.close()
