import numpy.random as nr
import matplotlib.pyplot as mlt
import time

def bubblesort(a):
    n = len(a)
    for k in range(n-1,0,-1):
        swapped = 0
        for l in range(0,k):
            if a[l] > a[l+1]:
                x = a[l] 
                a[l] = a[l+1]
                a[l+1] = x
            swapped = swapped + 1
        if swapped == 0:
            break
    return 

f_values = []
x_values = []
#hier Länge der Liste beliebig anpassen
for k in range(0,5):
    x_values.append(k)
    a = nr.randint(100, size = 10**k)
    start = time.time()
    bubblesort(a)
    end = time.time()
    f_values.append(end-start)



mlt.plot(x_values, f_values, label = "Bubblesort")
mlt.legend(loc = "best")
mlt.xlabel("Länge der Liste in 10^x")
mlt.ylabel("Dauer des Sortierens in s")
mlt.show()
#mlt.savefig("Versuch.png")
#print("Fertig!")