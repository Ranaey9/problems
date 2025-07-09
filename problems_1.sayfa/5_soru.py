# Vize ve final notuna göre geçme durumunu hesaplayan algoritma(Not=Vize*0,4+Final*0,6) Geçme Notu:55
vize=float (input("Lütfen vize notunuzu giriniz: "))
final=float (input("Lütfen final notunuzu giriniz: "))
notu = vize * 0.4 + final * 0.6
if notu >= 55:
    print("Geçtiniz, Notunuz:", notu)
else:
    print("Kaldınız, Notunuz:", notu)