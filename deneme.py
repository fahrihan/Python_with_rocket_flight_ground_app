import serial
import serial.tools.list_ports

 #tools.list_ports.comports()
port_tara = serial.tools.list_ports.comports()
portlar = []

for i in port_tara:

    portlar.append(i[0])

print(portlar)


Takim_id = 155
Sayac = 1