class network:
    # Bleibt immer bestehen, allerdings kann der Fluss mithilfe der Funktion "augmentiere_um_epsilon" verändert werden
    def __init__(self,edges,capacity,source,sink,flow):
        self.edges = edges
        self.capacity = capacity
        self.source = source
        self.sink = sink
        self.flow = flow

    def augmentiere_um_epsilon(self,path):
        #Der path stammt aus dem Restgraphen
        epsilon = []
        for i in range(len(path)-1):
            if (path[i],path[i+1]) in self.edges and (path[i+1],path[i]) not in self.edges:
                x = self.edges.index((path[i],path[i+1]))
                epsilon.append(self.capacity[x]-self.flow[x])
            if (path[i],path[i+1]) not in self.edges and (path[i+1],path[i]) in self.edges:
                epsilon.append(self.flow[self.edges.index((path[i+1],path[i]))])
            if (path[i],path[i+1]) in self.edges and (path[i+1],path[i]) in self.edges:
                x = self.edges.index((path[i],path[i+1]))
                epsilon.append(max([self.capacity[x]-self.flow[x], self.flow[self.edges.index((path[i+1],path[i]))]]))
        epsilon = min(epsilon)
        
        for i in range(len(path)-1):
            if (path[i],path[i+1]) in self.edges and (path[i+1],path[i]) not in self.edges:
                x = self.edges.index((path[i],path[i+1]))
                self.flow[x] = self.flow[x] + epsilon
            if (path[i],path[i+1]) not in self.edges and (path[i+1],path[i]) in self.edges:
                x = self.edges.index((path[i+1],path[i]))
                self.flow[x] = self.flow[x] - epsilon
            if (path[i],path[i+1]) in self.edges and (path[i+1],path[i]) in self.edges:
                x = self.edges.index((path[i],path[i+1]))
                if self.capacity[x]-self.flow[x] > self.flow[self.edges.index((path[i+1],path[i]))]:
                    self.flow[x] = self.flow[x] + epsilon
                else:
                    x = self.edges.index((path[i+1],path[i]))
                    self.flow[x] = self.flow[x] - epsilon


class residual_graph:
    def __init__(self,network):
        self.edges_in_residual = []
        self.residual_capacity = []
        for i in range(len(network.edges)):
            if network.flow[i] < network.capacity[i]:
                self.edges_in_residual.append(network.edges[i])
                self.residual_capacity.append(network.capacity[i]-network.flow[i])
            if network.flow[i] > 0:
                a = network.edges[i]
                b = (a[1],a[0])
                self.edges_in_residual.append(b)
                self.residual_capacity.append(network.flow[i])
    
    def search_in_residual(self, source, sink):
        #Suche einen s-t-Weg
        found = False
        R = [source]
        Q = [source]
        p = {}
        while len(Q) > 0:
            v = Q[0]
            for (x,w) in self.edges_in_residual:
                if x == v:
                    if w not in R:
                        R.append(w)
                        Q.append(w)
                        p[w] = v
                        if w == sink:
                            found = True
                            break      
            if found == False:
                Q.remove(Q[0])
            else:
                Q = []
                path = [sink]
                y = sink
                while y != source:
                    path.append(p[y])
                    y = p[y]
                path.reverse()
                return(path)


def Ford_Fulkerson(network):
    network.flow = [0 for i in range(len(network.edges))]
    network_augmented = network
    path_exists = True
    while path_exists == True:
        residual_current = residual_graph(network_augmented)
        augmented_path = residual_current.search_in_residual(network.source, network.sink)
        if augmented_path == None:
            path_exists = False
        else:
            network_augmented.augmentiere_um_epsilon(augmented_path)
    return(network_augmented.flow)

##################################################################################################

#Veranschaulichung anhand des Beispiels aus der Aufgabenstellung
with open("netzwerk.txt", "r") as file:
    reader = file.read()
    reader = reader.split()
    edges = []
    capacity = []
    source = 4
    sink = 5
    for x in range(int(len(reader)/3)): #Da Länge immer durch 3 teilbar nicht durch int verfälscht
       edges.append((int(reader[3*x]),int(reader[3*x+1])))
       capacity.append(int(reader[3*x+2]))
    #Da alle Einträge ganzzahlig sind, kann hier int statt float verwendet werden

Network = network(edges, capacity, source, sink, None)

#Stelle Durchfluss f der Kanten dar:
print(Ford_Fulkerson(Network))

#Max_Flow(N):
result = 0
for (x,y) in Network.edges:
    if x == source:
        result = result + Network.flow[Network.edges.index((x,y))]
print(result)