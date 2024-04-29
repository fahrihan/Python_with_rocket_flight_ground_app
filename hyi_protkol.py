import struct

def sayi_byte_cevir(sayi_d):

    sayi = bytearray(struct.pack("f", sayi_d))

    gecici_degisken = ["0x%02x" % i for i in sayi]

    degisken1 = gecici_degisken[0]
    degisken2 = gecici_degisken[1]
    degisken3 = gecici_degisken[2]
    degisken4 = gecici_degisken[3]

    degisken1 = int(degisken1,0)
    degisken2 = int(degisken2,0)
    degisken3 = int(degisken3,0)
    degisken4 = int(degisken4,0)

    return  degisken1,degisken2,degisken3,degisken4


def yer_istasyonu_protokol(irtifa_Roket_y,irtifa_Roket_GPS_y,Roket_GPS_enlem_y,Roket_GPS_boylam_y,Roket_X_ekseni_y,Roket_Y_ekseni_y,Roket_Z_ekseni_y,Payload_GPS_irtifa_y,Payload_GPS_enlem_y,Payload_GPS_boylam_y,Sayac_y,Durum_y,Takim_id_y):


    irtifa_Roket = irtifa_Roket_y
    irtifa_Roket_GPS = irtifa_Roket_GPS_y
    Roket_GPS_enlem = Roket_GPS_enlem_y
    Roket_GPS_boylam = Roket_GPS_boylam_y
    Payload_GPS_irtifa = Payload_GPS_irtifa_y
    Payload_GPS_enlem = Payload_GPS_enlem_y
    Payload_GPS_boylam = Payload_GPS_boylam_y

    Takim_id =Takim_id_y
    Sayac = Sayac_y

    Kademe_GPS_irtifa = 0x00
    Kademe_GPS_enlem = 0x00
    Kademe_GPS_boylam = 0x00
    Jriskop_X = Roket_X_ekseni_y
    Jriskop_Y = Roket_Y_ekseni_y
    Jriskop_Z = Roket_Z_ekseni_y
    ivme_X = 0x00
    ivme_Y = 0x00
    ivme_Z = 0x00
    aci = 0x00

    Durum = Durum_y

    olusturalacak_paket = bytearray(range(0, 78))





    olusturalacak_paket[0] = 0xff
    olusturalacak_paket[1] = 0xff
    olusturalacak_paket[2] = 0x54
    olusturalacak_paket[3] = 0x52
    olusturalacak_paket[4] = Takim_id     #Takım id
    olusturalacak_paket[5] = Sayac      #Sayac_degeri

    irtifa_Roket_cevrilmis = sayi_byte_cevir(irtifa_Roket)

    olusturalacak_paket[6] = irtifa_Roket_cevrilmis[0]
    olusturalacak_paket[7] = irtifa_Roket_cevrilmis[1]
    olusturalacak_paket[8] = irtifa_Roket_cevrilmis[2]
    olusturalacak_paket[9] = irtifa_Roket_cevrilmis[3]


    irtifa_Roket_GPS_cevrilmis = sayi_byte_cevir(irtifa_Roket_GPS)

    olusturalacak_paket[10] = irtifa_Roket_GPS_cevrilmis[0]
    olusturalacak_paket[11] = irtifa_Roket_GPS_cevrilmis[1]
    olusturalacak_paket[12] = irtifa_Roket_GPS_cevrilmis[2]
    olusturalacak_paket[13] = irtifa_Roket_GPS_cevrilmis[3]


    Roket_GPS_enlem_cevrilmis = sayi_byte_cevir(Roket_GPS_enlem)

    olusturalacak_paket[14] = Roket_GPS_enlem_cevrilmis[0]
    olusturalacak_paket[15] = Roket_GPS_enlem_cevrilmis[1]
    olusturalacak_paket[16] = Roket_GPS_enlem_cevrilmis[2]
    olusturalacak_paket[17] = Roket_GPS_enlem_cevrilmis[3]




    Roket_GPS_boylam_cevrilmis = sayi_byte_cevir(Roket_GPS_boylam)

    olusturalacak_paket[18] = Roket_GPS_boylam_cevrilmis[0]
    olusturalacak_paket[19] = Roket_GPS_boylam_cevrilmis[1]
    olusturalacak_paket[20] = Roket_GPS_boylam_cevrilmis[2]
    olusturalacak_paket[21] = Roket_GPS_boylam_cevrilmis[3]



    Payload_GPS_irtifa_cevrilmis = sayi_byte_cevir(Payload_GPS_irtifa)

    olusturalacak_paket[22] = Payload_GPS_irtifa_cevrilmis[0]
    olusturalacak_paket[23] = Payload_GPS_irtifa_cevrilmis[1]
    olusturalacak_paket[24] = Payload_GPS_irtifa_cevrilmis[2]
    olusturalacak_paket[25] = Payload_GPS_irtifa_cevrilmis[3]




    Payload_GPS_enlem_cevrilmis = sayi_byte_cevir(Payload_GPS_enlem)

    olusturalacak_paket[26] = Payload_GPS_enlem_cevrilmis[0]
    olusturalacak_paket[27] = Payload_GPS_enlem_cevrilmis[1]
    olusturalacak_paket[28] = Payload_GPS_enlem_cevrilmis[2]
    olusturalacak_paket[29] = Payload_GPS_enlem_cevrilmis[3]



    Payload_GPS_boylam_cevrilmis = sayi_byte_cevir(Payload_GPS_boylam)

    olusturalacak_paket[30] = Payload_GPS_boylam_cevrilmis[0]
    olusturalacak_paket[31] = Payload_GPS_boylam_cevrilmis[1]
    olusturalacak_paket[32] = Payload_GPS_boylam_cevrilmis[2]
    olusturalacak_paket[33] = Payload_GPS_boylam_cevrilmis[3]



    Kademe_GPS_irtifa_cevrilmis = sayi_byte_cevir(Kademe_GPS_irtifa)

    olusturalacak_paket[34] = Kademe_GPS_irtifa_cevrilmis[0]
    olusturalacak_paket[35] = Kademe_GPS_irtifa_cevrilmis[1]
    olusturalacak_paket[36] = Kademe_GPS_irtifa_cevrilmis[2]
    olusturalacak_paket[37] = Kademe_GPS_irtifa_cevrilmis[3]





    Kademe_GPS_enlem_cevrilmis = sayi_byte_cevir(Kademe_GPS_enlem)

    olusturalacak_paket[38] = Kademe_GPS_enlem_cevrilmis[0]
    olusturalacak_paket[39] = Kademe_GPS_enlem_cevrilmis[1]
    olusturalacak_paket[40] = Kademe_GPS_enlem_cevrilmis[2]
    olusturalacak_paket[41] = Kademe_GPS_enlem_cevrilmis[3]



    Kademe_GPS_boylam_cevrilmis = sayi_byte_cevir(Kademe_GPS_boylam)

    olusturalacak_paket[42] = Kademe_GPS_boylam_cevrilmis[0]
    olusturalacak_paket[43] = Kademe_GPS_boylam_cevrilmis[1]
    olusturalacak_paket[44] = Kademe_GPS_boylam_cevrilmis[2]
    olusturalacak_paket[45] = Kademe_GPS_boylam_cevrilmis[3]




    Jriskop_X_cevrilmis = sayi_byte_cevir(Jriskop_X)

    olusturalacak_paket[46] = Jriskop_X_cevrilmis[0]
    olusturalacak_paket[47] = Jriskop_X_cevrilmis[1]
    olusturalacak_paket[48] = Jriskop_X_cevrilmis[2]
    olusturalacak_paket[49] = Jriskop_X_cevrilmis[3]



    Jriskop_Y_cevrilmis = sayi_byte_cevir(Jriskop_Y)

    olusturalacak_paket[50] = Jriskop_Y_cevrilmis[0]
    olusturalacak_paket[51] = Jriskop_Y_cevrilmis[1]
    olusturalacak_paket[52] = Jriskop_Y_cevrilmis[2]
    olusturalacak_paket[53] = Jriskop_Y_cevrilmis[3]



    Jriskop_Z_cevrilmis = sayi_byte_cevir(Jriskop_Z)

    olusturalacak_paket[54] = Jriskop_Z_cevrilmis[0]
    olusturalacak_paket[55] = Jriskop_Z_cevrilmis[1]
    olusturalacak_paket[56] = Jriskop_Z_cevrilmis[2]
    olusturalacak_paket[57] = Jriskop_Z_cevrilmis[3]



    ivme_X_cevrilmis = sayi_byte_cevir(ivme_X)

    olusturalacak_paket[58] = ivme_X_cevrilmis[0]
    olusturalacak_paket[59] = ivme_X_cevrilmis[1]
    olusturalacak_paket[60] = ivme_X_cevrilmis[2]
    olusturalacak_paket[61] = ivme_X_cevrilmis[3]



    ivme_Y_cevrilmis = sayi_byte_cevir(ivme_Y)

    olusturalacak_paket[62] = ivme_Y_cevrilmis[0]
    olusturalacak_paket[63] = ivme_Y_cevrilmis[1]
    olusturalacak_paket[64] = ivme_Y_cevrilmis[2]
    olusturalacak_paket[65] = ivme_Y_cevrilmis[3]



    ivme_Z_cevrilmis = sayi_byte_cevir(ivme_Z)

    olusturalacak_paket[66] = ivme_Z_cevrilmis[0]
    olusturalacak_paket[67] = ivme_Z_cevrilmis[1]
    olusturalacak_paket[68] = ivme_Z_cevrilmis[2]
    olusturalacak_paket[69] = ivme_Z_cevrilmis[3]




    aci_cevrilmis = sayi_byte_cevir(aci)

    olusturalacak_paket[70] = aci_cevrilmis[0]
    olusturalacak_paket[71] = aci_cevrilmis[1]
    olusturalacak_paket[72] = aci_cevrilmis[2]
    olusturalacak_paket[73] = aci_cevrilmis[3]




    olusturalacak_paket[74] = Durum

    olusturalacak_paket[76] = 0x0D
    olusturalacak_paket[77] = 0x0A

    check_sum = 0
    i = 4
    while i < 75:
        check_sum += olusturalacak_paket[i]
        i += 1

    check_sum_degeri = check_sum % 256
    olusturalacak_paket[75] = check_sum_degeri


    hex_liste = list()
    i =0
    while i < 78:
        hexle = hex(olusturalacak_paket[i])
        i+=1
        hex_liste.append(hexle)



    result = bytes([int(x,0) for x in hex_liste])

    return result


