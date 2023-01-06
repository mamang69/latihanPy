# data = "ini adalah string"
# print(data)
# print(type(data))
# 1. Cara membuat string

'''
  1.Dengan menggunakan single quote (' ')
  2.Dengan menggunakan double quote (" ")
'''

data = 'Menggunakan singgle quote'
print(data)

data = 'Menggunakan double quote'
print(data)

print('"halo apa kabar"')
print("'halo apa kabar'")
print("ini adalah hari jum'at")

# kita bisa menggunakan backlash (\)
# membuat tanda (') menjadi string , contoh :

print('mari kita solat jum\'at')
print('g\'day, isn\'t it ?')

# membuat backlash menjadi string
print("C:\\user\\ucup")

# tab (\t)
print("ucup \totong, jauhan")

# backspace \b
print("ucup \botong")

# newline/enter \n,
print("baris pertama. \nbaris kedua")  # LF -> Line Feed (UNIX)
print("baris pertama. \rbaris kedua")  # CR ->Carriage Return
# CLRF -> Line Feed Carriage return (Windows)
print("baris pertama. \r\nbaris kedua")

# string literal atau raw (r)
# print('C:\new folder')  # harusnya menggunakan

print(r'C:\new folder')

# multi line literal ("""""")
print("""
Nama  : Ucup
kelas : 3 SD
""")

print(r""" 
Nama  : Ucup
kelas : 3 SD
web   : www.ucup.com/newID
""")
