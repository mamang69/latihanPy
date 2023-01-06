# Operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah assignment

a = 5  # ini adalah assignment
print("Nilai a adalah = ", a)

# jika ada penjumlahan
# a = a+1, maka bisa disingkat menjadi :

a += 1  # artinya a = a+1
print("Nilai a adalah = ", a)

a -= 2  # artinya a = a-2
print("Nilai a adalah = ", a)

a *= 5  # artinya a = a*5
print("Nilai a adalah = ", a)

a /= 2  # artinya a = a/2
print("Nilai a adalah = ", a)

# mdoulus dan floor division
b = 10
b %= 3  # artinya b= b%3
print("\nNilai b adalah = ", b)

b = 10
b //= 3  # artinya b= b//3
print("Nilai b adalah = ", b)

# eksponen
b = 10
b **= 2  # artinya b= b**2
print("Nilai b adalah = ", b)


# Untuk perator bitwise
# or
c = True
print("\nnilai c = ", c)
c |= False
print("nilai c = ", c)

c = False
print("nilai c = ", c)
c |= False
print("nilai c = ", c)

# and
c = True
print("\nnilai c = ", c)
c &= False
print("nilai c = ", c)

c = False
print("nilai c = ", c)
c &= False
print("nilai c = ", c)

# xor
c = True
print("\nnilai c = ", c)
c ^= False
print("nilai c = ", c)

c = True
print("nilai c = ", c)
c ^= True
print("nilai c = ", c)
