# membuat gabungan area rentang dari angka

# ++++++++++3---------10+++++++++

# contoh
inputUser = float(
    input("masukan angka yang bernilai kurang dari 3 atau lebih dari 10 = "))

# ++++++3
# memeriksa angka kurang dari 3
k3 = inputUser < 3
print("untuk kurang dari 3 adalah = ", k3)

print("\n")
# -------10+++++++
# memeriksa angka lebih dari 10
l10 = inputUser > 10
print("untuk lebih dari 10 adalah = ", l10)

hasil = k3 or l10
print("angka yang anda masukan adalah = ", hasil)

# -------3++++++10-------
print("\n")
# untuk lebih lebih dari 3
l3 = inputUser > 3
print("untuk lebih dari 3 adalah = ", l3)

# untuk kurang dari 10
k10 = inputUser < 10
print("untuk kurang dari 10 adalah = ", k10)

hasil = l3 and k10
print("angka yang anda masukan adalah = ", hasil)


# pr
# no 1. -----0+++++5----8++++++++11----
# no 2. ++++++0-----5+++++8-----11++++++

# no 1
inputUser = float(input("Masukan angka yang akan di cek = "))

l0 = inputUser > 0
print("untuk angka kurang dari 0 ", l0)

k5 = inputUser < 5
print("untuk angka kurang dari 5 ", k5)

l8 = inputUser > 8
print("untuk angka lebih dari 8 ", l8)

k11 = inputUser < 11
print("untuk angka kurang dari 11 ", k11)

hasil = l0 and k5 or l8 and k11

print("Hasil dari angka tersebut adalah ", hasil)

print("\n")

# no 2
inputUser = float(input("Masukan angka yang akan di cek = "))

k0 = inputUser < 0
print("untuk angka kurang dari 0 ", k0)

l5 = inputUser > 5
print("untuk angka lebih dari 5 ", l5)

k8 = inputUser < 8
print("untuk angka kurang dari 8 ", k8)

l11 = inputUser > 11
print("untuk angka lebih dari 11 ", l11)

hasil = k0 or l5 and k8 or l11

print("Hasil dari angka tersebut adalah ", hasil)
