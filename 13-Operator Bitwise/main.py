# bitwise => operasi masing masing bit

a = 9
b = 5

# bitwise OR (|)
c = a | b
print("\n============= OR =============")
print("nilai :", a, ", binary: ", format(a, '08b'))
print("nilai :", b, ", binary: ", format(b, '08b'))
print("------------------------------(|)")
print("nilai :", c, ", binary: ", format(b, '08b'))

# bitwise AND (&)
c = a & b
print("\n============= OR =============")
print("nilai :", a, ", binary: ", format(a, '08b'))
print("nilai :", b, ", binary: ", format(b, '08b'))
print("------------------------------(&)")
print("nilai :", c, ", binary: ", format(b, '08b'))

# bitwise XOR (^)
c = a ^ b
print("\n============= OR =============")
print("nilai :", a, ", binary: ", format(a, '08b'))
print("nilai :", b, ", binary: ", format(b, '08b'))
print("------------------------------(^)")
print("nilai :", c, ", binary: ", format(b, '08b'))

# bitwise NOT (~)
c = ~a
print("\n============= NOT =============")
# untuk mengakali mirrornya, maka gunakanlah XOR contoh :
d = 0b0000001001
e = 0b1111111111
print("nilai : ", e ^ d, ", binary : ", format(e ^ d, '08b'))

# shifting

# shift right (>>)
c = a >> 2
print("\n============= SHIFT RIGHT =============")
print("nilai :", a, ", binary: ", format(a, '08b'))
print("------------------------------(>>)")
print("nilai :", c, ", binary: ", format(c, '08b'))

# shift left (<<)
c = a << 2
print("\n============= SHIFT LEFT =============")
print("nilai :", a, ", binary: ", format(a, '08b'))
print("------------------------------(<<)")
print("nilai :", a, ", binary: ", format(c, '08b'))
