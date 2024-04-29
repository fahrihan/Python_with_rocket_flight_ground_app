import serial
import time


def veri_bol(com_deger,deger):
    istasyon_alici = serial.Serial(port=com_deger, baudrate=115200, stopbits=1)

    gelen_veriler = istasyon_alici.readline()

    if deger ==1:
        cevirici = str(gelen_veriler)

        deger_liste = cevirici.split()

        irtifa_Roket = float(deger_liste[1])
        irtifa_Roket_GPS = float(deger_liste[2])
        Roket_GPS_enlem = float(deger_liste[3])
        Roket_GPS_boylam = float(deger_liste[4])

        Roket_uydu = int(deger_liste[5])

        Roket_X_ekseni = int(deger_liste[6])
        Roket_Y_ekseni = int(deger_liste[7])
        Roket_Z_ekseni = int(deger_liste[8])

        Payload_GPS_irtifa = float(deger_liste[9])
        Payload_GPS_enlem = float(deger_liste[10])
        Payload_GPS_boylam = float(deger_liste[11])

        Payload_uydu = int(deger_liste[12])

        Roket_durum = int(deger_liste[13])

        Sayac = 55
        Takim_id = 253

        gonderilecek_veri = (irtifa_Roket,irtifa_Roket_GPS,Roket_GPS_enlem,Roket_GPS_boylam,Roket_uydu,Roket_X_ekseni,Roket_Y_ekseni,Roket_Z_ekseni,Payload_GPS_irtifa,Payload_GPS_enlem,Payload_GPS_boylam,Payload_uydu,Roket_durum,Sayac,Takim_id)
        print(Roket_GPS_enlem)
        return gonderilecek_veri

    if deger ==2:
        cevirici = str(gelen_veriler)

        deger_liste = cevirici.split()

        irtifa_Roket = float(deger_liste[1])
        irtifa_Roket_GPS = float(deger_liste[2])
        Roket_GPS_enlem = float(deger_liste[3])
        Roket_GPS_boylam = float(deger_liste[4])

        Roket_uydu = int(deger_liste[5])

        Roket_X_ekseni = int(deger_liste[6])
        Roket_Y_ekseni = int(deger_liste[7])
        Roket_Z_ekseni = int(deger_liste[8])

        Payload_GPS_irtifa = float(deger_liste[9])
        Payload_GPS_enlem = float(deger_liste[10])
        Payload_GPS_boylam = float(deger_liste[11])

        Payload_uydu = int(deger_liste[12])

        Roket_durum = int(deger_liste[13])

        Sayac = int(deger_liste[14])

        Takim_id = int(deger_liste[15])

        gonderilecek_veri = (
        irtifa_Roket, irtifa_Roket_GPS, Roket_GPS_enlem, Roket_GPS_boylam, Roket_X_ekseni, Roket_Y_ekseni,
        Roket_Z_ekseni, Payload_GPS_irtifa, Payload_GPS_enlem, Payload_GPS_boylam, Roket_durum, Sayac, Takim_id)

        return gonderilecek_veri