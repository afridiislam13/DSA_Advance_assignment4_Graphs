# 1. Breadth First Traversal for a Graph.

from collections import defaultdict, deque

def bfs(graph, start_vertex):
    visited = defaultdict(bool)
    # Create a queue for BFS
    queue = deque()
    queue.append(start_vertex)
    visited[start_vertex] = True

    # BFS traversal
    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end=" ")

        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

print("Breadth-First Traversal starting from vertex 'A':")
bfs(graph, 'A')

# 2. Depth First Traversal for a Graph.

def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(start_vertex)
    print(start_vertex, end=" ")

    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
print("Depth-First Traversal starting from vertex 'A':")
dfs(graph, 'A')

# 3. Count the number of nodes at given level in a tree using BFS.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def count_nodes_at_level(root, target_level):
    if not root:
        return 0

    queue = deque([(root, 0)])
    count_at_level = 0

    while queue:
        node, level = queue.popleft()

        if level == target_level:
            count_at_level += 1

        for child in node.children:
            queue.append((child, level + 1))

    return count_at_level

root = TreeNode('A')
root.children = [TreeNode('B'), TreeNode('C')]
root.children[0].children = [TreeNode('D'), TreeNode('E')]
root.children[1].children = [TreeNode('F')]
root.children[0].children[1].children = [TreeNode('G')]

target_level = 2
count = count_nodes_at_level(root, target_level)
print(f"Number of nodes at level {target_level}: {count}")

# 4. Count number of trees in a forest.

from collections import defaultdict

def dfs(graph, start_vertex, visited):
    visited.add(start_vertex)

    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def count_trees_in_forest(graph):
    num_trees = 0
    visited = set()

    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited)
            num_trees += 1

    return num_trees

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B'],
    'F': ['G'],
    'G': ['F']
}

num_trees = count_trees_in_forest(graph)
print("Number of trees in the forest:", num_trees)

# 5. Detect Cycle in a Directed Graph.

def has_cycle(graph):
    def dfs(vertex, visited, recursion_stack):
        visited[vertex] = True
        recursion_stack[vertex] = True

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:  # Cycle detected
                return True

        recursion_stack[vertex] = False
        return False

    num_vertices = len(graph)
    visited = [False] * num_vertices
    recursion_stack = [False] * num_vertices

    for vertex in range(num_vertices):
        if not visited[vertex]:
            if dfs(vertex, visited, recursion_stack):
                return True

    return False

# Example graph as an adjacency list representing a directed graph with a cycle
graph_with_cycle = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [2]
}

graph_without_cycle = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4],
    4: []
}

print("Has cycle in graph_with_cycle:", has_cycle(graph_with_cycle))
print("Has cycle in graph_without_cycle:", has_cycle(graph_without_cycle))
