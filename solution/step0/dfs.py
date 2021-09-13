def solution(N, M, V, edges):
    graph = {}
    for i in edges:
        if i[0] not in graph:
            graph[i[0]] = [i[1]]
        else:
            graph[i[0]].append(i[1])
        if i[1] not in graph:
            graph[i[1]] = [i[0]]
        else:
            graph[i[1]].append(i[0])

    def dfs(start):
        visit = list()
        stack = list()

        stack.append(start)

        while stack:
            node = stack.pop()
            if node not in visit:
                visit.append(node)
                stack.extend(graph[node])
        return visit
    return dfs(V)



N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

print(solution(N, M, V, edges))