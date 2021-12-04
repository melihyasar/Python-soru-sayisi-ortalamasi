import os
def gırıs(message):#kullanıcıya sayısal veri girişi sormak için fonksiyon
    try:#kullanıcı sayısal değer girer ise sorun yok
        deger = int(input(message))
        return deger 
    except:#kullanıcı sayısal değer girmez ise(abc gibi bir değer girerse) sayısal veri girmesi için sor
        return gırıs("lütfen sayı giriniz: ")

def gırıs2(message2):#kullanıcıya sayısal veri girişi sormak için 2. fonksiyon.Yukarıdakinin aynısı
    try:
        deger2 = int(input(message2))
        return deger2
    except:
        return gırıs2("lütfen sayı giriniz: ")



cwd = os.getcwd() #cwd = mevcut çalışma konumu(.py dosyasının içinde bulunduğu klasör)
cwd2 = cwd + "\soru sayısı" #cwd2 = \soru sayısı klasörünü konumu
cwdss = cwd2 + "\soru_sayisi.txt" #cwdss = \soru sayısı\soru_sayisi.txt dosyasının konumu
cwdgs = cwd2 + "\gun_sayisi.txt"  #cwdgs = \soru sayısı\gun_sayisi.txt dosyasının konumu
cwdh = cwd2 + "\hedef.txt"     #cwdh = \soru sayısı\hedef.txt dosyasının konumu
print("Soru sayısı ortalaması hesaplayıcı")
f = open(cwdh, 'r')
hedef = f.read()
f.close()
print("Mevcut hedefiniz " + hedef)
if int(hedef) > 0: #mevcut hedef var mı kontrol et
  print()
else:
 
 hedef = gırıs2("lütfen hedef belirleyin: ") #eğer yoksa hedef belirlemesini sor
 f = open(cwdh, 'w')
 f.write(str(hedef)) 
 f.close()
 print("Mevcut hedefiniz " + str(hedef))

 

sorusayisi = gırıs("bu günkü soru sayınızı giriniz: ")

f= open(cwdss, 'r') #toplam soru sayısı ile bu günkü soru sayısını toplayıp "cwdss"ye yaz
x= f.read()
y = int(x) + int(sorusayisi)
z = str(y)
f.close()
f = open(cwdss, 'w')
f.write(z)
f.close()
 
  
f = open(cwdgs, 'r')# toplam gün sayısını al ve 1 ekle
q = f.read()
m = int(q) + 1 
n = str(m)
f.close()
f = open(cwdgs, 'w')
f.write(n)
f.close()
 

ortalama = y/m #toplam soru sayısını toplam gün sayısına böl
print("Ortalamanız günlük " + str(ortalama) + " soru.")# ortalamayı yazdır

#ortalama hedefin altında mı üstünde mi hedefi tutturuyor mu yazdır
if ortalama < int(hedef):
    print("hedefinizin altındasınız!")
if ortalama == int(hedef):
   print("hedefi tuturuyorsunuz!")
if ortalama > int(hedef):
    print("hedefinizin üstündesiniz!")
print()
 
print("Ortalamayı sıfırlamak için 1, hedefi sıfırlamak için 2, ikisini de sıfırlamak için 3 yazın.")
b = input("Programı kapatmak için hiçbirşey yazmadan enter a basınız ")#kullanıcıya hedef-ortalama veya ikisini de sıfırlamak isteyip istemediğini sor
if b == "1":#ortalamayı sıfırlamak için
    f = open(cwdss, 'w')#"cwdss"yi sıfırla
    f.write("0")
    f.close()
    f = open(cwdgs, 'w')#"cwdgs"yi sıfırla
    f.write("0")
    f.close()
    print("Ortalama sıfırlandı")
    input("Kapatmak için hiçbirşey yazmadan enter a basınız ")
elif b == "2":#hedefi sıfırlamak için
    f = open(cwdh, 'w')#"cwdh"yi sıfırla
    f.write("0")
    f.close()
    print("Hedef sıfırlandı")
    input("Kapatmak için hiçbirşey yazmadan enter a basınız ")
elif b =="3":#her ikisini de sıfırlamak için
    f = open(cwdss, 'w')#"cwdss"yi sıfırla
    f.write("0")
    f.close()
    f = open(cwdgs, 'w')#"cwdgs"yi sıfırla
    f.write("0")
    f.close()
    f = open(cwdh, 'w')#"cwdh"yi sıfırla
    f.write("0")
    f.close()
    print("Hedef ve ortalama sıfırlandı")
    input("Kapatmak için hiçbirşey yazmadan enter a basınız ")
    #Melih Yaşar












