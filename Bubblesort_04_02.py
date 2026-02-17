import numpy
import time
import matplotlib.pyplot as plt

def bubblesort(N):
    start = time.time()

    S = numpy.random.randint(low=0, high= 99, size=N)
    sigma =[i for i in range(N)]
    for i in range(0, N-1): #der code muss hier bei 0 starten, da unsere Listen bei .py zero-indexed sind
        for j in range(i+1, N):
            if S[sigma[j]] < S[sigma[i]]:
                tmp = sigma[i]
                sigma[i] = sigma[j]
                sigma[j] = tmp

    end = time.time()

    return end - start

# Das Programm vergleicht Werte in S, tauscht jedoch nur eine Liste der Indizes.
#Also wird nicht die geordnete Liste S ausgegeben, sondern eine "Anleitung" zum sortieren von S.

n_liste = [10**i for i in range(5)]
laufzeiten = [bubblesort(n) for n in n_liste]

plt.plot(n_liste, laufzeiten)
plt.show()