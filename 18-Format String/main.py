# Format String

# contoh generic
# string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)


# boolean
boolean = True
format_str = f"boolnya adalah {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"angka = {angka:d}"
print(format_str)

# ribuan
angka = 2000000
format_str = f"angka = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.542
format_str = f"angka = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54231
format_str = f"angka = {angka:010.2f}"
print(format_str)

# menampilkan tanda plus minus
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus :+d}"
format_plus = f"plus = {angka_plus :+d}"

print(format_minus)
print(format_plus)

# format persen
persentase = 0.045
format_persen = f"persen {persentase :.2%}"
print(format_persen)

# melakukan operasi aritmatika dalam placeholder/kurawal
harga = 10000
jumlah = 5

format_str = f"harga total = {harga*jumlah:,}"
print(format_str)


# format angka lain (binary,octal,hexadecimal)

angka = 255
format_binary = f"binary {bin(angka)}"
format_octal = f"octal {oct(angka)}"
format_hexa = f"hexa {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)
