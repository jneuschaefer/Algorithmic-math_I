import math
import matplotlib.pyplot as mlt

#Aufgabe 4a)
def geteps():
    y = 1
    while 1+y != 1:
        y = 0.5*y
    return 2*y

def getmin():
    y = 1
    while y != 0:
        altes_y = y
        y = 0.5*altes_y
    return altes_y
#altes_y, da 2*y sonst als 0.0 angezeigt wird

def getmax():
    y = 1
    while y < math.inf:
        y = 2*y
    return y
#Die wortwörtliche Implementierung der Aufgabenstellung führt zu keinem brauchbaren Ergebnis.

def getmax_2():
    y = 1
    try:
        while math.inf - y > 0:
            y = 2*y
        return "Hat funktioniert: %f" %(y)
    except OverflowError:
        return y
# liefert maximale Größe Float
# Maximum würde irgendwo zwischen y und 2*y liegen

#Aufgabe 4b)
x = 1
h = [2**(-a) for a in range(0,31)]
Ergebnis_Näherung = []
for i in h:
    a = (math.cos(x+i) - math.cos(x-i))/(2*i)
    Ergebnis_Näherung.append(a)
Ergebnis_tatsächlich = -math.sin(x)
print(Ergebnis_Näherung)
print(Ergebnis_tatsächlich)
absoluter_Fehler = [abs(Ergebnis_Näherung[i] - Ergebnis_tatsächlich) for i in range(len(Ergebnis_Näherung))]
relativer_Fehler = [abs(absoluter_Fehler[i] / Ergebnis_tatsächlich) for i in range(len(absoluter_Fehler))]
#abs(), da log10() nicht mit negativen Werten arbeiten kann

x_values = [math.log10(x) for x in h]
f_values = [math.log10(x) for x in absoluter_Fehler]
g_values = [math.log10(x) for x in relativer_Fehler]
mlt.plot(x_values, f_values, label="Absoluter Fehler")
mlt.plot(x_values, g_values, label="Relativer Fehler")
mlt.legend(loc="best")
mlt.xlabel("log(h)")
mlt.ylabel("log(Fehler)")
mlt.show()

mlt.plot(f_values, g_values) 
mlt.show()