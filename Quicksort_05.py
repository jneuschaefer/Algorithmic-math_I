import numpy as np
import numpy.random as nr
import time
import matplotlib.pyplot as mlt

def quicksort(a):
    x = a[0]
    R = []
    L = []
    for n in range(1,len(a)):
        if a[n]>=x:
            R.append(a[n])
        else:
            L.append(a[n])
    if len(R) != 0:
        R = quicksort(R)
    if len(L) != 0:
        L = quicksort(L)
    x = np.array([x])
    ergebnis = 0
    ergebnis = np.concatenate([L,x,R])
    return ergebnis

def quicksort_in_place(a,start = 0,laenge = None):
    if laenge is None:
        laenge = len(a)
    k = start
    for n in range(k,laenge):
        if a[k] > a[n]:
            x = a[n]
            y = a[k]
            k = k+1
            for i in range(n-1,k-1,-1):
                a[i+1] = a[i]
            a[k-1] = x
            a[k] = y
    if  k != laenge:
        quicksort_in_place(a, start = k+1, laenge = laenge)
    if  k != start:
        quicksort_in_place(a, start = start,laenge = k)
    return a

def ist_sortiert(a):
    ergebnis = True
    for n in range(len(a)-1):
        if a[n]>a[n+1]:
            ergebnis = False
    return ergebnis


f_values = []
x_values = []
#hier Länge der Liste beliebig anpassen
for k in range(0,16):
    x_values.append(2**k)
    a = nr.randint(100, size = 2**k)
    start = time.time()
    b = quicksort_in_place(a)
    end = time.time()
    f_values.append(end-start)
    if ist_sortiert(b) == False:
        print("Nicht sortiert!")



mlt.plot(x_values, f_values, label = "Quicksort")
mlt.legend(loc = "best")
mlt.xlabel("Länge der Liste")
mlt.ylabel("Dauer des Sortierens in s")
mlt.show()
#mlt.savefig("Versuch.png")
#print("Fertig!")