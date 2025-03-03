"""
buatkan program perhitungan celcius ke fahrenheit, dan algoritma akan berhenti pada saat diinputkan nilai celcius = 0
"""

# c = 1
# while True:
#     c = int(input("Input nilai celcius : "))
#     if c > 0:
#         f = (9/5 * c) + 32
#         print (f"Nilai {c} celcius = {f} fahrenheit")
#     else:
#         break
print ("keluar dari program")

"""Buat program yang meminta pengguna untuk memasukkan bilangan bulat positif. Program harus menjumlahkan semua bilangan genap dari 1 hingga bilangan yang dimasukkan"""

# bilbul = int(input("Bilangan bulat positif = ")) # bilbul = 10
# genap = 0
# for i in range (1, bilbul+1): # 1 - 11
#     if i % 2 == 0 :
#         genap = genap + i

# print (f"Jumlah bilangan genap 1 - {bilbul} = {genap}")

"""
Buat program yang meminta pengguna memasukkan sebuah bilangan bulat positif, lalu menampilkan pola bintang segitiga siku-siku
"""
# x = int (input ("Tinggi segitiga = "))
# for i in range (1,x+1):
#     print ("* "*i)


"""
Buatlah program Python yang menampilkan angka dari 1 hingga 20. Namun, jika angka tersebut habis dibagi 3, tampilkan "Fizz" dan jika habis dibagi 5, tampilkan "Buzz". Jika habis dibagi 3 dan 5 sekaligus, tampilkan "FizzBuzz".
"""
# print ("Angka 1-20")
# for i in range(1,21):
#     if i % 3 == 0 and i % 5 == 0:
#         print (i, " FizzBuzz")
#     elif i % 5 == 0:
#         print (i, " Buzz")
#     elif i % 3  == 0:
#         print (i, " Fizz")
#     else:
#         print (i)


"""
Buatlah program Python yang meminta pengguna untuk memasukkan 5 angka. Program kemudian menampilkan angka-angka tersebut dalam urutan terbalik.
"""
data = [] # list / array
for i in range (5):
    data.append(input(f"data ke-{i+1} = "))

print()
i = len(data) # len(data) panjang array data
while i != 0:
    print (f"data ke-{i} = {data[i-1]}")
    i -= 1
