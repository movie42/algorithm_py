# BFS 깊이 우선 탐색
# 시작 노드에서 형제 노드를 우선으로 탐색하는 방법
# 큐를 활용함


graph = {}

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["D"] = ["B", "E", "F"]
graph["E"] = ["D"]
graph["F"] = ["D"]
graph["H"] = ["C"]
graph["G"] = ["C"]
graph["C"] = ["A", "G", "H", "I"]
graph["I"] = ["C", "J"]
graph["J"] = ["I"]


def BFS(graph, start_node):
    will_visit, visited = [], []

    will_visit.append(start_node)

    while will_visit:
        node = will_visit.pop(0)
        if node not in visited:
            visited.append(node)
            will_visit.extend(graph[node])
    return visited


["A", "B", "C", "D", "G", "H", "I", "E", "F", "J"]
print(BFS(graph, "A"))
