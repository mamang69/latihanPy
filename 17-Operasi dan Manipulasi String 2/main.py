# Operator dalam bentuk method

# merubah case dari string

# merubah semua ke upper case

salam = "bro!"

print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KecE AbiEezZzZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# pengecekan menggunakan is X method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam+" is Lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam+" is Lower = " + str(apakah_upper))

# isalpha() --> untuk mengecek semuanya huruf
# isalnum() --> huruf dan angka
# isdecimal() --> untuk angka saja
# isspace() --> untuk mengecek spasi , tap , newline dll
# istitle() --> semua kata dimulai huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul+" is title = " + str(cek_judul))

# cek komponen startswith() endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = ", cek_start)

cek_start = "Sangjangnim Oppa".endswith("Oppa")
print("end   = ", cek_start)

# penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabung = ','.join(pisah)
print("gabungan = ", gabung)

gabung = "akuwwsayangwwkamu"
print("pisah ", gabung.split('ww'))

# alokasi char rjust(),ljust(),center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10, "-")
print("'"+tengah+"'")

# kebalikan alokasi strip()
tengah = tengah.strip("-")
print("'"+tengah+"'")
