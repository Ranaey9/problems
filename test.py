# isim = input("Adını gir: ")
# print("Merhaba, " + isim + "!")

# a=int(input("sayiyı gir: "))
# b=int(input("sayiyi gir: "))
# print("sum :",a+b)

# tek çift kontrolü
# numb=int(input("please enter a number: "))
# if(numb%2==0):
#     print("cift")
# else: print("tek")

# pozatif negatif kontrolü
# numb=int(input("Please enter a number: "))
# if( numb>0):
#     print("Positive")
# elif( numb<0):
#     print("Negative")
# else:
#     print("Zero")

# geçme durumu hesaplama
# nott = int(input("Lütfen notunuzu giriniz: "))
# if nott >= 90 and nott <= 100:
#     print("Puanınız: AA")
# elif nott >= 80:
#     print("Puanınız: BA")
# elif nott >= 70:
#     print("Puanınız: BB")
# elif nott >= 60:
#     print("Puanınız: CB")
# elif nott >= 50:
#     print("Puanınız: CC")
# elif nott >= 0:
#     print("Kaldınız")
# else:
#     print("Geçersiz not girdiniz.")

# sayi = 1
# while sayi <= 10:
#     print(sayi)
#     sayi += 1

# 0 girene kadar sayılar topla
# toplam = 0
# i = 0
# while True:  # sürekli çalışsın ama kesinlikle break kullan
#     sayi = int(input("Sayı gir (0 girersen durur): "))
#     if sayi == 0:
#         break
#     toplam += sayi
#     i += 1
# print("Toplam:", toplam)

# cift sayılar 
# numb=int (input("Lütfen bir sayı giriniz: "))
# for i in range (1,numb+1): #for numb in range(2,101,2): 2’den başla, 2’şer artırarak 100’e kadar git.
#     if i % 2 == 0:
#         print(i)

#  Kullanıcıdan alınan N sayının ortalamasını hesapla
# n=int(input("Kaç sayı gireceksiniz? "))
# sum=0
# for i in range(n):
#     sayi= int(input("Sayıyı giriniz: "))
#     sum += sayi
# ortalama = sum / n
# print("Ortalama:", ortalama)

# faktöriyel hesaplama
# n=int (input("Lütfen bir sayı giriniz: "))
# faktoriyel = 1
# for i in range(1, n + 1):
#     faktoriyel *= i
# print("Faktöriyel:", faktoriyel)

# Bir sayının asal olup olmadığını bulan
# numb=int (input("Lütfen bir sayı giriniz: "))
# if numb <2 :
#     print("asal degil")
# for i in range(2,numb):
#     if numb%i==0:
#         print("asal degil")
#         break
# else:
#     print("asal") 

# Girilen Sayıya Kadar Olan Asal Sayıları Listele
# sayi = int(input("Bir sayı giriniz: "))
# for j in range(2, sayi + 1):
#     asal = True
#     for i in range(2, j):
#         if j % i == 0:
#             asal = False
#             break
#     if asal:
#         print(j)

# Girilen N sayıyı listeye ekle, içinden en büyük ve en küçük olanı yazdır.
# n=int(input("Kaç sayı gireceksiniz? "))
# max1=0
# min1=0
# liste=[]
# for i in range(0,n):
#     sayi= int(input("Sayıyı giriniz: "))
#     liste.append(sayi)
#     max1=max(liste)
#     min1=min(liste)
# print("En büyük sayı:", max1)
# print("En küçük sayı:", min1)
# print("Liste:", liste)

# Ortalama üzerindeki sayıları bul
# n = int(input("Kaç sayı gireceksiniz? "))
# liste = []
# sum=0
# for i in range(0,n):
#     sayi = int(input("sayıyı giriniz: "))
#     liste.append(sayi)
# sum+=sayi
# ortalama = sum / n
# print("Ortalama:", ortalama)
# print("Ortalama üzeri sayılar:")
# for s in liste:
#     if s > ortalama:
#         print(s)
