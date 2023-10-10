#!/usr/bin/env python
# coding: utf-8

# # Kullanıcıdan alınan cümledeki ünlü harf sayısını bulan python kodu.



cumle = input("Lütfen bir cümle girin: ")
unlu_sayisi = 0
unluler = "aeıioöuüAEIİOÖUÜ"

for harf in cumle:
    if harf in unluler: 
        unlu_sayisi +=1
        print('Ünlü harf sayısı:',unlu_sayisi)



cumle = input("Lütfen bir cümle girin: ")
unlu_sayisi = 0
unluler = "aeıioöuüAEIİOÖUÜ"

for harf in cumle:
    if harf in unluler: 
        unlu_sayisi +=1
    print('Ünlü harf sayısı:',unlu_sayisi)




cumle = input("Lütfen bir cümle girin: ")
unlu_sayisi = 0
unluler = "aeıioöuüAEIİOÖUÜ"

for harf in cumle:
    if harf in unluler: 
        unlu_sayisi +=1
print('Ünlü harf sayısı:',unlu_sayisi)




cumle = input("Lütfen bir cümle girin: ")
unlu_sayisi = 0
unluler = "aeıioöuüAEIİOÖUÜ"

for harf in cumle:
    if harf in unluler: 
        unlu_sayisi +=1
print(f"Girdiğiniz cümledeki ünlü harf sayısı: {unlu_sayisi}")


# # Karakter Sayısı Sayma


cumle = input("Bir cümle giriniz: ")
print(len(cumle))


# # Faktöriyel Hesaplama



sayi = int(input("Faktöriyelinin alınmasını istediğiniz sayıyı giriniz: "))
faktoriyel = 1
for i in range(1,sayi+1):
    faktoriyel *= i
print(f"{sayi}!={faktoriyel}")


# # Kelime Ters Çevirme


kelime = input("Lütfen bir kelime giriniz: ")
tersi = kelime[::-1]
print("Kelimenin tersi: ", tersi)


# # Asal sayıları bulma


#Kaça kadar asal sayılar bulunsun diye bir sınır sayı vereceğiz.
sinir = int(input("Bir sınır sayısı giriniz: "))
asallar = []
for sayi in range(2,sinir+1):
#yani 2 ile sınırsayımızın bir fazlası arasındaki bir sayı için
    for bolen in range (2,sayi):
# bölen değeri de 2'den sayı değerine kadar olan sayılar arasındaki bir sayı olacak şekilde
        if sayi%bolen ==0:
            break
        else:
            asallar.append(sayi)
        
print(sinir, "değerine kadar olan asal sayılar: ", asallar)



ust_sinir = int(input("Asal sayıları bulmak için bir üst sınır girin: "))

asal_sayilar = []
for sayi in range(2, ust_sinir + 1):
    asal_mi = True
    for bolen in asal_sayilar:
        if (bolen * bolen > sayi):
            break
        if (sayi % bolen) == 0:
            asal_mi = False
            break
    if asal_mi:
        asal_sayilar.append(sayi)

print("Asal sayılar:", asal_sayilar)


# # Listedeki elemanları sıralama


liste = [3,64,8,2,7558,87,75,5643,1]
liste.sort()
print("Listenin sıralı hali şu şekildedir: ", liste)



liste = ["f","g","m","j"]
liste.sort()
print("Listenin sıralı hali şu şekildedir: ", liste)







