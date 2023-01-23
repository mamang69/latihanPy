# Operasi dan manipulasi stirng

# 1. Menyambung string (concatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah+"'" + nama_akhir

print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. Operator untuk sting
# mengecek apakah ada komponen character di string
d = "d"
status = d in nama_lengkap
print("sting "+d+" ada di"+nama_lengkap + " " + str(status))

d = "D"
status = d in nama_lengkap
print("sting "+d+" ada di"+nama_lengkap + " " + str(status))

d = "d"
status = d not in nama_lengkap
print("sting "+d+" tidak ada di"+nama_lengkap + " " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : "+nama_lengkap[0])
print("index ke-0 : "+nama_lengkap[6])
# dari 0 sampai 3, karena angka terakhirnya tidak dicetak
print("index ke-[0:4] : "+nama_lengkap[0:4])

# 0 sampai 6 dengan increment 2
print("index ke-[0,2,4,6] : "+nama_lengkap[0:6:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

# operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada data diatas " + data + " = " + str(jumlah))
