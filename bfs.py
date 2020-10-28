import csv
from collections import deque
aux = []
aux2 = []
vertices = []

class Vertice:
    def __init__(self, id):
        self.id = id
        self.visitado = False
        self.adjacencia = []

    def get_id(self):
        return self.id

    def get_visitado(self):
        return self.visitado

    def get_adjacencia(self):
        return self.adjacencia

    def set_visitado(self, value):
        self.visitado = value

    def set_adjacencia(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia.append(vertice)
            self.adjacencia.sort()

    def __str__(self):
        return 'Vertice: {}\nAdjacente: {}'.format(self.id, self.adjacencia)


#print(Vertice(1))

class Aresta:
    def __init__(self, origem: Vertice, destino: Vertice, peso=None):
        self.origem = origem
        self.destino = destino
        self.peso = peso

    def get_origem(self):
        return self.origem

    def get_destino(self):
        return self.destino

    def set_origem(self, nova_origem: Vertice):
        self.origem = nova_origem

    def set_destino(self, novo_destino: Vertice):
        self.destino = novo_destino

    def __str__(self):
        return '{} -> {}'.format(self.origem.get_id(), self.destino.get_id()) # 1 -> 2


#vertice1 = Vertice(1)
#vertice2 = Vertice(2)

#print(Aresta(vertice1, vertice2))

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []
        #self.DFS = []
        self.BFS = []

    def novo_vertice(self, novo_vertice):
        self.vertices.append(Vertice(novo_vertice))

    def nova_aresta(self, origem, destino):
        origemAUX = self.busca_vertice(origem)
        destinoAUX = self.busca_vertice(destino)
        if origemAUX and destinoAUX:
            self.arestas.append(Aresta(origemAUX, destinoAUX))
            self.arestas.append(Aresta(destino, origem)) #quando eu tenho nessa linha e a de cima. e grafo n direcional
            origemAUX.set_adjacencia(destino)
            destinoAUX.set_adjacencia(origem)
            self.create_adjacencia()
        else:
            print('um dos vertices n é valido. origem: {}\tdestino: {}'.format(origem,destino))

    def busca_vertice(self, id):
        for vertice in self.vertices:
            if vertice.get_id() == id:
                return vertice

        return None

    def get_all_vertices(self):
        for x in self.vertices:
            print(x)

    def get_all_arestas(self):
        for x in self.arestas:
            print(x)

    def create_adjacencia(self):
        self.adjacentes = {}
        for x in self.vertices:
            self.adjacentes[x.get_id()] = x.get_adjacencia()

    def set_visitado(self, vertice):
        for x in self.vertices:
            if x.get_id() == vertice.get_id():
                x.set_visitado(True)
            else:
                x.set_visitado(False)

    def BFS_lindo(self, raiz):
        self.BFS.clear()
        raizAUX = self.busca_vertice(raiz) #ve se a raiz existe na lsita de vertices
        self.set_visitado(raizAUX) #se sim já seta como visitado
        self.BFS.append(raiz) # e coloca no vetor BFS
        self.visita_BFS(raizAUX)
        return self.BFS

    def visita_BFS(self, vertice):
        fila = [vertice] #inicio da nossa fila já com o raiz gostoso
        while fila: #ou len(fila) != 0
            vertice = fila[0] #pega o primeiro vertice da fila
            for adjacente in vertice.get_adjacencia(): 
                verticeAUX = self.busca_vertice(adjacente) #busca o adjacente e salva
                if not verticeAUX.get_visitado(): #se o adjacente n tiver sido visitado
                    verticeAUX.set_visitado(True)
                    self.BFS.append(adjacente)
                    fila.append(verticeAUX)
            fila.pop(0)

    def __repr__(self):
        for x in self.arestas:
            print(x)

        for x in self.vertices:
            print(x)

def main():
    grafo = Grafo()
    with open('teste.csv') as csvfile:
        hualian = csv.reader(csvfile, delimiter=';')
        for row in hualian:
            aux.append(int(row[0]))
            aux2.append(int(row[1]))
            aux3 = aux + aux2

    seen = set()
    for x in aux3:
        if x not in seen:
            vertices.append(x)
            seen.add(x)       
    vertices.sort()

    for x in vertices:
        grafo.novo_vertice(x)

    for x,y in zip(aux,aux2):
        grafo.nova_aresta(x,y)

    print(grafo.BFS_lindo(vertices[0]))

if __name__ == '__main__':
    main() 