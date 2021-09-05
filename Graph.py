class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connected to: ' + str([vertex.id for vertex in self.connectedTo]) 

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo(nbr)

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        v = Vertex(key)
        self.vertList[key] = v
        self.numVertices += 1
        return v

    def getVertex(self, vertKey):
        if self.vertList[vertKey]:
            return self.vertList[vertKey]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, fromVert, toVert, cost=0):
        if fromVert not in self.vertList:
            self.addVertex(fromVert)
        if toVert not in self.vertList:
            self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)

g.addEdge(0,1,2)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')