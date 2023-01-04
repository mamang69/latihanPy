# latihan konversi satuan temperatur

# Celcius to another temp

print("\n Program Konversi temperatur")

celcius = float(input("Masukan Suhu "))

CReamur = (4/5)*celcius
CKelvin = celcius+273
CFahrenheit = (9/5)*celcius+32
print("suhu dari Celsius ke reamurnya adalah = ", CReamur, "R")
print("suhu dari Celsius ke fahrenheitnya adalah = ", CFahrenheit, "F")
print("suhu dari Celsius ke kelvinnya adalah = ", CKelvin, "K")


'''
PR
Buatlah rumus Fahrenheit to kelvin
Buatlah rumus kelvin to fahrenheit
'''

# rumus fahrenheit to kelvin
f = float(input("Masukan suhu = "))
c = 5/9*(f-32)
k = c+273.15
print("Suhu dari Fahrenheit ke kelvin adalah = ", k)

# rumus kelvin to fahrenheit
k = float(input("masukan suhu Kelvin = "))
c = k-273.15
f = (c*9)/5+32

print("Suhu dari Kevin ke Fahrenheit adalah = ", f)
