import matplotlib.pyplot as mlt
import csv
import math

#zunächst lesen wir die Informationen aus den Dateien als Listen ein
yKoord = []
with open("ycoords.txt") as csvfile:
    ycoords = csv.reader(csvfile, delimiter = " ")
    for row in ycoords:
        yKoord.append(float(row[0]))
xKoord = []
with open("xcoords.txt") as csvfile:
    xcoords = csv.reader(csvfile, delimiter = " ")
    for row in xcoords:
        xKoord.append(float(row[0]))
Kanten = []
with open("edges.txt") as csvfile:
    edges = csv.reader(csvfile)
    for row in edges:
        Kanten.append((int(row[0]), int(row[1])))


#hier haben wir Karten allgemein als Klasse mit Punkten und Kanten definiert
class Karte:
    #Initialisiere die Karte
    def __init__(self, edges, ycoords, xcoords):
        self.edges = edges
        self.ycoords = ycoords
        self.xcoords = xcoords
        self.points = [(self.xcoords[i], self.ycoords[i]) for i in range(len(self.xcoords))]
        #Bilde Gewichte durch euklidische Norm
        self.länge = {}
        for (x,y) in self.edges:
            self.länge[(x,y)] = ((self.xcoords[y] - self.xcoords[x])**2 + (self.ycoords[y] - self.ycoords[x])**2)**0.5

    #Zeige die Karte als Plot, optional mit bis zu zwei markierten Punkten
    def show(self, mark1 = None, mark2 = None):
        for (x,y) in self.edges:
            mlt.plot([self.xcoords[x], self.xcoords[y]],[self.ycoords[x],self.ycoords[y]], color = "black", linewidth = 0.5)
        if mark1 != None:
            mlt.scatter([self.xcoords[mark1]], [self.ycoords[mark1]], color = "red", marker = "x")
        if mark2 != None:
            mlt.scatter([self.xcoords[mark2]], [self.ycoords[mark2]], color = "red", marker = "x")
        mlt.show()

    #Berechne eine Weg vom Startpunkt zum Endpunkt, der auf der Karte eingezeichnet wird
    def weg(self, start, ende):
        #Algorithmus von Djistra
        R = []
        V_ohne_R = [self.points[i] for i in range(len(self.points))]
        #Länge und Parents hier wegen wechselnder Indizierung in V_ohne_R als dictionaries
        l = {}
        p = {}
        for v in V_ohne_R:
            if v == self.points[start]:
                l[v] = 0
            else:
                l[v] = math.inf
        #while R != self.points:
        while self.points[ende] not in R:
            #finde minimale Länge in V_ohne_R
            min = l[V_ohne_R[0]]
            index = 0
            for i in range(1,len(V_ohne_R)):
                if min>l[V_ohne_R[i]]:
                    min = l[V_ohne_R[i]]
                    index = i
            u = V_ohne_R[index]
            R.append(u)
            V_ohne_R.remove(u)
            for v in V_ohne_R:
                x = self.points.index(u)
                y = self.points.index(v)
                if (x, y) in self.edges:
                    if l[v]>l[u] + self.länge[(x, y)]:
                        l[v] = l[u] + self.länge[(x, y)]
                        p[v] = u
                elif (y, x) in self.edges:
                    if l[v]>l[u] + self.länge[(y, x)]:
                        l[v] = l[u] + self.länge[(y, x)]
                        p[v] = u
        #lese aus p den Pfad von start nach ende heraus
        path = []
        x = self.points[ende]
        path.append(x)
        y = p[x]
        path.append(y)
        while y != self.points[start]:
            path.append(p[y])
            y = p[y]
        #plotte zunächst den Weg und rufe dann show auf, um den Rest der Karte hinzuzufügen
        for i in range(len(path)-1):
            x = self.points.index(path[i])
            y = self.points.index(path[i+1])
            mlt.plot([self.xcoords[x], self.xcoords[y]],[self.ycoords[x],self.ycoords[y]], color = "red")
        self.show(mark1 = start, mark2 = ende)

Poppelsdorf = Karte(Kanten, yKoord, xKoord)
#Poppelsdorf.show(1758,584)
Poppelsdorf.weg(1758,584)