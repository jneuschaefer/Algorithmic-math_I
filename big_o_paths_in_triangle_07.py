import math
import timeit
import numpy.random as nr
import time
import matplotlib.pyplot as mlt
import random

#Unser Dreieck ist eine einfache Liste
def Dreieck(d):
    Dreieck = []
    for i in range(1,d+1):
        for q in range(1,i+1):
            Dreieck.append(random.randint(1,99))
    return Dreieck

#Unser Suchalgorithmus liest eine Liste (reversed) ein,
#erkennt anhand der Anzahl der Elemente die Struktur des Dreiecks,
#und ermittelt via backward induction den kürzesten Weg
def Suche(a):
    Tiefe = 1/2*(-1 + math.sqrt(1+8*len(a)))  #Schritt 1: Ermittle Tiefe
    w=int(Tiefe)

    e=[] #Schritt 2: Wir schauen uns die unterste Ebene an, und bestimmen den jeweis optimalen Pfad (und eliminieren den strikt dominierten Pfad).
    for i in range(0,w-1):
        t=int(a[i])
        z=int(a[i+1])
        if t>z:
            e.append(z)
        else:
            e.append(t)

    r =[] #Schritt 3: Wir wissen nun, für eine Ebene höher, welcher nächste Pfad optimal ist. Wir gehen also eine Ebene höher und summieren die Länge des gerade ermittelten Folgepfads.
    for i in range(w, len(a)):
        r.append(a[i])
    for i in range(0, len(e)):
        r[i]=r[i]+e[i]

    if len(r)>1:
        #print(r)
        a=Suche(r)
        return(a)
    else:
        return(r)

#Als Illustration für die Funktionsweise hier das Beispiel-Dreieck vom Zettel:
a = [41, 30, 38, 62, 26, 87, 71, 38, 67, 16]
print(a)
# wir wollen bottom-up verfahren, und drehen daher die Liste um (backward induction)
a.reverse()
print(a)
print(Suche(a))

#Besitmme Laufzeit für beliebig groß-generierte Dreiecke:
f_values = []
x_values = []
#hier Länge der Liste beliebig anpassen
for k in range(1,200):
    
    z=0 #Für die x-Achse müssen wir von d auf n schließen:
    for i in range(1,k+1):
        z=z+i
    x_values.append(z)
    eins = Dreieck(k)
    eins.reverse()
    n=timeit.timeit(lambda: Suche(eins), number=1)
    f_values.append(n)

mlt.plot(x_values, f_values)
mlt.xlabel("n")
mlt.ylabel("Dauer der Suche in s")
mlt.show()