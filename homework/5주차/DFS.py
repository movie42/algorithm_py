# DFS 깊이 우선 탐색
# 시작 노드에서 가장 깊은 곳까지 먼저 탐색한 후에 그곳에서 다른 깊이로 탐색하는 방법
# 스텍과 큐를 활용함

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


def DFS(graph, start_node):
    will_visit, visited = [], []

    will_visit.append(start_node)

    while will_visit:
        node = will_visit.pop()
        if node not in visited:
            visited.append(node)
            will_visit.extend(graph[node])
    return visited


print(DFS(graph, "A"))
