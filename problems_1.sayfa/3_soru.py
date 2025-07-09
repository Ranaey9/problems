# Klavyeden girilen 3 sayı içerisinden en küçük sayıyı bulan algoritma?
a = int(input("1. sayıyı girin: "))
b = int(input("2. sayıyı girin: "))
c = int(input("3. sayıyı girin: "))

en_kucuk = a
if b < en_kucuk:
    en_kucuk = b
if c < en_kucuk:
    en_kucuk = c

print("En küçük sayı:", en_kucuk)
