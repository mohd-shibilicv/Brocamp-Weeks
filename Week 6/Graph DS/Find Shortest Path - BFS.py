from collections import deque


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
            self.graph_dict[vertex2].append(vertex1)

    def display(self):
        for vertex in self.graph_dict:
            path = " -> ".join(self.graph_dict[vertex])
            print(f"{vertex} : {path}")

    def has_edge(self, vertex1, vertex2):
        return vertex1 in self.graph_dict and vertex2 in self.graph_dict[vertex1]
    
    def get_edges(self, vertex):
        return self.graph_dict[vertex]
    
    def find_shortest_path_BFS(self, start, end):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            vertex, path = queue.popleft()
            visited.add(vertex)
            if vertex == end:
                return path
            
            for neighbour in self.graph_dict[vertex]:
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour]))
        
        return None
    
    def print_shortest_path(self, start, end):
        path = self.find_shortest_path_BFS(start, end)

        if path is None:
            print(f"No path is found between {start} and {end}")
        else:
            print(f"Shortest path between {start} and {end} :", " -> ".join(path))
    
    def DFS(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbour in self.graph_dict:
            if neighbour not in visited:
                self.DFS(neighbour, visited)
    
    def BFS(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(self.graph_dict[vertex])


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

print("Is there an edge between D and A :", graph.has_edge("D", "A"))

print("What are the edges of C :", graph.get_edges("C"))

print("Depth First Search Traversal :", end=" ")
graph.DFS("D")
print()
print("Breadth First Search Traversal :", end=" ")
graph.BFS("D")
print()

graph.print_shortest_path("A", "C")
