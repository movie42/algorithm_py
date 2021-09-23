# BFS
# 큐를 활용
# will_visit 큐, visited 큐를 생성

graph = {}

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(data, start_node):
    will_visit, visited = list(), list()
    will_visit.append(start_node)
    while will_visit:
        node = will_visit.pop(0)
        if node not in visited:
            visited.append(node)
            will_visit.extend(graph[node])
    return visited

print(bfs(graph, 'A'))