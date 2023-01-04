# Casting adalah merubah dari satu tipe ke tipe lain contoh :

print("====INTEGER====")
data_int = 0
print("data = ", data_int, ", type = ", type(data_int))

# cara merubah/meng casting
data_float = float(data_int)
print("data = ", data_float, ", type = ", type(data_float))

data_str = str(data_int)
print("data = ", data_str, ", type = ", type(data_str))

# akan bernilai false jika angka 0 dan True jika angka lain
data_bool = bool(data_int)
print("data = ", data_bool, ", type = ", type(data_bool))


print("====Float====")
data_float = 1.2
print("data = ", data_float, ", type = ", type(data_float))

# akan dibulatkan kebawah
data_int = int(data_float)
print("data = ", data_int, ", type = ", type(data_int))

data_str = str(data_float)
print("data = ", data_str, ", type = ", type(data_str))


data_bool = bool(data_float)
print("data = ", data_bool, ", type = ", type(data_bool))


print("====BOOLEAN====")
data_bool = True
print("data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool)
print("data = ", data_int, ", type = ", type(data_int))

data_str = str(data_bool)
print("data = ", data_str, ", type = ", type(data_str))

data_float = float(data_bool)
print("data = ", data_float, ", type = ", type(data_float))


print("====STRING====")
data_str = "0"
print("data = ", data_str, ", type = ", type(data_str))

data_int = int(data_str)
print("data = ", data_int, ", type = ", type(data_int))

# str to bool hanya akan menjadi false jika string dikosongkan/null
data_bool = bool(data_str)
print("data = ", data_bool, ", type = ", type(data_bool))

data_float = float(data_str)
print("data = ", data_float, ", type = ", type(data_float))
