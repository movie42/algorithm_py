# DFS
# 스택과 큐를 활용
# will_visit 스택, visited 큐를 생성

graph = {}

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['H'] = ['C']
graph['G'] = ['C']
graph['C'] = ['A', 'G', 'H', 'I']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(data, start_node):
    will_visit, visited = list(), list()
    will_visit.append(start_node)
    while will_visit:
        node = will_visit.pop()
        if node not in visited:
            visited.append(node)
            will_visit.extend(data[node])
    return visited

print(dfs(graph, 'A'))

