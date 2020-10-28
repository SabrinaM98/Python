'''
DFS algorithm that counts the amount of 'steps' it takes to get from one vertex(origin) to a vertex(destiny).
This algorithm does not take in consideration the 'shortest path' bewteen two vertexes.
'''
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

    #grafo.get_all_arestas()
    #grafo.get_all_vertices()

    print(grafo.adjacentes)
    print(vertices[1])
    print(grafo.percorre_negada(vertices[1]))

if __name__ == '__main__':
    main() 

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.DFS = []

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

    def percorre_negada(self, origem, destiny=None): #conta saltos. tipo dijkstra só q conta saltos e entrega o primeiro caminho. n é o mais curto
        vertice = self.busca_vertice(origem)

        if not vertice:
            return 'vertice n existe bro'
        
        caminhos = {}
        percorre = [origem] #lista de vertices a serem percorridos 
        count = 1
        self.set_visitado(vertice) #setar o vertice de origem como visitado

        for key in percorre: #loop na lista de vertices a serem visitados
            for id_vertice in self.adjacentes[key]: #loop para percorrer os adjacentes dos visitados 
                destino = self.busca_vertice(id_vertice) #busca do objeto vertice
                if not destino.get_visitado(): #teste para saber se ja foi visitado
                    caminhos['{}-{}'.format(vertice.get_id(), id_vertice)] = count #definiçao da distancia da visitaçao
                    destino.set_visitado(True) #seta como visitado o vertice q foi percorrido
                    if destiny and destino.get_id() == destiny:
                        return count
                    for hualian in destino.get_adjacencia(): #loop de verificaçao de adjacentes n visitados
                        if not self.busca_vertice(hualian).get_visitado():
                            percorre.append(id_vertice)
                            
            count+=1 #contador de distancia

        return caminhos

    def DFS_lindo(self, raiz):
        self.DFS.clear()
        raizAUX = self.busca_vertice(raiz)
        self.set_visitado(raizAUX) #iniciando em raiz
        self.DFS.append(raiz)
        self.visita(raizAUX)
        return self.DFS

    def visita(self, vertice):
        for adjacente in vertice.get_adjacencia():
            verticeAUX = self.busca_vertice(adjacente)
            if not verticeAUX.get_visitado():
                verticeAUX.set_visitado(True)
                self.DFS.append(adjacente)
                self.visita(verticeAUX)         

    def __repr__(self):
        for x in self.arestas:
            print(x)

        for x in self.vertices:
            print(x)

aux = []
aux2 = []
vertices = []

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

    #grafo.get_all_arestas()
    #grafo.get_all_vertices()

    print(grafo.adjacentes)
    print(vertices[1])
    print(grafo.percorre_negada(vertices[1]))

if __name__ == '__main__':
    main() 
