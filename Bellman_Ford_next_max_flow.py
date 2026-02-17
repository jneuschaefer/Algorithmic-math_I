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
        #Algorithmus von Moore-Bellman-Ford
        l = []
        p = [None for i in range(len(self.points))]
        l = [math.inf for i in range(len(self.points))]
        l[start] = 0
        for k in range(len(self.points)):
            for (x,y) in self.edges:
                if l[x] > l[y] + self.länge[(x,y)]:
                    l[x] = l[y] + self.länge[(x,y)]
                    p[x] = y
                if l[y] > l[x] + self.länge[(x,y)]:
                    l[y] = l[x] + self.länge[(x,y)] 
                    p[y] = x
        #lese aus p den Pfad von start nach ende heraus
        path = []
        x = self.points[ende]
        path.append(x)
        y = p[ende]
        path.append(self.points[y])
        while y != start:
            path.append(self.points[p[y]])
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