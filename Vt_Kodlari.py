import sqlite3

conn = sqlite3.connect("otomasyon.db")

cursor = conn.cursor()


class TabloCreate:

    def create_ogrenci(self):
        cursor.execute(
            'CREATE TABLE "ogrenci" ("ID"	INTEGER,"adi"	TEXT,"soyadi"	TEXT,"bolumu"	TEXT,PRIMARY KEY("ID" AUTOINCREMENT))')
        conn.commit()

    def create_notlar(self):
        cursor.execute(
            'CREATE TABLE "notlar" ("ID"	INTEGER,"OgrenciID"	INTEGER,"Vize"	INTEGER,"Final"	INTEGER,"Ortalama"	INTEGER,"HarfNotu"	TEXT,"DersAdi"	TEXT,PRIMARY KEY("ID" AUTOINCREMENT))')
        conn.commit()



# Öğrenci ekleme fonksiyonu
class Create:
    def Ogrenci_Kayit(self):
        sayi = int(input("Girmek istediğiniz öğrenci sayısını giriniz: "))
        for i in range(sayi):
            Adi = input("Öğrencinin adını giriniz: ")
            Soyadi = input("Öğrencinin soyadını giriniz: ")
            Bolum = input("Öğrencinin bölümünü giriniz: ")
            cursor.execute('INSERT INTO ogrenci (adi, soyadi, bolumu) VALUES (?, ?, ?)', (Adi, Soyadi, Bolum))
            conn.commit()
            print("Girilen öğrenci bilgisi kaydedildi.")

    # Not Ekleme İşlemleri
    def Ogrenci_Not_Kayit(self):
        OgrenciID = int(input("öğrenci ID giriniz:"))
        ders_adi = input("dersin adını giriniz:")
        vize = int(input("vize notunuzu giriniz:"))
        final = int(input("final notunuzu giriniz:"))
        ort = int(vize + final) / 2
        if ort > 70:
            harfnotu = "AA"
        elif ort < 70:
            harfnotu = "FF"
        else:
            print("geçersiz bir rakam girdiniz.")
        cursor.execute(
            "INSERT INTO notlar (OgrenciID, Vize, Final, Ortalama, 'HarfNotu','DersAdi') VALUES (?,?,?,?,?,?)",
            (OgrenciID, vize, final, ort, harfnotu, ders_adi))
        conn.commit()
        print("kayıt başarılı şekilde eklenmiştir.")

class Read:
    # Öğrenci Listeleme
    def Ogrenci_Listele(self):
        cursor.execute('SELECT * FROM ogrenci')
        ogrenciler = cursor.fetchall()
        for i in ogrenciler:
            print(i)

    # Arama yapılarak öğrenci listeleme
    def Ogrenci_Listele_Detay(self):
        ad = input("Aratmak istediğiniz öğrencinin adını giriniz: ")
        cursor.execute("SELECT * FROM ogrenci WHERE adi= ?", (ad,))
        data = cursor.fetchall()
        for i in data:
            print(i)

    # Not Listeleme
    def Not_Listele(self):
        cursor.execute('SELECT * FROM notlar')
        notlar = cursor.fetchall()
        for i in notlar:
            print(i)

    # Arama yapılarak not listeleme
    def Not_Listele_Detay(self):
        dersAd = input("Aratmak istediğiniz dersin adını giriniz: ")
        cursor.execute("SELECT * FROM notlar WHERE DersAdi= ?", (dersAd,))
        data = cursor.fetchall()
        for i in data:
            print(i)

class Delete:
    # Öğrenci Silme
    def Ogrenci_Sil(self):
        ogrenciId = int(input("Silmek istediğiniz Öğrencinin ID'sini giriniz: "))
        cursor.execute('DELETE FROM ogrenci WHERE ID=?', (ogrenciId,))
        conn.commit()
        print('Kayıt başarıyla silindi!')

    # Not Silme
    def Not_Sil(self):
        notId = int(input("Silmek istediğiniz Öğrenci notunun ID'sini giriniz: "))
        cursor.execute('DELETE FROM notlar WHERE ID=?', (notId,))
        conn.commit()
        print('Kayıt başarıyla silindi!')

class Update:
    # Öğrenciler için güncelleme fonksiyonu
    def Ogrenci_Adi_Guncelle(self):
        ad = input("Yeni girmek istediğiniz ismi giriniz: ")
        ID = int(input("Güncellemek istediğiniz öğrencinin ID'sini giriniz: "))
        cursor.execute('UPDATE ogrenci SET adi=? WHERE ID=?', (ad, ID))
        conn.commit()
        print('Güncelleme başarılı!')

    def Ogrenci_Soyadi_Guncelle(self):
        soyad = input("Yeni girmek istediğiniz soyadı giriniz: ")
        ID = int(input("Güncellemek istediğiniz öğrencinin ID'sini giriniz: "))
        cursor.execute('UPDATE ogrenci SET soyadi=? WHERE ID=?', (soyad, ID))
        conn.commit()
        print("Güncelleme başarılı!")

    def Ogrenci_Bolumu_Guncelleme(self):
        bolum = input("Güncellemek istediğiniz öğrencinin bölümünü giriniz: ")
        ID = int(input("Güncellemek istediğiniz öğrencinin ID'sini giriniz: "))
        cursor.execute('UPDATE ogrenci SET bolumu=? WHERE ID=?', (bolum, ID))
        conn.commit()
        print('Güncelleme başarılı!')

    def OgrenciToplu_Guncelleme(self):
        ID = int(input("Güncellemek istediğiniz öğrencinin ID'sini giriniz: "))
        secim = input("Ögrencinin adını değiştirmek için 'adi' Soyadını değiştirmek  için 'soyadi' Bolümünü Değiştirmek içni 'bolumu' yazınız: ")
        if secim == 'adi':
            ad = input("Lütfen yeni adı giriniz: ")
            cursor.execute('UPDATE ogrenci SET ' + secim + ' =? WHERE ID=?', (ad, ID))
        elif secim == 'soyadi':
            soyad = input("Lütfen yeni soyadi giriniz: ")
            cursor.execute('UPDATE ogrenci SET ' + secim + ' =? WHERE ID=?', (soyad, ID))
        elif secim == 'bolumu':
            bolum = input("Lütfen yeni bölümü giriniz: ")
            cursor.execute('UPDATE ogrenci SET ' + secim + ' =? WHERE ID=?', (bolum, ID))
        else:
            print("Yanlış bir değer girdiniz.")
        conn.commit()
        print("İşlem Başarılı Olmuştur.")

    # Öğrenci Notları için güncelleme fonksiyonu
    def Ders_Adi_Guncelle(self):
        ad = input("Yeni girmek istediğiniz ders adını giriniz: ")
        ID = int(input("Güncellemek istediğiniz dersin ID'sini girin: "))
        cursor.execute("UPDATE notlar SET DersAdi=? WHERE ID=?", (ad, ID))
        conn.commit()
        print("Güncelleme başarılı!")

    def Vize_Not_Guncelle(self):
        vize = int(input("Yeni girmek istediğiniz vize notunu giriniz: "))
        ID = int(input("Güncellemek istediğiniz öğrencinin ID'sini girin: "))
        cursor.execute("UPDATE notlar SET Vize=? WHERE ID=?", (vize, ID))
        conn.commit()
        print("Güncelleme başarılı!")

        # Ortalama ve Harf Notu Güncelleme
        cursor.execute("SELECT Vize, Final, Ortalama FROM notlar WHERE ID=?", (ID,))
        result = cursor.fetchone()
        vize = result[0]
        final = result[1]

        ort = int(vize + final) / 2
        if ort > 70:
            harfnotu = "AA"
        elif ort < 70:
            harfnotu = "FF"
        else:
            print("geçersiz bir rakam girdiniz.")

        cursor.execute("UPDATE notlar SET Ortalama=?, HarfNotu=? WHERE ID=?", (ort, harfnotu, ID))
        conn.commit()
        print("Ortalama ve Harf Notu güncellendi.")

    def Final_Not_Guncelle(self):
        final = int(input("Yeni girmek istediğiniz final notunu giriniz: "))
        ID = int(input("Güncellemek istediğiniz öğrencinin ID'sini girin: "))
        cursor.execute("UPDATE notlar SET Final=? WHERE ID=?", (final, ID))
        conn.commit()
        print("Güncelleme başarılı!")

        # Ortalama ve Harf Notu Güncelleme
        cursor.execute("SELECT Vize, Final, Ortalama FROM notlar WHERE ID=?", (ID,))
        result = cursor.fetchone()
        vize = result[0]
        final = result[1]

        ort = int(vize + final) / 2
        if ort > 70:
            harfnotu = "AA"
        elif ort < 70:
            harfnotu = "FF"
        else:
            print("geçersiz bir rakam girdiniz.")

        cursor.execute("UPDATE notlar SET Ortalama=?, HarfNotu=? WHERE ID=?", (ort, harfnotu, ID))
        conn.commit()
        print("Ortalama ve Harf Notu güncellendi.")


