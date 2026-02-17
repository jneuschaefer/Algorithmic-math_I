import time
import matplotlib.pyplot as mlt
import timeit

def fibonacci_rekursiv(n):
    if n == 0 or n == 1:
        return 1
    ergebnis = fibonacci_rekursiv(n-1) + fibonacci_rekursiv(n-2)
    return ergebnis

for i in range(1,31):
    print(fibonacci_rekursiv(i))

def fibonacci_iterativ(n):
    ergebnis = 1
    prepre = 1
    pre = 1
    for i in range(2,n+1):
        ergebnis = pre + prepre
        prepre = pre
        pre = ergebnis
    return ergebnis

for i in range(1,31):
    print(fibonacci_iterativ(i))

x_values = []
g_values = []
f_values = []
rekursiv = []
iterativ = []
for i in range(1,36):
    x_values.append(i)
    start = time.time()
    a = fibonacci_iterativ(i)
    end = time.time()
    z=timeit.timeit(lambda: fibonacci_iterativ(i), number=1)
    iterativ.append(a)
    f_values.append(z)
    start = time.time()
    b = fibonacci_rekursiv(i)
    end = time.time()
    rekursiv.append(b)
    g_values.append(end-start)

print([iterativ[i] for i in range(20)])
print([rekursiv[i] for i in range(20)])
#print(g_values)
#print(f_values)

mlt.semilogy(x_values,g_values, label = "Rekursiv")
mlt.semilogy(x_values,f_values, label = "Iterativ")
mlt.xlabel("n")
mlt.ylabel("Dauer in s")
mlt.legend(loc = "best")
mlt.show()