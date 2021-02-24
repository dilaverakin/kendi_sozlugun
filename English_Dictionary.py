from time import sleep
import random
liste = []
ing_sozluk = {}  # türkçe anlamını veririyor
turk_sozluk = {}  # ingilizce anlamını veriyor
rastgele_turk=[]
rastgele_ing=[]

def sozluk(): #dosyadaki kelimeleri okuyup sözlüklere atıyor
    with open("Words.txt", "r") as file:
        for i in file.readlines():  # dosyayı readlines foncıyonu ile satır satır okuyor
            i = i[:-1]
            i = i.split("=")
            liste.append(i)
        for i in range(0, len(liste)):
            ing_sozluk[liste[i][0]] = liste[i][1]  # burda sozluge ekleme yapılıyor
            turk_sozluk[liste[i][1]] = liste[i][0]
def test(kelime,islem):
    try:
        if islem == "1":
            return ing_sozluk[kelime]
        elif islem == "2":
            return turk_sozluk[kelime]
    except KeyError:
        print("Böyle Bir Kelime Bulunmuyor")
def yazdır(kelime,anlamı): #sözlüğümüze yeni kelime ekliyor
    print("Kelime ekleniyor...")
    sleep(1)
    with open("Words.txt","a") as ekle:
        ekle.write(kelime)
        ekle.write("=")
        ekle.write(anlamı)
        ekle.write("\n")
    print("Kelimeniz Başariyla eklendi")
def rastgele():
    c=0
    with open("Words.txt", "r") as file:
        for i in file.readlines():  # dosyayı readline foncıyonu ile satır satır okuyor
            i = i[:-1]
            i = i.split("=")
            liste.append(i)
            a,b = 0,1
            rastgele_turk.append(liste[c][a])
            rastgele_ing.append(liste[c][b])
            c+=1

print("-"*60,"""\n\t\tTürkçeden ingilizceye ceviren sözlük için '1'e Basın \n
\t\tİngilizceden Türkçeye çeviren sözlük için '2'e Basın\n
\t\tKelime eklemek için '3'e Basın\n
\t\tKelime Oyunu için '4'e Basın\n
\t\tÇıkmak için 'q' Basın\n""","-"*60)
sozluk()
while True:
    islem = input("Hangi sözlüğü istiyorsunuz ------->>> ")
    if islem=="q":
        print("Bilgiler kaydediliyor ....")
        sleep(1)
        print ("Sistem kapatılıyor...")
        sleep(1)
        print ("Sistem Kapatıldı.")
        break
    elif islem=="1":
        print("Çıkmak için 'q'a Basın \t\t<<<--->>>\t\tİNGİLİZCE ANLAMINI VERİR..")
        while True:
            kelime = input("kelimeyi giriniz : ")
            if kelime == "q":
                break
            anlamı = test(kelime, islem)
            if anlamı==None: #değer None olarak dönerse hiçbir işlem yapmadan döngünün başına dönüyor
                continue
            print ("ingilizce anlamı : ",anlamı)
    elif islem=="2":
        print("Çıkmak için 'q'a Basın \t\t<<<--->>>\t\tTÜRKÇE ANLAMINI VERİR..")
        while True:
            kelime = input("kelimeyi giriniz : ")
            if kelime == "q":
                break
            anlamı = test(kelime,islem)
            if anlamı==None:
                continue
            print("Türkçe anlamı : ",anlamı)
    elif islem=="3":
        print("*** ÇIKMAK İÇİN 'q'a BASIN ***")
        while True:
            kelime= input("Kelimenin  Türkçesini  Buraya  giriniz : ")
            if kelime=="q":
                break
            anlamı= input("Kelimenin İngilizcesini Buraya giriniz : ")
            yazdır(kelime,anlamı)
    elif islem=="4":
        print("""\t\t\t\t***  Merhaba Hoşgeldin  ***\n
        Hadi Zaman Kaybetmeden Oyuna Başlıyalım\n""","-"*50)
        while True:
            istek = input("Türkçe Sözlük için '1'e Basın\nİngilizce Sözlük için '2'e Basın\nÇıkmak için 'q'a Basın --->>> ")
            if istek=="q":
                break
            elif istek=="1":
                while True:
                    sayı = random.randint(0,len(rastgele_turk))
                    rastgele()
                    cevap=input ("\t\t*** {}***\nKelimesinin İngilizcesi Nedir : ".format(rastgele_turk[sayı]))
                    if cevap=="q":
                        break
                    elif cevap==rastgele_ing[sayı]:
                        print("Tebrikler Bildiniz..\n")
                    else:
                        print("Yanlış Cevap daha Çok çalışman gerek...")
                        print("Doğru Cevap : ",rastgele_ing[sayı])
            elif istek=="2":
                while True:
                    sayı = random.randint(0, len(rastgele_turk))
                    rastgele()
                    cevap = input("\t\t*** {}***\nKelimesinin İngilizcesi Nedir : ".format(rastgele_ing[sayı]))
                    if cevap == "q":
                        break
                    elif cevap == rastgele_turk[sayı]:
                        print("Tebrikler Bildiniz..\n")
                    else:
                        print("Yanlış Cevap daha Çok çalışman gerek...")
                        print("Doğru Cevap : ",rastgele_turk[sayı])


    else:
        print("***Lütfen Geçerli Bir İşlem Giriniz***")
        continue