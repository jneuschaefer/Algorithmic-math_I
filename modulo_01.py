def modulo_addition(m,n):
    try:
        if "." in m or "." in n:
            print("Es können nur ganze Zahlen verarbeitet werden.")
            return
        n = int(n)
        m = int(m)
        if m > 0 and n > 0:
            q = 0
            while m >= n:
                m = m-n
                q = q+1
            r = m
            return "q = %i, r = %i" % (q,r)
        else:
            print("Es können nur positive Zahlen verarbeitet werden.")
            return
    except ValueError:
        print("Es können nur Zahlen verarbeitet werden.")

def modulo_division(m,n):
    try:
        if "." in m or "." in n:
            print("Es können nur ganze Zahlen verarbeitet werden.")
            return
        n = int(n)
        m = int(m)
        if m > 0 and n > 0:
            q = int(m/n)
            r = m - q*n
            return "q = %i, r = %i" % (q,r)
        else:
            print("Es können nur positive Zahlen verarbeitet werden.")
            return
    except ValueError:
        print("Es können nur Zahlen verarbeitet werden.")

print("Darstellung: m = n*q + r")
m = input("m = ")
n = input("n = ")
print(modulo_addition(m,n))