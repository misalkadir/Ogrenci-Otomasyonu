import Vt_Kodlari

# Proje ilk oluşturulduğunda tablolar oluşturulmak için aşağıdaki kodları kullandık.
# Vt_Kodlari.create_ogrenci()
# Vt_Kodlari.create_notlar()
# obj = Vt_Kodlari.TabloCreate()
# obj.create_ogrenci()

create = Vt_Kodlari.Create()
read = Vt_Kodlari.Read()
update = Vt_Kodlari.Update()
delete = Vt_Kodlari.Delete()

while True:
    query = int(input("Öğrenci islemleri icin 1'e, not islemleri icin 2'ye, çıkmak için 3'e basınız: "))

    # ÖĞRENCİ İŞLEMLERİ(query=soru/sorgu, sub_query=alt_sorgu, value=değer, option=seçim,seçenek)
    if query == 1:
        while True:
            sub_query = int(input(
                "Öğrenci eklemek için 1'e silmek için 2'ye güncellemek için 3'e basınız çıkmak için 4'e basınız: "))
            if sub_query == 1:
                create.Ogrenci_Kayit()
            elif sub_query == 2:
                option = int(input("Listeleterek silmek için 1'e Aratarak silmek için 2'ye basın: "))
                if option == 1:
                    read.Ogrenci_Listele()
                    delete.Ogrenci_Sil()
                elif option == 2:
                    read.Ogrenci_Listele_Detay()
                    delete.Ogrenci_Sil()
                else:
                    print("Yanlış giriş yaptınız.")
            elif sub_query == 3:
                value = int(input(
                    "Öğrenci adı güncellemek için 1'e, soyadı için 2'ye,bölümü için 3'e basınız.Hepsini birden güncellemek için 4'e basınız: "))
                if value == 1:
                    print("Güncelleme işlemi için aşağıdaki öğrencilerden birinin ID'sini seçebilirsiniz.")
                    read.Ogrenci_Listele()
                    update.Ogrenci_Adi_Guncelle()
                    print('Güncellenen öğrenci listesi verilmiştir.')
                    read.Ogrenci_Listele()
                elif value == 2:
                    print("Güncelleme işlemi için aşağıdaki öğrencilerden birinin ID'sini seçebilirsiniz.")
                    read.Ogrenci_Listele()
                    update.Ogrenci_Soyadi_Guncelle()
                    print('Güncellenen öğrenci listesi verilmiştir.')
                    read.Ogrenci_Listele()
                elif value == 3:
                    print("Güncelleme işlemi için aşağıdaki öğrencilerden birinin ID'sini seçebilirsiniz.")
                    read.Ogrenci_Listele()
                    update.Ogrenci_Bolumu_Guncelleme()
                    print('Güncellenen öğrenci listesi verilmiştir.')
                    read.Ogrenci_Listele()
                elif value == 4:
                    print("Güncelleme işlemi için aşağıdaki öğrencilerden birinin ID'sini seçebilirsiniz.")
                    read.Ogrenci_Listele()
                    update.OgrenciToplu_Guncelleme()
                    print('Güncellenen Liste verilmiştir.')
                    read.Ogrenci_Listele()
                else:
                    print("Yanlış değer girdiniz.")
            elif sub_query == 4:
                print("öğrenci işlemi yapmak istemediniz ana menüye yönlendiriliyorsunuz.")
                break
            else:
                print("Geçerli bir seçim yapmadınız tekrar deneyiniz.")
                continue

    # NOT İŞLEMLERİ
    elif query == 2:
        while True:
            sub_query = int(input("Notlar eklemek için 1'e silmek için 2'ye güncellemek için 3'e basınız çıkmak için 4'e basınız: "))
            if sub_query == 1:
                print("Aşağıdaki öğrenci listesine göre işlem yapmalısınız.")
                read.Ogrenci_Listele()
                create.Ogrenci_Not_Kayit()
            elif sub_query == 2:
                option = int(input("Listeleterek silmek için 1'e Aratarak silmek için 2'ye basın: "))
                if option == 1:
                    read.Not_Listele()
                    delete.Not_Sil()
                elif option == 2:
                    read.Not_Listele_Detay()
                    delete.Not_Sil()
                else:
                    print("Hatalı işlem yaptınız.")
                read.Not_Listele()
            elif sub_query == 3:
                value = int(input(
                    "Ders Adı güncellemek için 1'e, Vize notu için 2'ye, Final notu için 3'e basınız. Hepsini birden güncellemek için 4'e basınız: "))
                if value == 1:
                    print("Güncelleme işlemi için aşağıdaki Notlardan birinin ID'sini seçebilirsiniz.")
                    read.Not_Listele()
                    update.Ders_Adi_Guncelle()
                    print('Güncellenen not listesi verilmiştir.')
                    read.Not_Listele()
                elif value == 2:
                    print("Güncelleme işlemi için aşağıdaki Notlardan birinin ID'sini seçebilirsiniz.")
                    read.Not_Listele()
                    update.Vize_Not_Guncelle()
                    print('Güncellenen not listesi verilmiştir.')
                    read.Not_Listele()
                elif value == 3:
                    print("Güncelleme işlemi için aşağıdaki Notlardan birinin ID'sini seçebilirsiniz.")
                    read.Not_Listele()
                    update.Final_Not_Guncelle()
                    print('Güncellenen not listesi verilmiştir.')
                    read.Not_Listele()
                else:
                    print("Yanlış değer girdiniz")
            elif sub_query == 4:
                print("Not işlemi yapmak istemediniz ana menüye yönlendiriliyorsunuz.")
                break
            else:
                print("Geçerli bir seçim yapmadınız tekrar deneyiniz.")
                continue

    # PROGRAMDAN ÇIKIŞ
    elif query == 3:
        print("\nHoşçakalın")
        break
    elif query == 4:
        read.Ogrenci_Listele()
    else:
        print("Geçerli bir sayı girmediniz lütfen tekrar deneyin.")
        continue
