import matplotlib.pyplot as mlt

def naive_Dreitermrekursion(n,a,b,c,p0,p1):
    p = [p0,p1]
    if type(a) != list:
        a = [a for x in range(n)]
    if type(b) != list:
        b = [b for x in range(n)]
    if type(c) != list:
        c = [c for x in range(n)]
    for k in range(2,n):
        x = a[k]*p[k-1]+b[k]*p[k-2]+c[k]
        p.append(x)
    return p

def geschlossene_Lösung(n,a,b,p0,p1):
    lambda1 = a/2 + (a*a/4 +b)**0.5
    lambda2 = a/2 - (a*a/4 +b)**0.5
    beta = (p1-lambda1*p0)/(lambda2-lambda1)
    alpha = p0-beta
    p = [p0,p1]
    l1 = lambda1
    l2 = lambda2
    for k in range(2,n):
        l1 = l1*lambda1
        l2 = l2*lambda2
        x = alpha*l1+beta*l2
        p.append(x)
    return p

def Miller_Algorithmus(m,a,b,p0,p1):
    #wähle n groß
    n = 100
    p_ = [0 for x in range(0,101)]
    p_[n] = 0
    p_[n-1] = 1
    for x in range(n, 1,-1):
        p_[x-2] = (-a/b)*p_[x-1]+(1/b)*p_[x]
    p = [p0,p1]
    for k in range(2,m):
        x = p_[k]/((p_[0]**2 + p_[1]**2)**0.5)
        p.append(x)
    return p

n = 50
a = -2
b = 1
c = 0
p0 = 1
p1 = (2**0.5)-1
x = naive_Dreitermrekursion(n,a,b,c,p0,p1)
y = geschlossene_Lösung(n,a,b,p0,p1)
z = Miller_Algorithmus(n,a,b,p0,p1)

x_values = [x for x in range(n)]

fig, axes = mlt.subplots(3)
fig.suptitle("Dreitermrekursion-Algorithmen")
axes[0].plot(x_values, x)
axes[0].set_title("Naive Dreitermrekursion")
axes[1].plot(x_values, y)
axes[1].set_title("Geschlossene Lösung")
axes[2].plot(x_values, z)
axes[2].set_title("Miller-Algorithmus")
mlt.show()

#etwas gequetscht, schwer zu sehen

mlt.plot(x_values, x, label="Naive Dreitermrekursion")
mlt.legend(loc = "best")
mlt.show()
mlt.plot(x_values, y, label="Geschlossene Lösung")
mlt.legend(loc = "best")
mlt.show()
mlt.plot(x_values, z, label="Miller-Algorithmus")
mlt.legend(loc = "best")
mlt.show()
#erscheinen nacheinander