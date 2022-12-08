#Bu kısımda kullanıcıdan bir gelir girilmesini istiyoruz.
gelir = float(input("Lütfen bir gelir giriniz: "))

#Bu kısımda kurumlar vergisi oranını belirtiyoruz.
vergi_oranı = 0.15

#Bu kısımda gelirin vergiye tabi tutarlarını hesaplıyoruz.
vergiye_tabi_tutar = gelir * vergi_oranı

#Bu kısımda hesaplanan vergi tutarını ekrana yazdırıyoruz.
print("Vergi tutarı:", vergiye_tabi_tutar)
