import os
def gırıs(message):
    try:
        deger = int(input(message))
        return deger
    except:
        return gırıs("lütfen sayı giriniz: ")

def gırıs2(message2):
    try:
        deger2 = int(input(message2))
        return deger2
    except:
        return gırıs2("lütfen sayı giriniz: ")



cwd = os.getcwd()
cwd2 = cwd + "\soru sayısı"
cwdss = cwd2 + "\soru_sayisi.txt"
cwdgs = cwd2 + "\gun_sayisi.txt"
cwdh = cwd2 + "\hedef.txt"
print("Soru sayısı ortalaması hesaplayıcı")
f = open(cwdh, 'r')
hedef = f.read()
f.close()
print("Mevcut hedefiniz " + hedef)
if int(hedef) > 0:
  print()
else:
 
 hedef = gırıs2("lütfen hedef belirleyin: ")
 f = open(cwdh, 'w')
 f.write(str(hedef))
 f.close()
 print("Mevcut hedefiniz " + str(hedef))

 

sorusayisi = gırıs("bu günkü soru sayınızı giriniz: ")

f= open(cwdss, 'r')
x= f.read()
y = int(x) + int(sorusayisi)
z = str(y)
f.close()
f = open(cwdss, 'w')
f.write(z)
f.close()
 
  
f = open(cwdgs, 'r')
q = f.read()
m = int(q) + 1 
n = str(m)
f.close()
f = open(cwdgs, 'w')
f.write(n)
f.close()
 

ortalama = y/m
print("Ortalamanız günlük " + str(ortalama) + " soru.")
if ortalama < int(hedef):
    print("hedefinizin altındasınız!")
if ortalama == int(hedef):
   print("hedefi tuturuyorsunuz!")
if ortalama > int(hedef):
    print("hedefinizin üstündesiniz!")
print()
 
print("Ortalamayı sıfırlamak için 1, hedefi sıfırlamak için 2, ikisini de sıfırlamak için 3 yazın.")
b = input("Programı kapatmak için hiçbirşey yazmadan enter a basınız ")
if b == "1":
    f = open(cwdss, 'w')
    f.write("0")
    f.close()
    f = open(cwdgs, 'w')
    f.write("0")
    f.close()
    print("Ortalama sıfırlandı")
    input("Kapatmak için hiçbirşey yazmadan enter a basınız ")
elif b == "2":
    f = open(cwdh, 'w')
    f.write("0")
    f.close()
    print("Hedef sıfırlandı")
    input("Kapatmak için hiçbirşey yazmadan enter a basınız ")
elif b =="3":
    f = open(cwdss, 'w')
    f.write("0")
    f.close()
    f = open(cwdgs, 'w')
    f.write("0")
    f.close()
    f = open(cwdh, 'w')
    f.write("0")
    f.close()
    print("Hedef ve ortalama sıfırlandı")
    input("Kapatmak için hiçbirşey yazmadan enter a basınız ")
    #Melih Yaşar












