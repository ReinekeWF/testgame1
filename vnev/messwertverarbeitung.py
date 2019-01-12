import time
import matplotlib.pyplot as mpl

datei = open("C:/Users/PCBenutzer/Desktop/messwerte.txt","r")
zeiten = []
watt = []
volt = []
ampere = []

x = 0
for inhalt in datei:
    if x == 10:
        break
    zerlegt = inhalt.split()
    zeiten.append(zerlegt[3])
    watt.append(zerlegt[6])
    volt.append(zerlegt[7])
    ampere.append(zerlegt[8])
    x += 1
    #time.sleep(1)

mpl.plot(zeiten,ampere,'')
mpl.plot(zeiten,volt,'')


mpl.show()
print(zeiten)
print(watt)
print(volt)
print(ampere)
