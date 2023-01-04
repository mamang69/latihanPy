# operasi Logic yang dapat dilakukan di py
# or,and,and,xor

print("===== NOT =====")
a = True
c = not a
print("data a = ", a)
print("--------------- NOT ---------------")
print("data c = ", c)


print("===== OR =====")
a = False
b = False
c = a or b
print(a, "OR", b, "= ", c)
a = False
b = True
c = a or b
print(a, "OR", b, " = ", c)
a = True
b = False
c = a or b
print(a, " OR", b, "= ", c)
a = True
b = True
c = a or b
print(a, " OR", b, " = ", c)

# dalam operasi logic OR, jika salah satunya true maka akan true
print("===== AND =====")
a = False
b = False
c = a and b
print(a, "AND", b, "= ", c)
a = False
b = True
c = a and b
print(a, "AND", b, " = ", c)
a = True
b = False
c = a and b
print(a, " AND", b, "= ", c)
a = True
b = True
c = a and b
print(a, " AND", b, " = ", c)
# dalam operasi logic AND,supaya nilainya true maka semuanya harus true

print("===== XOR =====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "= ", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, " = ", c)
a = True
b = False
c = a ^ b
print(a, " XOR", b, "= ", c)
a = True
b = True
c = a ^ b
print(a, " XOR", b, " = ", c)
# dalam operasi logic XOR, akan true jika salah satunya true dan sisanya akan false
