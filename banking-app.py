def bakiye_goster():
    print(f"Mevcut bakiyeniz ₺{bakiye}")
def para_yatir():
    tutar = float(input("Yatirmak istediginiz tutari giriniz: "))

    if tutar < 0 :
        print("Gecersiz islem")
        return 0
    else:
        return tutar

def para_cek():
    tutar = float(input("Çekmek istediginiz tutari giriniz: "))

    if tutar > bakiye:
        print("Gecersiz islem")
        return 0
    else:
        return tutar

anlik_calisiyor = True
bakiye = 0


while anlik_calisiyor:
    print("Banka Uygulamasi")
    print("1-Bakiye Goster")
    print("2-Para Yatir")
    print("3-Para Çek")
    print("4-Çikiş Yap")

    secim = input("Bir işlem seçiniz (1-4): ")

    if secim == "1":
        bakiye_goster()
    elif secim =="2":
        bakiye += para_yatir()
    elif secim =="3":
        bakiye -= para_cek()
    elif secim =="4":
        anlik_calisiyor = False
    else:
        break