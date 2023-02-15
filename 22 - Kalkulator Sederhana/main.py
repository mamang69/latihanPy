# latihan membuat kalkulator sederhana

print("======= Selamat Datang Di Perhitungan Mamang =======")

angka1 = float(input("Masukan angka 1 = "))
operator = input("Pilih operator(+,-,*,/) ")
angka2 = float(input("Masukan angka 2 = "))

if operator == "+":
    hasil = angka1+angka2
    print(f"Anda memilih penjumlahan dan hasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Anda memilih pengurangan dan hasilnya adalah = {hasil}")
elif operator == "*":
    hasil = angka1*angka2
    print(f"Anda memilih perkalian dan hasilnya adalah = {hasil}")
elif operator == "/":
    hasil = angka1/angka2
    print(f"Anda memilih pembagian dan hasilnya adalah = {hasil}")
else:
    print("Operasi apaan tu coy")
