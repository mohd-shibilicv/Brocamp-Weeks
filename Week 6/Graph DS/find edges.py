class Graph:
    def __init__(self) -> None:
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
            self.graph_dict[vertex2].append(vertex1)

    def has_edges(self, vertex1, vertex2):
        return vertex1 in self.graph_dict and vertex2 in self.graph_dict[vertex1]
    
    def get_edge(self, vertex):
        return self.graph_dict[vertex]

    def display(self):
        for vertex in self.graph_dict:
            print(vertex, ":", " -> ".join(self.graph_dict[vertex]))

    
graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

graph.display()

print("Is there an edge between D and A :", graph.has_edges("D", "A"))

print("What are the edges of C :", graph.get_edge("C"))

