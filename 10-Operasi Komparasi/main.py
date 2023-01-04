# Operasi komparasi adalah opersai pembandingan nilai , jadi hasil dari komparasi adalah bolean , jadi hanya ada true dan false

a = 4
b = 2

# lebih dari
print("============ LEBIH DARI ============")
hasil = a > 3
print(a, ' > ', 3, ' = ', hasil)
hasil = b > 3
print(b, ' > ', 3, ' = ', hasil)
hasil = b > 2
print(b, ' > ', 2, ' = ', hasil)


# kurang dari
print("============ KURANG DARI ============")
hasil = a < 3
print(a, ' < ', 3, ' = ', hasil)
hasil = b < 3
print(b, ' < ', 3, ' = ', hasil)
hasil = b < 2
print(b, ' < ', 2, ' = ', hasil)


# lebih dari sama dengan
print("============ LEBIH DARI SAMA DENGAN ============")
hasil = a >= 3
print(a, ' >= ', 3, ' = ', hasil)
hasil = b >= 3
print(b, ' >= ', 3, ' = ', hasil)
hasil = b >= 2
print(b, ' >= ', 2, ' = ', hasil)


# kurang dari sama dengan
print("============ KURANG DARI SAMA DENGAN ============")
hasil = a <= 3
print(a, ' <= ', 3, ' = ', hasil)
hasil = b <= 3
print(b, ' <= ', 3, ' = ', hasil)
hasil = b <= 2
print(b, ' <= ', 2, ' = ', hasil)


# sama dengan
print("============ SAMA DENGAN ============")
hasil = a == 3
print(a, ' == ', 3, ' = ', hasil)
hasil = b == 3
print(b, ' == ', 3, ' = ', hasil)
hasil = b == 2
print(b, ' == ', 2, ' = ', hasil)


# sama dengan
print("============ TIDAK SAMA DENGAN ============")
hasil = a != 3
print(a, ' != ', 3, ' = ', hasil)
hasil = b != 3
print(b, ' != ', 3, ' = ', hasil)
hasil = b != 2
print(b, ' != ', 2, ' = ', hasil)

# jika melakukan komparasi terutama di py , semua operator di atas dapat dilakukan pada syntax literal (a==4 dan lain lain)
# is membandingkan objek contoh penggunaan is . is mengalami banyak perubahan , yang dulunya dapat digunakan untuk literal , namun sekarang tidak bisa
# a = 2
# b = 3
# a is b


# Is
x = 5
y = 5

print("============ IS ============")
# jika angkanya sama maka py akan memasukan nilai tersebut ke memori yang sama
print("nilai x", x, "id = ", hex(id(x)))
# namun jika berbeda maka akan dimasukan ke memori yang berbeda
print("nilai y", y, "id = ", hex(id(y)))

hasil = x is y
# oleh karena itu, hasil dari x,y sekarang true. Karena disimpan ditempat yang sama
print(hasil)


print("============ IS NOT ============")
print("nilai x", x, "id = ", hex(id(x)))
print("nilai y", y, "id = ", hex(id(y)))

# meskipun secara variable berbeda, hasil dari x,y sekarang ini akan bernilai false, karena nilai nya disimpan ditempat yang sama(nilainya sama)
hasil = x is not y
print(hasil)
