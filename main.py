import sys
import time

from PyQt5.QtWidgets import QDialog,QApplication,QSplashScreen,QMainWindow

from PyQt5.QtCore import Qt

import serial.tools.list_ports

import acilis_ekrani
import ana_ekran
import hyi_protkol
import yer_istasyonu_veri_alma
class acilis_ekran(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        self.acilma_islem()

    def acilma_islem(self):
        self.ui = acilis_ekrani.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Magnetar Takımı")
        self.setWindowFlag(Qt.FramelessWindowHint)

    def acilma_suresi(self):
        for i in range(100):
            time.sleep(0.03)
            self.ui.yukleme_bar.setValue(i)



class Ana_ekran(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ana_baslangic_islem()

        self.ui.ekran_degistir_anaekran.clicked.connect(self.ekran_degistir_ana_ekrandan_bilgiye)
        self.ui.ekran_degistir_bilgi.clicked.connect(self.ekran_degistir_bilgiden_ana_ekrana)
        self.ui.btn_kapa.clicked.connect(self.uygulama_kapat)


        self.ui.yer_istasyon_baglan.clicked.connect(self.yer_com_sec)
        self.ui.hyi_baglan.clicked.connect(self.hyi_com_sec)



    def ana_baslangic_islem(self):
        self.ui = ana_ekran.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.com_ekle_yer()
        self.com_ekle_hyi()



    def ekran_degistir_ana_ekrandan_bilgiye(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def ekran_degistir_bilgiden_ana_ekrana(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def uygulama_kapat(self):
        app.exec_(sys.argv)

    def com_ekle_yer(self):
        port_tara = serial.tools.list_ports.comports()
        portlar = []
        for i in port_tara:
            portlar.append(i[0])
        for j in portlar:
            j = str(j)
            self.ui.yer_combox.addItem(j)

    def com_ekle_hyi(self):
        port_tara = serial.tools.list_ports.comports()
        portlar = []
        for i in port_tara:
            portlar.append(i[0])
        for j in portlar:
            j = str(j)
            self.ui.hyi_combox.addItem(j)

    def yer_com_sec(self):
        com = self.ui.yer_combox.currentText()
        print(com,11)
        self.veri_guncelle(com)

    def hyi_com_sec(self):
        self.hyi_com = self.ui.hyi_combox.currentText()


    def veri_guncelle(self,com):
        istasyon_alici = serial.Serial(port=com, baudrate=115200, stopbits=1)
        #self.hyi_com_sec()
        #hyi_gonder = serial.Serial(port=self.hyi_com, baudrate=115200, stopbits=1)

        Takim_id = 155
        Sayac = 1

        gelen_veriler = istasyon_alici.readline()

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

        Sayac = 1

        Takim_id = 11

        gonderilecek_veri = hyi_protkol.yer_istasyonu_protokol(irtifa_Roket, irtifa_Roket_GPS, Roket_GPS_enlem,
                                                               Roket_GPS_boylam, Roket_X_ekseni, Roket_Y_ekseni,
                                                               Roket_Z_ekseni, Payload_GPS_irtifa,
                                                               Payload_GPS_enlem, Payload_GPS_boylam, Sayac,
                                                               Roket_durum, Takim_id)


        #hyi_gonder.write(gonderilecek_veri)

        self.ui.t_id.setText(str(Takim_id))
        self.ui.sayac.setText(str(Sayac))
        self.ui.R_irtifa.setText(str(irtifa_Roket))
        self.ui.R_gps_irtifa.setText(str(irtifa_Roket_GPS))
        self.ui.R_enlem.setText(str(Roket_GPS_enlem))
        self.ui.R_boylam.setText(str(Roket_GPS_boylam))
        self.ui.R_gps_uydu.setText(str(Roket_uydu))
        self.ui.kurtarma_d.setText(str(Roket_durum))
        self.ui.R_x_v.setText(str(Roket_X_ekseni))
        self.ui.R_y_v.setText(str(Roket_Y_ekseni))
        self.ui.R_z_v.setText(str(Roket_Z_ekseni))
        self.ui.P_gps_irtifa.setText(str(Payload_GPS_irtifa))
        self.ui.P_gps_enlem.setText(str(Payload_GPS_enlem))
        self.ui.P_gps_boylam.setText(str(Payload_GPS_boylam))
        self.ui.P_gps_uydu.setText(str(Payload_uydu))

        print(Sayac)
        Sayac += 1

        time.sleep(1)

        istasyon_alici.close()
        self.yer_com_sec()



        if Sayac ==255:
            Sayac = 0

    def yer_kes(self):
        print("asdasdasdads")

if __name__ == "__main__":


    app = QApplication(sys.argv)
    acilma = acilis_ekran()
    acilma.show()
    acilma.acilma_suresi()

    ana_ekran = Ana_ekran()

    acilma.finish(ana_ekran)


    ana_ekran.show()

    app.exec_()
