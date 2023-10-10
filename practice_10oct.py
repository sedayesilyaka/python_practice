#!/usr/bin/env python
# coding: utf-8

# # Kullanıcıdan alınan cümledeki ünlü harf sayısını bulan python kodu.

# In[ ]:


cumle = input("Lütfen bir cümle girin: ")
unlu_sayisi = 0
unluler = "aeıioöuüAEIİOÖUÜ"

for harf in cumle:
    if harf in unluler: 
        unlu_sayisi +=1
        print('Ünlü harf sayısı:',unlu_sayisi)


# In[6]:


cumle = input("Lütfen bir cümle girin: ")
unlu_sayisi = 0
unluler = "aeıioöuüAEIİOÖUÜ"

for harf in cumle:
    if harf in unluler: 
        unlu_sayisi +=1
    print('Ünlü harf sayısı:',unlu_sayisi)


# In[7]:


cumle = input("Lütfen bir cümle girin: ")
unlu_sayisi = 0
unluler = "aeıioöuüAEIİOÖUÜ"

for harf in cumle:
    if harf in unluler: 
        unlu_sayisi +=1
print('Ünlü harf sayısı:',unlu_sayisi)


# In[8]:


cumle = input("Lütfen bir cümle girin: ")
unlu_sayisi = 0
unluler = "aeıioöuüAEIİOÖUÜ"

for harf in cumle:
    if harf in unluler: 
        unlu_sayisi +=1
print(f"Girdiğiniz cümledeki ünlü harf sayısı: {unlu_sayisi}")


# # Karakter Sayısı Sayma

# In[11]:


cumle = input("Bir cümle giriniz: ")
print(len(cumle))


# # Faktöriyel Hesaplama

# In[15]:


sayi = int(input("Faktöriyelinin alınmasını istediğiniz sayıyı giriniz: "))
faktoriyel = 1
for i in range(1,sayi+1):
    faktoriyel *= i
print(f"{sayi}!={faktoriyel}")


# # Kelime Ters Çevirme

# In[16]:


kelime = input("Lütfen bir kelime giriniz: ")
tersi = kelime[::-1]
print("Kelimenin tersi: ", tersi)


# # Asal sayıları bulma

# In[22]:


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


# In[23]:


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

# In[25]:


liste = [3,64,8,2,7558,87,75,5643,1]
liste.sort()
print("Listenin sıralı hali şu şekildedir: ", liste)


# In[26]:


liste = ["f","g","m","j"]
liste.sort()
print("Listenin sıralı hali şu şekildedir: ", liste)


# In[ ]:




