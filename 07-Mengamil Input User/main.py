# cara memasukan data dari inputan user

# data yang diterima dari inputan adalah string
data = input("mauskan data: ")

print("data = ", data, type(data))

# jika kita ingin mengambil integer , maka :
data_int = int(input("masukan angka "))
print("data = ", data_int, type(data_int))

# bagaimana jika boolean yang hanya bisa mendeteksi true and false ?
biner = bool(int(input("masukan angka : ")))
print("data = ", biner, type(biner))

# latihan mandiri
# 1 buatlah kalkulator sederhana

a = int(input("masukan angka a = "))
b = int(input("masukan angka b = "))

print("Hasil dari penjumlahan diatas adalah = ", a+b)
print("Hasil dari pengurangan diatas adalah = ", a-b)
print("Hasil dari perkalian diatas adalah = ", a*b)
print("Hasil dari pembagian diatas adalah = ", a/b)
print("Hasil dari modulo diatas adalah = ", a % b)

a = int(input("Masukan angka yang ingin di cek = "))
if a % 2 == 0:
    print(a, " Adalah angka genap")
else:
    print(a, " Adalah angka ganjil")
