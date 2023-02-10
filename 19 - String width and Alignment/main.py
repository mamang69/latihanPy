# Width and Multiline

# data
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_sepatu = 36

# String standard
data_string = f"nama = {data_nama} umur = {data_umur}tinggi = {data_tinggi} sepatu = {data_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline nenggunakan enter/(\n)
data_string = f"nama = {data_nama} \numur = {data_umur}\ntinggi = {data_tinggi} \nsepatu = {data_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# menggunakan kutip triplets

data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar menggunakan :>(jumlah width)
data_nama = "Ucup"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
